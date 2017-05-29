import tools


class Communication:

	def __init__(self, parser, server, server_fd):
		self.parser = parser
		self.server_fd = server_fd
		self.server = server
		self.player_turn = False

	def info(self, message):
		assert self.player_turn
		self.server.send(message + "\n")
		response = self.server_fd.readline().strip()
		message_get_action = self.server_fd.readline().strip()
		assert message_get_action == "get_action"
		return response

	def action(self, message):
		assert self.player_turn
		assert message != "end_turn"
		self.server.send(message + "\n")
		response = self.server_fd.readline().strip()
		err=0
		while response != "get_action":
			valid=self.parser.parse(response)
			if valid==-1:
				err=-1
			response = self.server_fd.readline().strip()
		return err

	def end_turn(self):
		assert self.player_turn
		self.server.send("end_turn\n")
		self.player_turn = False

	def wait(self):
		assert not self.player_turn
		response = self.server_fd.readline().strip()
		while response != "get_action": #Tant que l'on ne demande pas au joueur de jouer
			valid=self.parser.parse(response)
			if valid==-1:
				print "Erreur wait %s" % response 
			response = self.server_fd.readline().strip()
		self.player_turn = True
