#!/bin/python


from calculator import Count
import unittest


class TestAdd(unittest.TestCase):
	"""docstring for ClassName"""
	def setUp(self):
		print("test add start")		

	def test_add(self):
		j = Count(9,7)
		self.assertEqual(j.add(),16)

	def test_add1(self):
		j = Count(-1,23)
		self.assertEqual(j.add(),22,msg="add方法执行成功！")

	def tearDown(self):
		print("test add end")



if __name__ == '__main__':
	unittest.main()
	