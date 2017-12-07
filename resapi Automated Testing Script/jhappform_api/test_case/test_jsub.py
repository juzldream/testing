#!/usr/bin/python3
#-*- coding:utf-8 -*-
#Date:23-10-2017
#Author:jhinno
#Version=.3


import sys
sys.path.append("..")
from tools.tools import *
import unittest
import main
import json



class TestJsub(unittest.TestCase):
    """测试 appform 提交作业 case："""

    def setUp(self):
        print("开始测试提交作业【jsub api】 ...")

    def tearDown(self):
        print("【jsub api】 访问的URL地址为：")
        print(self.url)
        print("【jsub api】 测试数据为：")
        print(self.data)
        print("【jsub api】 测试返回值：")
        print(self.result)
        print("【jsub api】 测试结束...")



    def actions(self, arg1,arg2,arg3):
        self.url = arg2[0] + 'jsub?appid=fluent&params=' + arg1 + '&token=' + arg2[1]
        self.result = Tools().access_web(self.url)
        self.data = "期望值:" + arg3 + "\n请求参数:" + arg1
        if arg3 == "1":    
            self.assertEqual(self.result['result'], 'success', msg = "作业提交失败！")
        else:
            self.assertNotEqual(self.result['result'], 'success', msg = "作业提交失败！")



    @staticmethod
    def getTestFunc(arg1,arg2,arg3,arg4):
        def func(self):
            self.actions(arg1,arg2,arg3)
        return func



def generateTestCases(cases):
    arglists = []
    lenth = len(cases[0])
    for i in range(lenth):
        casname = cases[0][i]['must'][0]['name']
        expect  = cases[0][i]['must'][0]['expect']
        params  = cases[0][i]['optional'][0]
        params['casfile'] = cases[0][i]['must'][0]['casfile']
        arglists.append((json.dumps(params),cases[1],expect,casname))
    for args in arglists:
        setattr(TestJsub, 'test_jsub_{2}{2}_{3}'.format(args[0],args[1],args[2],args[3]), TestJsub.getTestFunc(*args) )


generateTestCases(main.get_test_data(type='jsub'))



if __name__ == '__main__':
	unittest.main()

