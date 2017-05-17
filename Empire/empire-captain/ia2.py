#!/usr/bin/python2.7
import os
import socket
import sys

import communication
import parser2
import tools


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

the_parser = parser2.Parser() # TODO: implement parser2 
the_communication = communication.Communication(the_parser, server, server_fd)


maps = [ {} , {} ]  # TODO choix de la map

turn = 0
while 1:
	turn = turn + 1
	the_communication.wait()

	tools.debug("turn: %d" %  turn)
	if do_debug: the_communication.action("dump_map")

	# 1. Process cities.
	for city in listcity #TODO list city à créer
		if city.production is not None:	# si la ville produit déjà quelque chose
			continue # on fait un break et on ne choisit pas 
		
		


	# 2. Process pieces.




	# 3. End turn.
	the_communication.end_turn()
