#!/usr/bin/python3
#-*- coding:utf-8 -*-
#Date:20-10-2017
#Author:jhinno
#Version=.3


import sys
sys.path.append("..")
from tools.tools import *
import unittest
import main



class Testdesktopclose(unittest.TestCase):
    """测试 appform 关闭桌面 case："""

    def setUp(self):
        print("开始测试关闭桌面【desktopClose api】 ...")

    def tearDown(self):
        print("【desktopClose api】 访问的URL地址为：")
        print(self.url)
        print("【desktopClose api】 测试数据为：")
        print(self.data)
        print("【desktopClose api】 测试返回值：")
        print(self.result)
        print("【desktopClose api】 测试结束...")


    def actions(self, arg1,arg2,arg3):
        self.url = arg3[0] + "desktopClose?id=" + arg1 + "&token=" + arg3[1]
        self.result = Tools().access_web(self.url)
        self.data = "期望值:" + arg2 + "\n桌面ID：" + arg1 
        if arg2 == "1":    
            self.assertEqual(self.result['result'], 'success', msg = self.result['message'] )
        else:
            self.assertNotEqual(self.result['result'], 'success', msg = self.result['message'])


    @staticmethod
    def getTestFunc(arg1,arg2,arg3,arg4):
        def func(self):
            self.actions(arg1,arg2,arg3)
        return func


 

def generateTestCases(cases):
    arglists = []
    lenth = len(cases[0])
    for i in range(lenth):
        cas = cases[0][i]['name'] 
        ext = str(cases[0][i]['expect'])
        idn = cases[0][i]['id']
        arglists.append((idn, ext, cases[1], cas))
    for args in arglists:
        setattr(Testdesktopclose, 'test_desktopclose_{0}_{1}{1}_{3}'.format(args[0], args[1], args[2], args[3]), Testdesktopclose.getTestFunc(*args) )


generateTestCases(main.get_test_data(type='desktopclose'))



if __name__ == '__main__':
	unittest.main()

