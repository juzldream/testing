#!/bin/python


from calculator import Count
import unittest


class TestAssert(unittest.TestCase):
	"""docstring for ClassName"""
	def setUp(self):
		print("start")

	def test_case(self):
		num = 10
		self.assertEqual(num,10,msg="输入的数字不等于10，测试不通过。")

	def test_case1(self):
		j = Count(9,7)
		self.assertTrue(j.is_prime(11),msg="不是一个质数。")

	def test_case2(self):
		n = "hello"
		m = "hello world"
		self.assertIn(n,m,msg="第二个参数不包含第一个参数。")

	def tearDown(self):
		print("test end")


if __name__ == '__main__':
	unittest.main()
