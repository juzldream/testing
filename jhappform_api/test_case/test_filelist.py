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



class TestFilelist(unittest.TestCase):
    """测试 appform 获取文件列表 case："""

    def setUp(self):
        print("开始测试获取文件列表【filelist api】 ...")


    def actions(self, arg1,arg2,arg3):
        self.url = arg3[0] + "filelist?dir=" + arg1 + "&token=" + arg3[1]
        self.result = Tools().access_web(self.url)
        self.data = "期望值:" + arg2 + "\n查找的目录:" + arg1
        if arg2 == "1":    
            self.assertEqual(self.result['result'], 'success', msg = "获取文件列表失败！")
        else:
            self.assertNotEqual(self.result['result'], 'success', msg = "获取文件列表失败！")


    @staticmethod
    def getTestFunc(arg1,arg2,arg3,arg4):
        def func(self):
            self.actions(arg1,arg2,arg3)
        return func

    def tearDown(self):
        print("【filelist api】 访问的URL地址为：")
        print(self.url)
        print("【filelist api】 测试数据为：")
        print(self.data)
        print("【filelist api】 测试返回值：")
        print(self.result)
        print("【filelist api】 测试结束...")
 

def generateTestCases(cases):
    arglists = []
    lenth = len(cases[0])
    for i in range(lenth):
        cas = cases[0][i]['name'] 
        ext = str(cases[0][i]['expect'])
        dri = cases[0][i]['dir']
        arglists.append((dri, ext, cases[1], cas))
    for args in arglists:
        setattr(TestFilelist, 'test_filelist_{0}_{1}{1}_{3}'.format(args[0], args[1], args[2], args[3]), TestFilelist.getTestFunc(*args) )


generateTestCases(main.get_test_data(type='filelist'))



if __name__ == '__main__':
	unittest.main()

