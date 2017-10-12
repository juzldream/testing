#!/usr/bin/python3
#-*- coding:utf-8 -*-
#Date:22-09-2017
#Author:jhinno
#Version=.3

import sys
sys.path.append("..")
from tools.get_access_token import * 
from tools.tools import *
import unittest



class TestPing(unittest.TestCase):
	"""检查 jhinno restful api 是否可用:"""

	def setUp(self):
		self.tk = GetAccessToken()
		print("test add start")		

	def test_001(self):
		self.assertTrue(self.tk.getToken(), msg="登录失败了！")




	def tearDown(self):
		print("test add end")



if __name__ == '__main__':
	unittest.main()

