#!/usr/bin/python3
#-*- coding:utf-8 -*-
#Date:22-09-2017
#Author:jhinno
#Version=.3

import sys
sys.path.append("..")
from tools.tools import *
import unittest

class TestLogout(unittest.TestCase):
	"""注销appform"""
	def setUp(self):
		print("test add start")		

#	def test_001(self):
#		s = Jobs().login()
#		self.assertTrue(s, msg="登录失败了！")

#	def test_002(self):
#		s = Jobs().login()
#		self.assertFalse(s, msg="登录失败了！")

	def test_03(self):
		js = Tools().readi_test_data('/scripts/jhappform_api/test_data/data.json')
		self.assertFalse(js, msg="登录失败了！")

	def test_04(self):
		js = Tools().readi_test_data('/scripts/jhappform_api/test_data/data.json')
		self.assertTrue(js, msg="登录失败了！")



	def tearDown(self):
		print("test add end")



if __name__ == '__main__':
	unittest.main()

