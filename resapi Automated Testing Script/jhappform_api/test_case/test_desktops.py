#!/usr/bin/python3
#-*- coding:utf-8 -*-
#Date:16-10-2017
#Author:jhinno
#Version=.3

import sys
sys.path.append("..")
from tools.tools import *
import unittest
import main



class TestDesktops(unittest.TestCase):
    """测试 appform 根据当前用户 scope 查询桌面列表 case："""

    def setUp(self):
        print("开始测试appform根据当前用户 scope 查询桌面列表【desktops api】 ...")
     

    def actions(self, arg1, arg2, arg3):
        self.url = arg3[0] + "desktops?token=" + arg1 
        self.result = Tools().access_web(self.url) 
        self.data = "期望值:" + arg2 + "\ntoken值为：" + arg1 
        if arg2 == "1":    
            self.assertEqual(self.result['result'], "success", msg = self.result['message'])
        else:
            self.assertNotEqual(self.result['result'], "success", msg = self.result['message'])

    @staticmethod
    def getTestFunc(arg1 , arg2, arg3, arg4):
        def func(self):
            self.actions(arg1, arg2, arg3)
        return func

    def tearDown(self):
        print("【desktops api】 访问的URL地址为：")
        print(self.url)
        print("【desktops api】 测试数据为：")
        print(self.data)
        print("【desktops api】 测试返回值：")
        print(self.result)
        print("【desktops api】 测试结束...")



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
        setattr(TestDesktops, 'test_desktops_{1}{1}{1}_{3}'.format(args[0] , args[1], args[2], args[3]), TestDesktops.getTestFunc(*args) )


generateTestCases(main.get_test_data(type='desktops'))



if __name__ == '__main__':
	unittest.main()

