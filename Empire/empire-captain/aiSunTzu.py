#!/usr/bin/python2.7
# coding=utf-8
import os
import socket
import sys

from packageSunTzu import communication
from packageSunTzu import parser
from packageSunTzu import tools
from packageSunTzu import game_map
from packageSunTzu import game_status
from packageSunTzu import cities
from packageSunTzu import units

def ASK_SUNTZU(): #TODO ATTENTION A CE TURC QUI TRAINE
	return 1


do_debug = False

if len(sys.argv) != 3:
	print >> sys.stderr, "usage: %s <server-name> <server-port>" % sys.argv[0]
	print >> sys.stderr, "\n"
	sys.exit(1)

server_name = sys.argv[1]
server_port = int(sys.argv[2])

# Connect to the server.
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
	server.connect((server_name, server_port))
except:
	print "unable to connect"
	sys.exit(1)

server_fd = server.makefile()

the_game_status=game_status.Game_status()
the_map=game_map.Map()
the_cities=cities.Citieslist()
the_units=units.Pieceslist()
the_types_of_units=units.Piecestypeslist()
the_parser = parser.Parser(the_game_status,the_map,the_units)
the_communication = communication.Communication(the_parser, server, server_fd)

turn = 0
while 1:
	turn = turn + 1
	the_communication.wait()

	tools.debug("turn: %d" %  turn)
	if do_debug: the_communication.action("dump_map")

	# 1. Process cities.
	for city in the_cities.get_cities():
		if city.production is not None:	# si la ville produit déjà quelque chose
			continue # on fait un break et on ne choisit pas

		(x,y)=city.get_pos()
		minimap=the_map.get_centered_map(x,y)
		cityproduction=ASK_SUNTZU(minimap)
		city.set_production(cityproduction)
		city_id=city.get_cityid()
		the_communication.action("set_city_production %d %d" % (city_id, city.production))

	# 2. Process pieces.
	for piece in the_units.get_pieces():
		pieceid=piece.get_pieceid()
		piecetype=piece.get_piecetype()
		nbmove=the_types_of_units.get_move(piecetype)
		while(nbmove!=0):
			(x, y) = piece.get_pos()
			minimap = the_map.get_centered_map(x,y)
			piecemove=ASK_SUNTZU(minimap)
			the_communication.action("move %d %d" % (pieceid,piecemove))
			nbmove=nbmove-1

	# 3. End turn.
	the_communication.end_turn()

