#!/usr/bin/python2.7

import os
import sys
import socket
import select

if len(sys.argv) != 5:
	print >> sys.stderr, "usage: %s <server-name> <server-port> <player-port> <observer-port>" % sys.argv[0]
	print >> sys.stderr, "\n"
	print >> sys.stderr, "This program waits for a connection on <observer-port> (for the observer) and"
	print >> sys.stderr, "on <player-port> (for the player). Then, it connects to the server and"
	print >> sys.stderr, "passes messages of the server to both the player and the observer. Messages"
	print >> sys.stderr, "from the player are sent to the server and messages from the observer are"
	print >> sys.stderr, "ignored"
	print >> sys.stderr, "\n"
	sys.exit(1)

server_name = sys.argv[1]
server_port = int(sys.argv[2])
player_port = int(sys.argv[3])
observer_port = int(sys.argv[4])

# Create sockets fot the observer and the player.
observer_srv = socket.socket()
observer_srv.bind(('localhost', observer_port))
observer_srv.listen(1)
player_srv = socket.socket()
player_srv.bind(('localhost', player_port))
player_srv.listen(1)

# Wait for the observer then the player.
observer, observer_addr = observer_srv.accept()
player, player_addr = player_srv.accept()

# Connect to the server.
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#server.settimeout(2)
try:
	server.connect((server_name, server_port))
except:
	print "unable to connect"
	sys.exit(1)

connections = [server, player]
recv_length = 4096

try:
	while 1:
		read_sockets, write_sockets, error_sockets = select.select(connections, [], [])
		for sock in read_sockets:
			if sock == player:
				data = player.recv(recv_length)
				#print "P>S   %s" % data
				server.send(data)
			elif sock == server:
				data = server.recv(recv_length)
				#print "S>P&O %s" % data
				player.send(data)
				observer.send(data)
except Exception as e:
	print >> sys.stderr, "Error: %s" % str(e)

try:
	server.close()
except:
	pass

try:
	player.close()
except:
	pass

try:
	observer.close()
except:
	pass
