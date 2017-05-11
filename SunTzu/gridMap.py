# Generated code -- http://www.redblobgames.com/grids/hexagons/
# SEE http://www.redblobgames.com/grids/hexagons/implementation.html



from __future__ import division
from __future__ import print_function

import collections
import math



Point = collections.namedtuple("Point", ["x", "y"])
Hex = collections.namedtuple("Hex", ["q", "r", "s"])


class Tile:


class Map:



def hex_add(a, b):
    return Hex(a.q + b.q, a.r + b.r, a.s + b.s)

def hex_subtract(a, b):
    return Hex(a.q - b.q, a.r - b.r, a.s - b.s)

def hex_scale(a, k):
    return Hex(a.q * k, a.r * k, a.s * k)

hex_directions = [Hex(1, 0, -1), Hex(1, -1, 0), Hex(0, -1, 1), Hex(-1, 0, 1), Hex(-1, 1, 0), Hex(0, 1, -1)]
def hex_direction(direction):
    return hex_directions[direction]

def hex_neighbor(hex, direction):
    return hex_add(hex, hex_direction(direction))

hex_diagonals = [Hex(2, -1, -1), Hex(1, -2, 1), Hex(-1, -1, 2), Hex(-2, 1, 1), Hex(-1, 2, -1), Hex(1, 1, -2)]
def hex_diagonal_neighbor(hex, direction):
    return hex_add(hex, hex_diagonals[direction])

def hex_length(hex):
    return (abs(hex.q) + abs(hex.r) + abs(hex.s)) // 2

def hex_distance(a, b):
    return hex_length(hex_subtract(a, b))

def hex_round(h):
    q = int(round(h.q))
    r = int(round(h.r))
    s = int(round(h.s))
    q_diff = abs(q - h.q)
    r_diff = abs(r - h.r)
    s_diff = abs(s - h.s)
    if q_diff > r_diff and q_diff > s_diff:
        q = -r - s
    else:
        if r_diff > s_diff:
            r = -q - s
        else:
            s = -q - r
    return Hex(q, r, s)

def hex_lerp(a, b, t):
    return Hex(a.q * (1 - t) + b.q * t, a.r * (1 - t) + b.r * t, a.s * (1 - t) + b.s * t)

def hex_linedraw(a, b):
    N = hex_distance(a, b)
    a_nudge = Hex(a.q + 0.000001, a.r + 0.000001, a.s - 0.000002)
    b_nudge = Hex(b.q + 0.000001, b.r + 0.000001, b.s - 0.000002)
    results = []
    step = 1.0 / max(N, 1)
    for i in range(0, N + 1):
        results.append(hex_round(hex_lerp(a_nudge, b_nudge, step * i)))
    return results


def enum(**enums):
    return type('Enum', (), enums)

Terrain =enum(WATER='1', GROUND='2')

piece_id=int

piece_type_id = int

city_id=int

player_id =int


class Tile:
	def __init__(self, terrain, location):
		self.terrain = terrain	# If None: unexplored.
		self.content = None
		self.visible = False
		self.location = location
		self.parent = None
	def get_location(self):
		return self.location
	def is_city(self):
		return False
	def is_owned_city(self):
		return False

class Piece:
	# States used for transporters.
	TRAVEL_TAKE=0
	TRAVEL_LAND=1
	TAKE=2
	LAND=3
	def __init__(self, piece_id, piece_type_id, owner, piece_hits):
		self.piece_hits = piece_hits
		self.piece_id = piece_id
		self.piece_type_id = piece_type_id
		self.owner = owner
		# TODO: interet ????
		#######self.content = []
		self.transport = []
		self.parent = None
		# Following attributes are not used by situation but
		# they are used by other classes.
		self.behavior = None
		self.steps_left = None
		self.path = None
		self.destination = None
		self.role = None
	def get_location(self):
		return self.parent.get_location()
	def is_piece(self):
		return True
	def is_city(self):
		return False
	def is_owned_city(self):
		return False


class OwnedCity:
	def __init__(self, city_id, parent, owner):
		self.city_id = city_id
		self.owner = owner
		self.parent = parent
		self.production = None
		self.content = []
	def get_location(self):
		return self.parent.get_location()
	def is_piece(self):
		return False
	def is_city(self):
		return True
	def is_owned_city(self):
		return True

class City:
	def __init__(self, city_id, parent):
		self.city_id = city_id
		self.parent = parent
	def get_location(self):
		return self.parent.get_location()
	def is_piece(self):
		return False
	def is_city(self):
		return True
	def is_owned_city(self):
		return False

class PieceType:
	def __init__(self, dictionary):
		for k, v in dictionary.items():
			setattr(self, k, v)


type tile =
  | Unknown
  | Explored of terrain
  (* (Nombre d'item qui ont une visibilite sur le carreau, terrain, contenu) *)
  | Visible of int * terrain * (item option)
  ;;

type player =
  { player_id : player_id
  ; player_view : tile array array
  ; player_pieces : piece_id Misc.Set.t
  ; player_cities : city_id Misc.Set.t
  } ;;

type game =
  { g_width : int
  ; g_height : int
  ; g_nb_players : int
  ; g_map : terrain array array
  ; g_map_items : item option array array
  ; g_cities : (city_id, city) Hashtbl.t
  ; g_pieces : (piece_id, piece) Hashtbl.t
  ; g_piece_types : (piece_type_id, piece_type) Hashtbl.t
  ; g_players : player array
  ; mutable g_round : int
  ; mutable g_turn : int (* Joueur qui a le jeton. *)
  ; mutable g_counter : int (* Pour la creation de nouveaux id. *)
  ; g_mailbox : (int * string) Queue.t (* (Jouer, message) *)
  ; mutable g_end : bool (* Indicateur de fin de partie. *)
  } ;;

