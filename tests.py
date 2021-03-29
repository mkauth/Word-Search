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
		
		self.test_cache = {
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
	
	def test_load_grid_from_file(self):
		words, grid = search.load_grid("testwordsearch.txt")
		
		self.assertEqual(words, ['BEAR','CAT','DOG','WOLF'])
		self.assertEqual(grid, self.test_grid)
		
		
	def test_cache_grid(self):
		cache = search.cache_grid(self.test_grid)
		
		self.assertEqual(cache, self.test_cache)
		
		
	def test_check_direction_for_word_up_left_found(self):
		expected_coords = [(3,3),(2,2),(1,1)]
		found, coords = search.check_for_word(self.test_grid, "BQH", (3,3), (-1,-1))
		self.assertTrue(found)
		self.assertEqual(coords, expected_coords)
		
	def test_check_direction_for_word_up_left_not_found(self):
		expected_coords = []
		found, coords = search.check_for_word(self.test_grid, "BQQ", (3,3), (-1,-1))
		self.assertFalse(found)
		self.assertEqual(coords, expected_coords)
		
	def test_check_direction_for_word_up_left_not_found_grid_edge_reached(self):
		expected_coords = []
		found, coords = search.check_for_word(self.test_grid, "MHT", (1,3), (-1,-1))
		self.assertFalse(found)
		self.assertEqual(coords, expected_coords)
		
	def test_check_direction_for_word_up_found(self):
		expected_coords = [(3,3),(3,2),(3,1),(3,0)]
		found, coords = search.check_for_word(self.test_grid, "BHMD", (3,3), (-1,0))
		self.assertTrue(found)
		self.assertEqual(coords, expected_coords)
	
	def test_check_direction_for_word_up_not_found(self):
		expected_coords = []
		found, coords = search.check_for_word(self.test_grid, "BQQ", (3,3), (-1,0))
		self.assertFalse(found)
		self.assertEqual(coords, expected_coords)
		
	def test_check_direction_for_word_up_not_found_grid_edge_reached(self):
		expected_coords = []
		found, coords = search.check_for_word(self.test_grid, "HMDI", (2,3), (-1,0))
		self.assertFalse(found)
		self.assertEqual(coords, expected_coords)
	
	def test_check_direction_for_word_up_right_found(self):
		expected_coords = [(1,3),(2,2),(3,1)]
		found, coords = search.check_for_word(self.test_grid, "AQM", (3,1), (-1,1))
		self.assertTrue(found)
		self.assertEqual(coords, expected_coords)
		
	def test_check_direction_for_word_up_right_not_found(self):
		expected_coords = []
		found, coords = search.check_for_word(self.test_grid, "AQQ", (3,1), (-1,1))
		self.assertFalse(found)
		self.assertEqual(coords, expected_coords)
		
	def test_check_direction_for_word_up_right_not_found_grid_edge_reached(self):
		expected_coords = []
		found, coords = search.check_for_word(self.test_grid, "MATT", (1,3), (-1,1))
		self.assertFalse(found)
		self.assertEqual(coords, expected_coords)

	def test_check_direction_for_word_right_found(self):
		expected_coords = [(0,4),(1,4),(2,4),(3,4)]
		found, coords = search.check_for_word(self.test_grid, "WOLF", (4,0), (0,1))
		self.assertTrue(found)
		self.assertEqual(coords, expected_coords)
		
	def test_check_direction_for_word_right_not_found(self):
		expected_coords = []
		found, coords = search.check_for_word(self.test_grid, "WOLG", (4,0), (0,1))
		self.assertFalse(found)
		self.assertEqual(coords, expected_coords)
		
	def test_check_direction_for_word_right_not_found_grid_edge_reached(self):
		expected_coords = []
		found, coords = search.check_for_word(self.test_grid, "FNMM", (4,3), (0,1))
		self.assertFalse(found)
		self.assertEqual(coords, expected_coords)
		
	def test_check_direction_for_word_down_right_found(self):
		expected_coords = [(1,1),(2,2),(3,3)]
		found, coords = search.check_for_word(self.test_grid, "HQB", (1,1), (1,1))
		self.assertTrue(found)
		self.assertEqual(coords, expected_coords)

	def test_check_direction_for_word_down_right_not_found(self):
		expected_coords = []
		found, coords = search.check_for_word(self.test_grid, "HQQ", (1,1), (1,1))
		self.assertFalse(found)
		self.assertEqual(coords, expected_coords)
		
	def test_check_direction_for_word_down_right_not_found_grid_edge_reached(self):
		expected_coords = []
		found, coords = search.check_for_word(self.test_grid, "BNFJ", (3,3), (1,1))
		self.assertFalse(found)
		self.assertEqual(coords, expected_coords)
	
	def test_check_direction_for_word_down_found(self):
		expected_coords = [(4,1),(4,2),(4,3)]
		found, coords = search.check_for_word(self.test_grid, "CAT", (1,4), (1,0))
		self.assertTrue(found)
		self.assertEqual(coords, expected_coords)
		
	def test_check_direction_for_word_down_not_found(self):
		expected_coords = []
		found, coords = search.check_for_word(self.test_grid, "CART", (1,4), (1,0))
		self.assertFalse(found)
		self.assertEqual(coords, expected_coords)
		
	def test_check_direction_for_word_down_not_found_grid_edge_reached(self):
		expected_coords = []
		found, coords = search.check_for_word(self.test_grid, "TNC", (1,4), (1,0))
		self.assertFalse(found)
		self.assertEqual(coords, expected_coords)
		
	def test_check_direction_for_word_down_left_found(self):
		expected_coords = [(3,0),(2,1),(1,2)]
		found, coords = search.check_for_word(self.test_grid, "DOG", (0,3), (1,-1))
		self.assertTrue(found)
		self.assertEqual(coords, expected_coords)

	def test_check_direction_for_word_down_left_not_found(self):
		expected_coords = []
		found, coords = search.check_for_word(self.test_grid, "DOT", (0,3), (1,-1))
		self.assertFalse(found)
		self.assertEqual(coords, expected_coords)
		
	def test_check_direction_for_word_down_left_not_found_grid_edge_reached(self):
		expected_coords = []
		found, coords = search.check_for_word(self.test_grid, "BLUE", (3,3), (1,-1))
		self.assertFalse(found)
		self.assertEqual(coords, expected_coords)
		
	def test_check_direction_for_word_left_found(self):
		expected_coords = [(3,3),(2,3),(1,3),(0,3)]
		found, coords = search.check_for_word(self.test_grid, "BEAR", (3,3), (0,-1))
		self.assertTrue(found)
		self.assertEqual(coords, expected_coords)
		
	def test_check_direction_for_word_left_not_found(self):
		expected_coords = []
		found, coords = search.check_for_word(self.test_grid, "BEAN", (3,3), (0,-1))
		self.assertFalse(found)
		self.assertEqual(coords, expected_coords)
		
	def test_check_direction_for_word_left_not_found_grid_edge_reached(self):
		expected_coords = []
		found, coords = search.check_for_word(self.test_grid, "ART", (3,1), (0,-1))
		self.assertFalse(found)
		self.assertEqual(coords, expected_coords)
		
	def test_find_word(self):
		expected_coords = [(3,3),(2,3),(1,3),(0,3)]

		coords = search.find_word("BEAR", self.test_grid, self.test_cache)
		
		self.assertEqual(coords, expected_coords)
		
	def test_find_all_words(self):
		expected_result = [
			"BEAR: (3,3),(2,3),(1,3),(0,3)",
			"CAT: (4,1),(4,2),(4,3)",
			"DOG: (3,0),(2,1),(1,2)",
			"WOLF: (0,4),(1,4),(2,4),(3,4)"
		]
		test_words = ["BEAR", "CAT", "DOG", "WOLF"]
		
		result = search.find_words(test_words, self.test_grid)
		
		self.assertEqual(result, expected_result)
		
		
if __name__ == '__main__':
	unittest.main()