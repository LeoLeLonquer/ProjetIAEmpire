open Actions ;;
open Connection ;;
open Empire ;;
open Mailbox ;;
open Misc ;;

let piece_types = Hashtbl.create 16 ;;

let config =
  { m_width = 40(*20*)
  ; m_height = 40(*12*)
  ; m_sea_level = -0.3 (*-0.3*)
  ; m_amplitude = 1.0
  ; m_octaves = 4
  ; m_persistence = 0.2
  ; m_frequency = 0.06
  ; m_cities_density = 0.2
  ; m_nb_players = 2
  ; m_piece_types = piece_types
  } ;;

Hashtbl.add piece_types 0
  { a_id = 0
  ; a_name = "ARMY"
  ; a_symbol = 'A'
  ; a_terrain = [Ground]
  ; a_build_time = 5
  ; a_strength = 1
  ; a_max_hits = 1
  ; a_speed = 1
  ; a_capacity = 0
  ; a_autonomy = None
  ; a_transportable = []
  ; a_visibility = 2
  ; a_can_invade = true
  } ;;

Hashtbl.add piece_types 1
  { a_id = 1
  ; a_name = "FIGHT"
  ; a_symbol = 'F'
  ; a_terrain = [Ground ; Water]
  ; a_build_time = 10
  ; a_strength = 1
  ; a_max_hits = 1
  ; a_speed = 8
  ; a_capacity = 0
  ; a_autonomy = Some 4
  ; a_transportable = []
  ; a_visibility = 4
  ; a_can_invade = false
  } ;;

Hashtbl.add piece_types 2
  { a_id = 2
  ; a_name = "TRANSPORT"
  ; a_symbol = 'T'
  ; a_terrain = [Water]
  ; a_build_time = 30
  ; a_strength = 1
  ; a_max_hits = 1
  ; a_speed = 2
  ; a_capacity = 4
  ; a_autonomy = None
  ; a_transportable = [0]
  ; a_visibility = 2
  ; a_can_invade = false
  } ;;

Hashtbl.add piece_types 3
  { a_id = 3
  ; a_name = "PATROL"
  ; a_symbol = 'P'
  ; a_terrain = [Water]
  ; a_build_time = 15
  ; a_strength = 1
  ; a_max_hits = 1
  ; a_speed = 4
  ; a_capacity = 0
  ; a_autonomy = None
  ; a_transportable = []
  ; a_visibility = 4
  ; a_can_invade = false
  } ;;

Hashtbl.add piece_types 4
  { a_id = 4
  ; a_name = "BATTLESHIP"
  ; a_symbol = 'B'
  ; a_terrain = [Water]
  ; a_build_time = 40
  ; a_strength = 2
  ; a_max_hits = 10
  ; a_speed = 2
  ; a_capacity = 0
  ; a_autonomy = None
  ; a_transportable = []
  ; a_visibility = 4
  ; a_can_invade = false
  } ;;

print_endline (Printf.sprintf "gerenerating game") ;;
let game = GameGen.create_game config ;;

(* Attente de la connexion des joueurs. *)
(* TODO: le premier joueur doit configurer la partie. *)
let port =
  let rec loop i =
    if i >= Array.length Sys.argv - 1 then 9301 else
    if Sys.argv.(i) = "-sport" then int_of_string (Sys.argv.(i + 1)) else
    loop (i + 1) in
  loop 0 ;;

let addr = Unix.inet_addr_loopback ;;

Printf.printf "server listening on 127.0.0.1:%d\n" port ;;
let server_sock = server_open game.g_nb_players addr port ;;
let connect_client _ =
  let socket = fst (Unix.accept server_sock) in
  { socket = socket
  ; in_channel = Unix.in_channel_of_descr socket
  ; out_channel = Unix.out_channel_of_descr socket
  } ;;
let connections = Array.init game.g_nb_players connect_client ;;

(* Envoi de la configuration a tous les joueurs, sans passer par Mailbox
   pour etre sur que ces messages partent en premier (sinon ils partiront apres
   les messages lies a la visibilite de la premiere ville). *)
let rec send_config i =
  if i < game.g_nb_players then begin
      output_string connections.(i).out_channel (Printf.sprintf "width %d\n" game.g_width) ;
      output_string connections.(i).out_channel (Printf.sprintf "height %d\n" game.g_height) ;
      output_string connections.(i).out_channel (Printf.sprintf "player_id %d\n" i) ;
      output_string connections.(i).out_channel (Printf.sprintf "piece_types %s\n" (info_get_info_piece_types game)) ;
      flush connections.(i).out_channel ;
      send_config (i + 1)
    end ;;

send_config 0 ;;

let handle_request game i message =
  let tokens = split message ' ' in
  assert (List.length tokens > 0) ;
  let post response = post_message game (i, response) in
  try
    begin
      match List.hd tokens with
      | "end_game" -> game.g_end <- true
      | "end_turn" -> turn_end_turn game
      | "dump_map" -> turn_dump_map game
      | "moves" ->
          let piece_id = int_of_string (List.nth tokens 1) in
          let q = int_of_string (List.nth tokens 2) in
          let r = int_of_string (List.nth tokens 3) in
          turn_moves game piece_id q r
      | "move" ->
          let piece_id = int_of_string (List.nth tokens 1) in
          let direction_id = int_of_string (List.nth tokens 2) in
          turn_move game piece_id direction_id
      | "set_city_production" ->
          let city_id = int_of_string (List.nth tokens 1) in
          let piece_type_id = int_of_string (List.nth tokens 2) in
          turn_set_city_production game city_id piece_type_id
      (* Requetes dont le traitement peut etre realise directement. Il ne
         necessite pas de tests particuliers. *)
      | "get_width" -> post (string_of_int game.g_width)
      | "get_height" -> post (string_of_int game.g_height)
      | "get_piece_types_names" ->
          let walk piece_type_id piece_type aux =
            (string_of_int piece_type_id ^ ":" ^ piece_type.a_name) :: aux in
          post (String.concat "," (Hashtbl.fold walk game.g_piece_types []))
      (* Requetes dont le traitement demande des tests sur ce que le joueur
         peut demander. *)
      | "can_move" ->
          let piece_id = int_of_string (List.nth tokens 1) in
          let direction_id = int_of_string (List.nth tokens 2) in
          post (string_of_bool (info_can_move game piece_id direction_id))
      | "can_enter" ->
          let piece_id = int_of_string (List.nth tokens 1) in
          let direction_id = int_of_string (List.nth tokens 2) in
          post (string_of_bool (info_can_enter game piece_id direction_id))
      | "can_attack" ->
          let piece_id = int_of_string (List.nth tokens 1) in
          let direction_id = int_of_string (List.nth tokens 2) in
          post (string_of_bool (info_can_attack game piece_id direction_id))
      | "get_piece_id_by_loc" ->
          let q = int_of_string (List.nth tokens 1) in
          let r = int_of_string (List.nth tokens 2) in
          begin match info_get_piece_id_by_loc game q r with
          | Some i -> post (string_of_int i)
          | None -> post "none"
          end
      | "get_transported_names_by_loc" ->
          let q = int_of_string (List.nth tokens 1) in
          let r = int_of_string (List.nth tokens 2) in
          let walk piece_id =
            let piece = Hashtbl.find game.g_pieces piece_id in
            let piece_type = Hashtbl.find game.g_piece_types piece.p_type in
            string_of_int piece_id ^ ":" ^ piece_type.a_name in
          let pieces = info_get_transported_pieces_by_loc game q r in
          post (String.concat "," (List.map walk pieces))
      | "get_info_city" ->
          let city_id = int_of_string (List.nth tokens 1) in
          post (info_get_info_city game city_id)
      | "get_info_piece" ->
          let piece_id = int_of_string (List.nth tokens 1) in
          post (info_get_info_piece game piece_id)
      | "get_city_production" ->
          let city_id = int_of_string (List.nth tokens 1) in
          begin match info_get_city_production game city_id with
          | Some (a, b, c) ->
              post (String.concat ":" (List.map string_of_int [a; b; c]))
          | None -> post "none"
          end
      | "get_list_cities" ->
          let f (a, b, c) = String.concat ":" (List.map string_of_int [a; b; c]) in
          post (String.concat "," (List.map f (info_get_list_cities game)))
      | "get_list_pieces" ->
          let f (a, b, c) = String.concat ":" (List.map string_of_int [a; b; c]) in
          post (String.concat "," (List.map f (info_get_list_pieces game)))
      | "get_list_movables" ->
          let f (a, b, c) = String.concat ":" (List.map string_of_int [a; b; c]) in
          post (String.concat "," (List.map f (info_get_list_movables game)))
      | "get_city_id_by_loc" ->
          let q = int_of_string (List.nth tokens 1) in
          let r = int_of_string (List.nth tokens 2) in
          begin match info_get_city_id_by_loc game q r with
          | Some i -> post (string_of_int i)
          | None -> post "none"
          end
      | _ -> post ("error \"invalid message: " ^ message ^ "\"")
    end
  with
  | ActionError message -> post ("error \"" ^ message ^ "\"") ;;

let rec handle_mailbox game connections =
  if have_message game then begin
      let player_id, message = read_message game in
      print_endline (Printf.sprintf "snd: %d <- %s" player_id message) ;
      output_string connections.(player_id).out_channel (message ^ "\n") ;
      handle_mailbox game connections
    end ;
  Array.iter (fun connection -> flush connection.out_channel) connections ;;

let rec handle_requests game connections =
  (* Demande d'action au joueur suivant. *)
  post_message game (game.g_turn, "get_action") ;
  (* Envoi des mails. *)
  handle_mailbox game connections ;
  (* Lecture des donnees du joueur et traitement. *)
  let message = read_client connections.(game.g_turn) in
  print_endline (Printf.sprintf "rcv: %d -> %s" game.g_turn message) ;
  handle_request game game.g_turn message ;

  (* Test de la fin de partie et rebouclage si on continue. *)
  let survivors =
    let get_survivors survivors player =
      if (Misc.Set.empty player.player_pieces) && (Misc.Set.empty player.player_cities)
      then survivors
      else player :: survivors in
    Array.fold_left get_survivors [] game.g_players in
  if List.length survivors = 0 then begin
    Array.iteri (fun i _ -> post_message game (i, "draw")) game.g_players ;
    handle_mailbox game connections
  end else if (List.length survivors) = 1 then begin
    let message = Printf.sprintf "winner %d" (List.hd survivors).player_id in
    Array.iteri (fun i _ -> post_message game (i, message)) game.g_players ;
    handle_mailbox game connections ;
  end else if game.g_end = false then
    handle_requests game connections
  ;;

handle_requests game connections ;;
Array.iter (fun x -> close x.socket) connections ;;
