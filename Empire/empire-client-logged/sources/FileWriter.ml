open Empire;;


let client_log="";;

let player_id =ref (-1) ;;

let update_player_id id=
   player_id := id ;;


let save file string =
    let channel = open_out file in
    output_string channel string;
    close_out channel;;

let appendToFile str file =
  	let oc =
  	open_out_gen
  	[Open_wronly; Open_creat; Open_append; Open_text] 0o666 file in
  	output_string oc str;
  	close_out oc;;

let appendToFileWithPlayerId str file =
  appendToFile ((Printf.sprintf "rcv: %d -> %s" !player_id str) ^ "\n") (Printf.sprintf "client%d_log.txt" !player_id);;


save (Printf.sprintf "client0_log.txt" ) client_log;;
save (Printf.sprintf "client1_log.txt" ) client_log;;
