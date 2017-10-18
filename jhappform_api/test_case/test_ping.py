#!/usr/bin/python3
#-*- coding:utf-8 -*-
#Date:13-10-2017
#Author:jhinno
#Version=.3

import sys
sys.path.append("..")
from tools.tools import *
import unittest
import main



class TestPing(unittest.TestCase):
    """测试 appform 连接资源 case："""

    def setUp(self):
        print("开始测试appform资源是否可用【ping api】 ...")
     

    def actions(self, arg1, arg2, arg3):
        self.url = arg3[0] + "ping?token=" + arg1 
        self.result = Tools().access_web(self.url) 
        if arg2 == "1":    
            self.assertEqual(self.result['result'], "success", msg = "token值不正确，appform 资源不可用！")
        else:
            self.assertNotEqual(self.result['result'], "success", msg = "token值不正确，appform 资源不可用！")

    @staticmethod
    def getTestFunc(arg1 , arg2, arg3, arg4):
        def func(self):
            self.actions(arg1, arg2, arg3)
        return func

    def tearDown(self):
        print("【ping api】 访问的URL地址为：")
        print(self.url)
        print("【ping api】 测试返回值：")
        print(self.result)
        print("【ping api】 测试结束...")


def generateTestCases(cases):
    arglists = []
    lenth = len(cases[0])
    for i in range(lenth):
        cas = cases[0][i]['name'] 
        tkn = cases[0][i]['token']
        ext = str(cases[0][i]['expect'])
        arglists.append((tkn,ext,cases[1], cas))
    arglists.append((cases[1][1], str(1), cases[1],"case" + str(lenth + 1)))
    for args in arglists:
        setattr(TestPing, 'test_ping_{1}{1}{1}_{3}'.format(args[0] , args[1], args[2], args[3]), TestPing.getTestFunc(*args) )



generateTestCases(main.get_test_data(type='ping'))



if __name__ == '__main__':
	unittest.main()

