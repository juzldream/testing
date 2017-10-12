#!/usr/bin/python3
#-*- coding:utf-8 -*-
#Date:12-10-2017
#Author:jhinno
#Version=.3

import sys
sys.path.append("..")
from tools.get_access_token import * 
from tools.tools import *
import unittest



class TestLogout(unittest.TestCase):
    """测试 appform 注销 case："""

    def setUp(self):
        print("start test login ...")
     
    def clear(self):
        #some cleanup code
        pass

    def actions(self, arg1):
        self.assertTrue(arg1, msg = "用户名或密码错误，没有获取到token值。登录appform失败！")


    @staticmethod
    def getTestFunc(arg1):
        def func(self):
            self.actions(arg1)
        return func

    def tearDown(self):
        print("test end login...")

def generateTestCases():
    arglists = [('arg11',), ('arg21', ), ('arg31',)]
    for args in arglists:
        setattr(TestLogout, 'test_func_%s'%(args[0]), TestLogout.getTestFunc(*args) )


s = generateTestCases()



if __name__ == '__main__':
	unittest.main()

