

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