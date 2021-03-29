import wordsearch as search
import unittest

class WordSearchTestCase(unittest.TestCase):

	def setup(self):
		self.test_grid = [
			['E','O','H','D','A'],
			['T','H','O','M','C'],
			['W','G','Q','H','A'],
			['R','A','E','B','T'],
			['W','O','L','F','N']
		]