


class Cell():
	
	
	def __init__(self, row, column):
		self.row = row
		self.column = column
		self.links = []
		
	def __str__(self):
		return "[%i,%i]" % (self.row, self.column)
	
	def link(self, cell, bidi=True):
		if cell:
			self.links.append(cell)
			if bidi:
				cell.link(self, False)
			return self
	
	def unlink(self, cell, bidi=True):
		self.links.remove(cell)
		if bidi:
			cell.unlink(self, False)
		return self
	
	def neighbors(self):
		neighbors = []
		if self.north:
			neighbors.append(self.north)
		if self.south:
			neighbors.append(self.south)
		if self.east:
			neighbors.append(self.east)
		if self.west:
			neighbors.append(self.west)
		return neighbors
	
		