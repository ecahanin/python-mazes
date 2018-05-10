import random
from copy import deepcopy
from grid import Grid


def bintree(original_grid):
	grid = Grid(original_grid.rows, original_grid.columns)
	for cell in grid.each_cell():
		neighbors = []
		if cell.north:
			neighbors.append(cell.north)
		if cell.east:
			neighbors.append(cell.east)
		
		if neighbors:
			neighbor = random.choice(neighbors)
			if neighbor:
				cell.link(neighbor)
	return grid

def sidewinder(original_grid):
	grid = Grid(original_grid.rows, original_grid.columns)
	for row in grid.each_row():
		run = []
		
		for cell in row:
			run.append(cell)
			
			at_eastern_boundary = not bool(cell.east)
			at_northern_boundary = not bool(cell.north)
			
			should_close = at_eastern_boundary or (not at_northern_boundary and random.randint(0,2)==0)
			
			if should_close:
				member = random.choice(run)
				if member.north:
					member.link(member.north)
					run = []
			else:
				cell.link(cell.east)
	return grid


def broder(original_grid):
	grid = Grid(original_grid.rows, original_grid.columns)
	cell = grid.random_cell()
	unvisited = grid.size() - 1
	
	while unvisited > 0:
		neighbors = cell.neighbors()
		neighbor = random.choice(neighbors)
		if not neighbor.links:
			cell.link(neighbor)
			unvisited -= 1
		
		cell = neighbor
	return grid

def backtracker(original_grid):
	grid = Grid(original_grid.rows, original_grid.columns)
	start_at = grid.random_cell()
	stack = []
	stack.append(start_at)
	
	while stack:
		current = stack[-1]
		neighbors = [neighbor for neighbor in current.neighbors() if not neighbor.links]
		
		if not neighbors:
			stack.pop()
		else:
			neighbor = random.choice(neighbors)
			current.link(neighbor)
			stack.append(neighbor)
	
	return grid
	

def huntkill(original_grid):
	grid = Grid(original_grid.rows, original_grid.columns)
	current = grid.random_cell()
	while current:
		unvisited_neighbors = [neighbor for neighbor in current.neighbors() if not neighbor.links]
		if unvisited_neighbors:
			neighbor = random.choice(unvisited_neighbors)
			current.link(neighbor)
			current = neighbor
		else:
			current = None
			for cell in grid.each_cell():
				visited_neighbors = [neighbor for neighbor in cell.neighbors() if neighbor.links]
				if not cell.links and visited_neighbors:
					current = cell
					neighbor = random.choice(visited_neighbors)
					current.link(neighbor)
	return grid


def wilsons(original_grid):
	grid = Grid(original_grid.rows, original_grid.columns)
	unvisited = list(grid.each_cell())
	
	first = random.choice(unvisited)
	unvisited.remove(first)
	
	while unvisited:
		cell = random.choice(unvisited)
		path = [cell]
		
		while cell in unvisited:
			cell = random.choice(cell.neighbors())
			try:
				position = path.index(cell)
			except ValueError:
				position = None
			if position is not None:
				path = path[0:position+1]
			else:
				path.append(cell)
				
		for i, cell in enumerate(path[0:-1]):
			cell.link(path[i+1])
			unvisited.remove(cell)
	
	return grid
	
	
		