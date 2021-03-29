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
		
		

if __name__ == '__main__':
	unittest.main()