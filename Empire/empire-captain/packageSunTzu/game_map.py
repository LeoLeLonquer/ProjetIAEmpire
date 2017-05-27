class Map:
	def __init__(self):
		self.map = {}
		self.directions=[ (+1,  0),
						  (+1, -1),
						  ( 0, -1),
						  (-1,  0),
						  (-1, +1),
						  ( 0, +1) ]
		self.width = 44	 # TODO: modifier automatiquement!
		self.height = 24	# TODO: modifier automatiquement!
		self.half_size = 3


	def get_map(self):
		return self.map

	def get_width(self):
		return self.width

	def get_height(self):
		return self.height

	def get_half_size(self):
		return self.half_size

	def set_width(self, width):
		self.width=width

	def set_height(self,height):
		self.height=height

	def update_map(self,x,y,symb):
		self.map[(x,y)]=symb

	def cube_ring(self,center, radius):
		if radius == 0:
			return [center]
		q, r = center
		results = []
		for i in range(len(self.directions)):
			qa, ra = self.directions[i]
			qb, rb = self.directions[(i + 1) % len(self.directions)]
			qd, rd = qb - qa, rb - ra
			if qd != 0:
				qd = qd / abs(qd)
			if rd != 0:
				rd = rd / abs(rd)
			for j in range(radius):
				results.append((q + radius * qa + j * qd, r + radius * ra + j * rd))
		return results


	def get_centered_map(self,x, y):
		tiles = []
		minimap=[]
		for r in range(self.half_size + 1):
			tiles.extend(self.cube_ring((x, y), r))

		for py in range(y - self.half_size, y + self.half_size + 1):
			for px in range(x - self.half_size, x + self.half_size + 1):
				if (px, py) in tiles:
					if px < 0 or px >= self.width or py < 0 or py >= self.height:
						minimap.append('!')
					elif (px, py) in self.map:
						minimap.append(self.map[(px, py)])
					else:
						minimap.append('?')
		return minimap

	def print_all_map(self):
		for py in range(self.height):
			for px in range(self.width):
				if px < 0 or px >= self.width or py < 0 or py >= self.height:
					print '!',
				elif (px, py) in self.map:
					print self.map[(px, py)],
				else:
					print "?",
			print ""


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
			if symb in ennemy_units:
				if symb == 'D' :
					blood_to_spill=blood_to_spill+10
				else :
					blood_to_spill=blood_to_spill+1
		return blood_to_spill
