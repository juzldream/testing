#!/usr/bin/python3
#-*- coding:utf-8 -*-
#Date:19-10-2017
#Author:jhinno
#Version=.3

import sys
sys.path.append("..")
from tools.tools import *
import unittest
import main



class TestUrl(unittest.TestCase):
    """测试 appform 返回应用页面url case："""

    def setUp(self):
        print("开始测试返回应用url【url api】 ...")

    def tearDown(self):
        print("【url api】 访问的URL地址为：")
        print(self.url)
        print("【url api】 测试数据为：")
        print(self.data)
        print("【url api】 测试返回值：")
        print(self.result)
        print("【url api】 测试结束...")  
     

    def actions(self, arg1, arg2, arg3):
        self.url = arg3[0] + "url?appname=" + arg1 + "&token=" + arg3[1] 
        self.result = Tools().access_web(self.url) 
        self.data = "期望值:" + arg2 + "\n应用名称：" + arg1 
        if arg2 == "0":
            self.assertEqual(self.result['result'],'failed', msg = "返回appform应用url测试失败！")
        else:
            self.assertEqual(self.result['result'],'success', msg = "返回appform应用url测试失败！")
            if arg1 == "jobmana":
                self.assertEqual(self.result['data'][0]['url'],'/appform/myjob/jobManagement?isInteractive=1', msg = "返回appform应用url测试失败！")
            elif arg1 == "desktopmana":
                self.assertEqual(self.result['data'][0]['url'],'/appform/mydesktop/desktopManagement?isInteractive=1', msg = "返回appform应用url测试失败！")
            elif arg1 == "spoolermana":
                self.assertEqual(self.result['data'][0]['url'],'/appform/mydata/dataManagement?isInteractive=1', msg = "返回appform应用url测试失败！")
            

    @staticmethod
    def getTestFunc(arg1, arg2, arg3, arg4):
        def func(self):
            self.actions(arg1, arg2, arg3)
        return func



def generateTestCases(cases):
    arglists = []
    lenth = len(cases[0])
    for i in range(lenth):
        cas = cases[0][i]['name'] 
        app = cases[0][i]['appname']
        ext = str(cases[0][i]['expect'])
        arglists.append((app,ext,cases[1], cas))
    for args in arglists:
        setattr(TestUrl, 'test_url_{1}{1}{1}_{3}'.format(args[0] , args[1], args[2], args[3]), TestUrl.getTestFunc(*args) )


generateTestCases(main.get_test_data(type='url'))



if __name__ == '__main__':
	unittest.main()

