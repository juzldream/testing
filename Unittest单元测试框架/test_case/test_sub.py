#!/bin/python


from calculator import Count
import unittest



class TestSub(unittest.TestCase):
	"""docstring for TestSub"""
	def setUp(self):
		print("test sub start")	

	def test_sub(self):
		j = Count(15,6)
		self.assertEqual(j.sub(),9,msg="sub方法执行成功！")	

	def test_sub1(self):
		j = Count(5,36)
		self.assertNotEqual(j.sub(),31,msg="sub方法执行成功！")	
		
	def tearDown(self):
		print("test sub end")


if __name__ == '__main__':
	unittest.main()
	