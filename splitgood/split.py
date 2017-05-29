import sys

# output = "txt"
output = "py"

nb_piece_type = 10 # TODO: modifier automatiquement!
width = 44	 # TODO: modifier automatiquement!
height = 24	# TODO: modifier automatiquement!
half_size = 3
filename = "player1"

maps = [ {} , {} ]

lines = open(filename, "r").readlines()

# http://www.redblobgames.com/grids/hexagons/
# var results = []
# for each -N <= dx <= N:
#     for each max(-N, -dx-N) <= dy <= min(N, -dx+N):
#	 var dz = -dx-dy
#	 results.append(cube_add(center, Cube(dx, dy, dz)))


#XXX: nous sommmes dans une config pointy-top

#direction =(q,r)=(x,y,z)=(r,-q-r,q)   : r=z axe horizontal, q=x axe diagonal Nord Ouest vers Sud-Est
directions = [ (+1,  0), (+1, -1), ( 0, -1), (-1,  0), (-1, +1), ( 0, +1) ]
			 #			#

allied_units=['C','M','N','O','P','Q']
ennemy_units=['D','W','X','Y','Z']


def cube_ring(center, radius):
	if radius == 0:
		return [center]
	q, r = center
	results = []
	for i in range(len(directions)):
		qa, ra = directions[i]
		qb, rb = directions[(i + 1) % len(directions)]
		qd, rd = qb - qa, rb - ra
		if qd != 0:
			qd = qd / abs(qd)
		if rd != 0:
			rd = rd / abs(rd)
		for j in range(radius):
			results.append((q + radius * qa + j * qd, r + radius * ra + j * rd))
	return results

def print_centered_map_txt(x, y, player):
	pmaps = maps[player]

	tiles = []
	for r in range(half_size + 1):
		tiles.extend(cube_ring((x, y), r))

	for py in range(y - half_size, y + half_size + 1):
		for px in range(x - half_size, x + half_size + 1):
			if (px, py) in tiles:
				if px < 0 or px >= width or py < 0 or py >= height:
					print "!",
				elif (px, py) in pmaps:
					print pmaps[(px, py)],
				else:
					print "?",
			else:
					print "#",
		print ""

def print_far_context_txt(x,y,player):
	pass #TODO

def print_even_further_context_txt(x,y,player):
	pass #TODO

def print_move_txt(direction, piece_type):
	print "move %d %d" % (direction, piece_type)

def print_set_city_production_txt(piece_type):
	print "set_city_production %d" % piece_type

def print_centered_map_py(x, y, player):
	global nb_print_centered_map
	pmaps = maps[player]

	tiles = []
	for r in range(half_size + 1):
		tiles.extend(cube_ring((x, y), r))

	print "map_%d = \"" % nb_print_centered_map,
	for py in range(y - half_size, y + half_size + 1):
		for px in range(x - half_size, x + half_size + 1):
			if (px, py) in tiles:
				if px < 0 or px >= width or py < 0 or py >= height:
					print "!",
				elif (px, py) in pmaps:
					print "%c" % pmaps[(px, py)],
				else:
					print "?",
	print "\""
	nb_print_centered_map = nb_print_centered_map + 1

def print_move_py(direction, piece_type):
	print "decision_%d = %d" % (nb_print_centered_map, direction)
	print "decision_piece_type_%d = %d" % (nb_print_centered_map, piece_type)
	print "decision_type_%d = 0" % nb_print_centered_map

def print_set_city_production_py(piece_type):
	print "decision_%d = %d" % (nb_print_centered_map, piece_type)
	print "decision_piece_type_%d = -1" % nb_print_centered_map
	print "decision_type_%d = 1" % nb_print_centered_map


def print_all_map(player):
	pmaps = maps[player]
	for py in range(height):
		for px in range(width):
			if px < 0 or px >= width or py < 0 or py >= height:
				print '!',
			elif (px, py) in pmaps:
				print pmaps[(px, py)],
			else:
				print "?",
		print ""

def print_even_further_context_py(x,y,player):
	print "even_further_context_%d= \" " % nb_print_centered_map,
	for (xp,yp) in mirror_centers((x,y),2*half_size):
		print "%d " % interest(get_centered_map(xp,yp,player)),
	print "\""

def print_far_context_py(x,y,player):
	print "far_context_%d = \" " % nb_print_centered_map,
	for (xp,yp) in mirror_centers((x,y),half_size):
		print "%d " % interest(get_centered_map(xp,yp,player)),
	print "\""


def print_enhanced_centered_map(x,y,player):
	print_far_context(x,y,player)
	print_centered_map(x,y,player)


def get_centered_map(x, y,player):
	tiles = []
	minimap=[]
	pmaps = maps[player]

	for r in range(half_size + 1):
		tiles.extend(cube_ring((x, y), r))

	for py in range(y - half_size, y + half_size + 1):
		for px in range(x - half_size, x + half_size + 1):
			if (px, py) in tiles:
				if px < 0 or px >= width or py < 0 or py >= height:
					minimap.append('!')
				elif (px, py) in pmaps:
					minimap.append(pmaps[(px, py)])
				else:
					minimap.append('?')
	return minimap


def rotate(l, n):
    newl= [-e for e in l]
    return newl[-n:] + newl[:-n]

def mirror_centers(center, radius):
    x,y=center
    list_centers=[]
    mirror_center=[2*radius+1, -radius, -radius-1]
    offset_mirror_center= [x+mirror_center[0],y+mirror_center[1]]
    list_centers.append(offset_mirror_center)
    for i in range(5):
        mirror_center=rotate(mirror_center,1)
        offset_mirror_center= [x+mirror_center[0],y+mirror_center[1]]
        list_centers.append(offset_mirror_center)
    return list_centers


def interest(minimap):
	blood_to_spill=0
	for symb in minimap :
		if symb  in ennemy_units:
			if symb == 'D' :
				blood_to_spill=blood_to_spill+10
			else :
				blood_to_spill=blood_to_spill+2
			if symb == 'M':
				blood_to_spill=blood_to_spill+1
	return blood_to_spill

def kronecker_inv(x,y):
	if x==y :
		return 0
	else :
		return 1


if output == "txt":
	print_move = print_move_txt
	print_set_city_production = print_set_city_production_txt
	print_centered_map = print_centered_map_txt
	print_far_context = print_far_context_txt
	print_even_further_context=print_even_further_context_txt
elif output == "py":
	nb_print_centered_map = 0
	print_move = print_move_py
	print_set_city_production = print_set_city_production_py
	print_far_context=print_far_context_py
	print_centered_map = print_centered_map_py
	print_even_further_context=print_even_further_context_py
else:
	print "invalid output: " + output
	sys.exit(2)

for line in lines:
	line = line.strip()
	if line.startswith("snd:"):
		fields = line[len("snd: "):]
		fields = line[5:]
		player = int(fields[0])
		fields = fields[5:].split(" ")

		if fields[0] in ["city-units-limit", "created-units-limit", "create_piece", \
				 "delete_piece", "enter_city", "get_action", "ko-invasion", \
				 "leave_city", "leave_terrain", "lose_city", "ok-invasion", \
				 "winner", "move", "enter_piece", "leave_piece"]:
			pass
		elif fields[0] == "set_visible":
			x = int(fields[1])
			y = int(fields[2])

			terrain = fields[3]

			if fields[4] == "owned_city":
				city_owner = int(fields[6])
				maps[player][(x, y)] = chr(ord('C')+kronecker_inv(city_owner,player))
			elif fields[4] == "piece":
				piece_owner = int(fields[5])
				piece_type = int(fields[7])
				maps[player][(x, y)] = chr(ord('M') + piece_type + kronecker_inv(piece_owner,player) * nb_piece_type)
			elif fields[4] == "city":
				maps[player][(x, y)] = 'c'
			elif fields[4] == "none":
				if terrain == "water":
					maps[player][(x, y)] = 'A'
				else:
					maps[player][(x, y)] = 'B'
			else:
				print "not handled: " + line
				sys.exit(1)
		elif fields[0] == "set_explored":
			x = int(fields[1])
			y = int(fields[2])

			terrain = fields[3]

			if terrain == "water":
				maps[player][(x, y)] = 'a'
			else:
				maps[player][(x, y)] = 'b'
		else:
			print "not handled: " + line
			sys.exit(1)
	elif line.startswith("action:"):
		fields = line[len("action: "):]
		player = int(fields[0])
		fields = fields[5:].split(" ")

		x = int(fields[2])
		y = int(fields[3])

		if fields[0] == "move":
			direction = int(fields[4])
			piece_type = int(fields[5])
			print_move(direction, piece_type)
		elif fields[0] == "set_city_production":
			piece_type = int(fields[4])
			print_set_city_production(piece_type)
		else:
			print "not handled: " + line
			sys.exit(1)
		#print_all_map(player)
		print_far_context(x,y,player)
		print_even_further_context(x,y,player)
		print_all_map(player)
		print_centered_map(x, y, player)

if output == "txt":
	pass
elif output == "py":
	print "maps = ["
	for i in range(nb_print_centered_map):
		print "map_%d, " % i
	print "]"
	print "far_contexts=["
	for i in range(nb_print_centered_map):
		print "far_context_%d, " % i
	print "]"
	print "even_further_contexts=["
	for i in range(nb_print_centered_map):
		print "even_further_context_%d, " % i
	print "]"
	print "decisions = ["
	for i in range(nb_print_centered_map):
		print "decision_%d, " % i
	print "]"
	print "decisions_piece_type = ["
	for i in range(nb_print_centered_map):
		print "decision_piece_type_%d, " % i
	print "]"
	print "decisions_type = ["
	for i in range(nb_print_centered_map):
		print "decision_type_%d, " % i
	print "]"
	nb_print_centered_map = 0
