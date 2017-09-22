#!/bin/python


from calculator import Count
import unittest


class TestAss(unittest.TestCase):
	"""docstring for ClassName"""
	def setUp(self):
		print("test add start")		
	for x in range(1,3):
		def test_ass(self):
			s = x 
			self.assertTrue(s, msg="chenggou")

	def test_add1(self):
		s = ''
		self.assertTrue(s, msg="shibai")

	def tearDown(self):
		print("test add end")



if __name__ == '__main__':
	unittest.main()
	
