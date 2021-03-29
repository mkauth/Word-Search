import wordsearch as search
import unittest

class WordSearchTestCase(unittest.TestCase):

	def setUp(self):
		self.test_grid = [
			['E','O','H','D','A'],
			['T','H','O','M','C'],
			['W','G','Q','H','A'],
			['R','A','E','B','T'],
			['W','O','L','F','N']
		]
	
	def test_load_grid_from_file(self):
		words, grid = search.load_grid("testwordsearch.txt")
		self.assertEqual(words, ['BEAR','CAT','DOG','WOLF'])
		self.assertEqual(grid, self.test_grid)
		
		
	def test_cache_grid(self):
		expected_cache = {
			'A': [(0,4),(2,4),(3,1)],
			'B': [(3,3)],
			'C': [(1,4)],
			'D': [(0,3)],
			'E': [(0,0),(3,2)],
			'F': [(4,3)],
			'G': [(2,1)],
			'H': [(0,2),(1,1),(2,3)],
			'L': [(4,2)],
			'M': [(1,3)],
			'N': [(4,4)],
			'O': [(0,1),(1,2),(4,1)],
			'Q': [(2,2)],
			'R': [(3,0)],
			'T': [(1,0),(3,4)],
			'W': [(2,0),(4,0)]
		}
		cache = search.cache_grid(self.test_grid)
		self.assertEqual(cache, expected_cache)

if __name__ == '__main__':
	unittest.main()