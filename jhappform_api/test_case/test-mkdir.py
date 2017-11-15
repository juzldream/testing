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



class TestMkdir(unittest.TestCase):
    """测试 appform 指定位置创建目录 case："""

    def setUp(self):
        print("开始测试指定目录下创建文件夹【mkdir api】 ...")


    def actions(self, arg1,arg2,arg3,arg4):
        self.url = arg4[0] + "mkdir?dirpath=" + arg1 + "&isforce=" + arg2 + "&token=" + arg4[1]
        self.result = Tools().access_web(self.url)
        self.data = "期望值:" + arg3 + "\n指定的路径：" + arg1 + "\n是否强制创建：" + arg2
        if arg3 == "1":    
            self.assertEqual(self.result['result'], 'success', msg = "文件夹创建失败！")

        else:
            self.assertNotEqual(self.result['result'], 'success', msg = "文件夹创建失败！")



    @staticmethod
    def getTestFunc(arg1,arg2,arg3,arg4,arg5):
        def func(self):
            self.actions(arg1,arg2,arg3,arg4)
        return func

    def tearDown(self):
        print("【mkdir api】 访问的URL地址为：")
        print(self.url)
        print("【mkdir api】 测试数据为：")
        print(self.data)
        print("【mkdir api】 测试返回值：")
        print(self.result)
        print("【mkdir api】 测试结束...")
 

def generateTestCases(cases):
    arglists = []
    lenth = len(cases[0])
    for i in range(lenth):
        cas = cases[0][i]['name'] 
        ext = str(cases[0][i]['expect'])
        foc = cases[0][i]['isforce']
        pth = cases[0][i]['dirpath']
        arglists.append((pth, foc, ext, cases[1], cas))
    for args in arglists:
        setattr(TestMkdir, 'test_mkdir_{0}_{1}_{2}{2}_{4}'.format(args[0], args[1], args[2], args[3], args[4]), TestMkdir.getTestFunc(*args) )


generateTestCases(main.get_test_data(type='mkdir'))



if __name__ == '__main__':
	unittest.main()

