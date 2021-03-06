#!/usr/bin/python2.7
# coding=utf-8
import os
import socket
import sys
import random
import time

from packageSunTzu import communication
from packageSunTzu import parser
from packageSunTzu import game_map
from packageSunTzu import game_status
from packageSunTzu import cities
from packageSunTzu import units
from packageSunTzu import play as SunTzu
#from packageSunTzu import trainPlay as SunTzu

def ASK_SUNTZU(typeid,minimap,far_context,even_further_context):
	return SunTzu.jouer(minimap,typeid,far_context,even_further_context)

def ASK_RANDOM(typeid):
	if typeid=="city":
		return random.randint(0,1)
	else:
		return random.randint(0,5)

def test_move(typeid,center,direction):
	val=-1
	x,y=center
	(dx,dy)= the_map.directions[direction]
	if (x+dx,y+dy) in the_map.get_map().keys():
		dest = the_map.get_map()[(x+dx,y+dy)]
		if dest in the_types_of_units.get_piecetype(typeid).get_terrain().keys():
			val=0
		if typeid==0 and (dest in the_types_of_units.get_ennemy_units() or dest == 'c'):
			val =0

	return val

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
the_parser = parser.Parser(the_game_status,the_map,the_cities,the_units,the_types_of_units)
the_communication = communication.Communication(the_parser, server, server_fd)
#the_SunTzu=SunTzu.SunTzu()

turn = 0
while 1:
	turn = turn + 1
	the_communication.wait()
	print "==================="
	print "turn %d " % turn

	# 1. Gestion des villes.
	print "cities : ",
	print the_cities.get_cities().keys()
	for cityid in the_cities.get_cities().keys():
		city=the_cities.get_city(cityid)
		if city is None :
			continue
		if city.get_production() is not None:	# si la ville produit déjà quelque chose
			continue # on fait un break et on ne choisit pas

		(x,y)=city.get_pos()
		minimap=the_map.get_centered_map(x,y)
		far_context= the_map.get_far_context(x,y)
		even_further_context= the_map.get_even_further_context(x,y)
		cityproduction=1#ASK_SUNTZU(-1,minimap,far_context,even_further_context)[0]
		print "cityprod : ",
		print cityproduction
		city.set_production(cityproduction)
		city_id=city.get_cityid()
		print "set_city_production %d %d" % (city_id, cityproduction)
		valid=the_communication.action("set_city_production %d %d" % (city_id, cityproduction))#TODO rajouter un if valid car sinon ça ne produit plus
		if valid==-1:
			print "Erreur Envoi message production"

	# 2. Gestion des pieces.
	print "units : ",
	print the_units.get_pieces().keys()

	for pieceid in the_units.get_pieces().keys():
		piece=the_units.get_piece(pieceid)
		if piece is None : #cette condition montre que certaines pièces ne sont pas supprimées
			continue
		piecetypeid=piece.get_piecetypeid()
		nbmove=the_types_of_units.get_piecetype(piecetypeid).get_move()
		while(nbmove!=0 and pieceid in the_units.get_pieces().keys()):
			time.sleep(0.5)
			valid=-1
			# while (valid==-1 ):
			(x, y) = piece.get_position()
			minimap = the_map.get_centered_map(x,y)
			far_context= the_map.get_far_context(x,y)
			even_further_context= the_map.get_even_further_context(x,y)
			piecemove=ASK_SUNTZU(piecetypeid,minimap,far_context,even_further_context)[0]
			print "move %d %d" % (pieceid,piecemove),
			valid= test_move(piecetypeid,(x,y),piecemove)
			if valid!=-1:
				print "envoyé"
				valid2=the_communication.action("move %d %d" % (pieceid,piecemove))
			else:
				print "INVALID"
						# TODO, réduire le choix d'actions jusqu'à ce qu'il ny ait plus de possibités
			nbmove=nbmove-1

	# 3.Envoi de End turn.
	the_communication.end_turn()
