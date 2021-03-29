

def load_grid(filename):
	file = open(filename)
	
	#first line is word list, load them into variable
	first_line = file.readline()
	
	#remove trailing new line
	first_line = first_line.rstrip("\n")
	
	words = first_line.split(',')
	
	grid = []
	#remaining lines are the grid, loop through and put in 2d list
	for line in file:
		row=[]
		
		#remove trailing new line from string
		formatted_line = line.rstrip("\n")
		
		for character in formatted_line.split(','):
			row.append(character)
			
		grid.append(row)
		
	file.close()
	return words, grid
	

def cache_grid(grid):
	cache = {}
	
	for x,row in enumerate(grid):
		for y, column in enumerate(row):
			char_positions = cache.setdefault(column, [])
			char_positions.append((x,y))
	
	return cache
	
def check_for_word(grid, word, start, direction):
	y, x = start
	move_y, move_x = direction
	coords = []
	grid_limit = len(grid)
	
	for letter in word:
		#if current position is in bounds and letter is a match
		if(x >= 0 and y >= 0 and x < grid_limit and y < grid_limit and grid[y][x] == letter):
			coords.append((x,y))
		else:
			return (False, [])
		
		x += move_x
		y += move_y
	
	return (True, coords)
		
		