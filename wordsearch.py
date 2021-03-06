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
		
		#add each character to the row
		for character in formatted_line.split(','):
			row.append(character)
			
		grid.append(row)
		
	file.close()
	return words, grid
	

def cache_grid(grid):
	cache = {}
	
	#go through every character in grid and add it position
	#to the list of positions for that letter in the cache
	for x, row in enumerate(grid):
		for y, column in enumerate(row):
			char_positions = cache.setdefault(column, [])
			char_positions.append((x,y))
	
	return cache
	
def check_for_word(grid, word, start, direction):
	#2d lists use y,x not x,y so we are taking these in backwards so the result can be return as x,y 
	y, x = start
	move_y, move_x = direction
	coords = []
	
	#the outer limit of the grid. since grid is square we only need size in one direction
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
	
		
def find_word(word, grid, cache):
		directions = [
			(-1,-1), #up left
			(-1,0), #up
			(-1,1), #up right
			(0,1), #right
			(1,1), #down right
			(1,0), #down
			(1,-1), #down left
			(0,-1) #left
		]
		
		starting_coords = cache[word[0]]
		
		#loop through all places in the grid where the word can start and check all 8 directions
		#for each until word is found
		for start in starting_coords:
			for direction in directions:
				found, coords = check_for_word(grid, word, start, direction)
				if found:
					return coords
					

def find_words(words, grid):
	cache = cache_grid(grid)
	result = []
	
	for word in words:
		coords = find_word(word, grid, cache)
		#convert list of tuples to a string
		coords_string = ",".join("(%s,%s)" %tup for tup in coords)
		
		word_location = word + ": " + coords_string
		result.append(word_location)
	
	return result
	

if __name__ == '__main__':
	#file that contains our word search to solve
	filename = "wordsearch.txt"
	
	words, grid = load_grid(filename)
	
	word_locations = find_words(words, grid)
	
	for entry in word_locations:
		print(entry)