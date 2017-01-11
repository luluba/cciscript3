#!/usr/bin/python
import unittest

class TestReversal(unittest.TestCase):
	def testEmpty(self):
		self.assertEqual('', revStr(''))

	def testSingle(self):
		self.assertEqual('a', revStr('a'))

	def testDouble(self):
		self.assertEqual('ba', revStr('ab'))

	def testValid(self):
		words = (('mary', 'yram'),
				 ('peter', 'retep'),
				 ('anna', 'anna')
				)
		
		for orig, exp in words:
			expected = revStr(orig)
			self.assertEqual(exp, expected)
	
	def testInvalid(self):
		words = (('hello', 'olle'), ('henry', 'yrnhe'))
		for orig, nonexp in words:
			expected = revStr(orig)
			self.assertNotEqual(nonexp, expected)

def revStr(s):
	return s[ :: -1]

if __name__ == "__main__":
	unittest.main()
