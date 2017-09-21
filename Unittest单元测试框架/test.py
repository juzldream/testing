#!/bin/python
#-*- coding:utf-8 -*-

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


class TestSub(unittest.TestCase):
	"""docstring for TestSub"""
	def setUp(self):
		print("test sub start")	

	def test_sub(self):
		j = Count(15,6)
		self.assertEqual(j.sub(),9,msg="sub方法执行成功！")	

	def test_sub1(self):
		j = Count(-5,36)
		self.assertEqual(j.sub(),1,msg="sub方法执行成功！")	
		
	def tearDown(self):
		print("test sub end")


if __name__ == '__main__':
	# unittest.main()
	suite = unittest.TestSuite()
	suite.addTest(TestAdd("test_add"))
	suite.addTest(TestAdd("test_add1"))

	suite.addTest(TestSub("test_sub1"))
	suite.addTest(TestSub("test_sub"))

	runner = unittest.TextTestRunner()
	runner.run(suite)
