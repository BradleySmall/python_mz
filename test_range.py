"""
	Author: Bradley M. Small
	All work is my own, and copyright (c) 2014 is retained. 
	This code is provided as a testing exercise solely for evaluating me for employment. 

"""
import unittest
import range

class Test_Range(unittest.TestCase):
	def setUp(self):
		self.myRange = range.Range()

	def test_AddRange(self):
		self.assertTrue(self.myRange.AddRange(2,9))
		self.assertFalse(self.myRange.AddRange(2,9))

	def test_DeleteRange(self):
		self.assertTrue(self.myRange.AddRange(2,9))
		self.assertTrue(self.myRange.DeleteRange(2,9))
		self.assertFalse(self.myRange.DeleteRange(2,9))

	def test_QueryRange(self):
		self.assertTrue(self.myRange.AddRange(1,10))
		self.assertTrue(self.myRange.QueryRange(1,10))
		self.assertFalse(self.myRange.QueryRange(12,30))

if __name__ == '__main__':
	unittest.main()
