import re
import sys

from game_map import *
from units import *
from cities import *
from game_status import *

class Parser:
	def __init__(self, the_game_status,the_map,the_cities,the_units,the_types_of_units):
		self.the_map = the_map
		self.the_game_status=the_game_status
		self.the_map=the_map
		self.the_cities=the_cities
		self.the_units=the_units
		self.the_types_of_units= the_types_of_units
		self.re_transport_in_city = re.compile(r"transport in-city (\d+) (\d+)")

		# The order matters: it must be the same of both rexes and handlers (see parse method).
		self.rexes =	[ re.compile(r"set_visible (\d+) (\d+) (\w+) none")
				, re.compile(r"set_visible (\d+) (\d+) (\w+) owned_city (\d+) (\d+)")
				, re.compile(r"set_visible (\d+) (\d+) (\w+) city (\d+)")
				, re.compile(r"set_visible (\d+) (\d+) (\w+) piece (\d+) (\d+) (\d+) (\d+)")
				, re.compile(r"set_explored (\d+) (\d+) (\w+)")
				, re.compile(r"width (\d+)")
				, re.compile(r"height (\d+)")
				, re.compile(r"piece_types (.*)")
				, re.compile(r"player_id (\d+)")
				, re.compile(r"create_piece (\d+) (\d+) (\d+) (\d+)")
				, re.compile(r"delete_piece (\d+)")
				, re.compile(r"enter_city (\d+) (\d+)")
				, re.compile(r"enter_piece (\d+) (\d+)")
				, re.compile(r"leave_piece (\d+) (\d+)")
				, re.compile(r"leave_city (\d+) (\d+)")
				, re.compile(r"leave_terrain (\d+) (\d+) (\d+)")
				, re.compile(r"move (\d+) (\d+) (\d+)")
				, re.compile(r"invade_city (\d+) (\d+) (\d+)")
				, re.compile(r"lose_city (\d+)")
				, re.compile(r"winner (\d+)")
				, re.compile(r"random_seed (\d+)")
				, re.compile(r"ko-invasion (\d+) (\d+) (\d+)")
				, re.compile(r"ok-invasion (\d+) (\d+) (\d+)")
				, re.compile(r"created-units-limit (\d+)")
				, re.compile(r"city-units-limit (\d+)")
				]
		self.proxy_handlers =	[ self.parse_set_visible_none
				, self.parse_set_visible_owned_city
				, self.parse_set_visible_city
				, self.parse_set_visible_piece
				, self.parse_set_explored
				, self.parse_width
				, self.parse_height
				, self.parse_piece_types
				, self.parse_player_id
				, self.parse_create_piece
				, self.parse_delete_piece
				, self.parse_enter_city
				, self.parse_enter_piece
				, self.parse_leave_piece
				, self.parse_leave_city
				, self.parse_leave_terrain
				, self.parse_move
				, self.parse_invade_city
				, self.parse_lose_city
				, self.parse_winner
				, self.parse_random_seed
				, self.parse_ko_invasion
				, self.parse_ok_invasion
				, self.parse_created_units_limit
				, self.parse_city_units_limit
				]

	def kronecker_inv(self,x,y):
		if x==y :
			return 0
		else :
			return 1

	def parse_set_visible_none(self, groups):
		(x,y) = int(groups.group(1)), int(groups.group(2))
		terrain =  groups.group(3)
		if terrain == "water":
			self.the_map.update_map(x,y,'A')
		else:
			self.the_map.update_map(x,y,'B')

	def parse_set_visible_owned_city(self, groups):
		(x,y) = int(groups.group(1)), int(groups.group(2))
		city_id = int(groups.group(4))
		city_owner = int(groups.group(5))
		if self.the_game_status.get_player_id() is None : # La premiere ville decouverte est celle du joueur
			self.the_game_status.set_player_id(city_owner)
		if city_owner==self.the_game_status.get_player_id():
			self.the_cities.add(city_id,City(city_id,x,y))
		self.the_map.update_map(x,y,chr(ord('C') + self.kronecker_inv(city_owner,self.the_game_status.player_id)))


	def parse_set_visible_city(self, groups):
		(x,y) = int(groups.group(1)), int(groups.group(2))
		city_id = int(groups.group(4))
		self.the_map.update_map(x,y,'c')


	def parse_set_visible_piece(self, groups):
		(x,y) = int(groups.group(1)), int(groups.group(2))
		piece_owner = int(groups.group(4))
		piece_type_id = int(groups.group(6))
		self.the_map.update_map(x,y, chr(ord('M') +piece_type_id +
										  self.the_types_of_units.get_nbpiecetype()*self.kronecker_inv(piece_owner,self.the_game_status.player_id)))

	def parse_set_explored(self, groups):
		(x,y) = int(groups.group(1)), int(groups.group(2))
		terrain = groups.group(3)
		if terrain == "water":
			self.the_map.update_map(x,y,'a')
		else:
			self.the_map.update_map(x,y,'b')

	def parse_width(self, groups):
		self.the_map.set_width(int(groups.group(1)))

	def parse_height(self, groups):
		self.the_map.set_height(int(groups.group(1)))


		#le programme split ignore les messages dans ces cas la :
		# if fields[0] in ["city-units-limit", "created-units-limit", "create_piece", \
		# 		 "delete_piece", "enter_city", "get_action", "ko-invasion", \
		# 		 "leave_city", "leave_terrain", "lose_city", "ok-invasion", \
		# 		 "winner", "move", "enter_piece", "leave_piece"]:

	def parse_leave_city(self, groups):
		pass

	def parse_enter_city(self, groups):
		pass

	def parse_enter_piece(self, groups):
		pass

	def parse_leave_piece(self, groups):
		pass

	def parse_leave_terrain(self, groups):
		pass

	def parse_player_id(self, groups):
		self.the_game_status.set_player_id(int(groups.group(1)))

	def parse_piece_types(self, groups): # ce type de message n'est jamais recu a priori
		pass
		# piece_types = groups.group(1).split(";")
		# piece_types = [x.split("#") for x in piece_types]
		# result = {}
		# terrain = {"water": self.the_situation.WATER, "ground": self.the_situation.GROUND}
		# for piece_type in piece_types:
		# 	info = {}
		# 	info["piece_type_id"] = int(piece_type[0])
		# 	info["name"] = piece_type[1]
		# 	info["symbol"] = piece_type[2]
		# 	info["terrains"] = [terrain[x] for x in piece_type[3].split(":")]
		# 	info["build_time"] = int(piece_type[4])
		# 	info["max_hits"] = int(piece_type[6])
		# 	info["speed"] = int(piece_type[7])
		# 	info["capacity"] = int(piece_type[8])
		# 	info["autonomy"] = None if piece_type[9] == "" else int(piece_type[9])
		# 	info["transportable"] = [] if piece_type[10] == "" else [int(x) for x in piece_type[10].split(":")]
		# 	info["visibility"] = int(piece_type[11])
		# 	info["can_invade"] = piece_type[12] in ["true", "True"]
		# 	result[info["piece_type_id"]] = situation.PieceType(info)
		# self.the_situation.set_piece_types(result)
		# for handler in self.handlers:
		# 	handler.set_piece_types(result)

	def parse_create_piece(self, groups):
		piece_id = int(groups.group(1))
		piece_type_id = int(groups.group(2))
		city_id = int(groups.group(3))
		self.the_cities.get_city(city_id).set_production(None)
		(x,y) = self.the_cities.get_city(city_id).get_pos()
		self.the_units.add(piece_id,Piece(piece_id,piece_type_id,x,y))


	def parse_delete_piece(self, groups): # pas besoin de mettre a jour la map delete_piece est suivi de set_visible
										  # mis a part si la piece est dans une ville
		piece_id = int(groups.group(1))
		self.the_units.remove(piece_id)
		print "delete_piece : %d" % piece_id


	def parse_move(self, groups):
		piece_id = int(groups.group(1))
		(x,y) = int(groups.group(2)), int(groups.group(3))
		self.the_units.get_piece(piece_id).set_position(x,y)

	def parse_invade_city(self, groups):
		city_id = int(groups.group(1))
		(x,y) = int(groups.group(2)), int(groups.group(3))
		self.the_cities.add(city_id,City(city_id, x,y))

	def parse_lose_city(self, groups):
		city_id = int(groups.group(1))
		location=self.the_cities.get_city(city_id).get_pos() # Pas sur d'en avoir besoin
		for pieceid in self.the_units.get_pieces().keys(): # on supprime les unites contenues dans la ville
			piece=self.the_units.get_piece(pieceid)
			if location==piece.get_position():
				self.the_units.remove(pieceid)

		self.the_cities.remove(city_id)


	def parse_winner(self, groups): # je pense qu'on ne passse jamais ici car methode end de situation n'existe pas
		if int(groups.group(1)) == self.the_game_status.get_player_id():
			print "Winner is you"
		else:
			print "Winner is the enemy"
		#self.the_situation.end()
		sys.exit(0)

	def parse_ok_invasion(self, groups):
		pass

	def parse_ko_invasion(self, groups):
		pass

	def parse_random_seed(self, groups):
		pass

	def parse_created_units_limit(self, groups):
		pass

	def parse_city_units_limit(self, groups):
		pass

	def parse(self, message):
		for i in range(len(self.rexes)):
			groups = self.rexes[i].match(message)
			if groups:
				self.proxy_handlers[i](groups)
				return i
		print message
		return -1 # dans le cas ou un message n'est pas handled
				# TODO, mettre des cas differents en fonction du message
		#self.the_situation.show()
		#raise Exception("error: not handled: " + message)
