from cell import Cell
from random import randint
from PIL import Image, ImageDraw

class Grid:
	def __init__(self, rows, columns):
		self.rows = rows
		self.columns = columns
		self.grid = self.prepare_grid()

		self.configure_cells()
		
	def __str__(self):
		output = '+' + '---+' * self.columns + '\n'
		for row in self.each_row():
			top = '|'
			bottom = '+'
			
			for cell in row:
				body = " {} ".format(self.contents_of(cell))
				if cell.east in cell.links:
					east_boundary = ' '
				else:
					east_boundary = '|'
				top += body + east_boundary
				
				if cell.south in cell.links:
					south_boundary = '   '
				else:
					south_boundary = '---'
				corner = '+'
				bottom += south_boundary + corner
			
			output += top + '\n'
			output += bottom + '\n'
		
		return output
	
	def prepare_grid(self):
		grid = [[] for i in range(self.rows)]
		for row in range(self.rows):
			grid[row] = [Cell(row, col) for col in range(self.columns)]
		return grid
	
	def cell(self, row, col):
		if (0 <= row < self.rows) and (0 <= col < self.columns):
			return self.grid[row][col]
		else:
			return None
		
	
	def each_cell(self):
		for row in self.grid:
			for cell in row:
				if cell:
					yield cell
	
	def each_row(self):
		for row in self.grid:
			yield row
					
	def configure_cells(self):
		for cell in self.each_cell():
			row, col = cell.row, cell.column
			if row == 0:
				cell.north = None
			else:
				cell.north = self.grid[row-1][col]
			if row == self.rows - 1:
				cell.south = None
			else:
				cell.south = self.grid[row+1][col]
			if col == 0:
				cell.west = None
			else:
				cell.west = self.grid[row][col-1]
			if col == self.columns - 1:
				cell.east = None
			else:
				cell.east = self.grid[row][col+1]
	
	def random_cell(self):
		row = randint(0,self.rows-1)
		col = randint(0,self.columns-1)
		return self.grid[row][col]
	

				
	def size(self):
		return self.rows * self.columns
	

	
	def contents_of(self, cell):
		return " "
	
	def to_png(self, filename, cell_size=20):
		filename = 'images/' + filename
		img_width = cell_size * self.columns + 1
		img_height = cell_size * self.rows + 1
		background_color = 'white'
		wall_color = 0
		
		img = Image.new('RGB', (img_width, img_height), background_color)
		draw = ImageDraw.Draw(img)
		for cell in self.each_cell():
			x1 = cell.column * cell_size
			y1 = cell.row * cell_size
			x2 = (cell.column + 1) * cell_size
			y2 = (cell.row + 1) * cell_size
			
			if not cell.north:
				draw.line((x1, y1, x2, y1), wall_color)
			if not cell.west:
				draw.line((x1, y1, x1, y2), wall_color)
			if cell.east not in cell.links:
				draw.line((x2, y1, x2, y2), wall_color)
			if cell.south not in cell.links:
				draw.line((x1, y2, x2, y2), wall_color)
			
		img.save(filename, 'PNG')
	
