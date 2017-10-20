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



class TestDeletefile(unittest.TestCase):
    """测试 appform 删除文件 case："""

    def setUp(self):
        print("开始测试删除文件【deletefile api】 ...")


    def actions(self, arg1,arg2,arg3):
        self.url = arg3[0] + "deletefile?file_name=" + arg1 + "&token=" + arg3[1]
        self.result = Tools().access_web(self.url)
        self.data = "期望值:" + arg2 + "\n要删除的文件名：" + arg1 
        if arg2 == "1":    
            self.assertEqual(self.result['result'], 'success', msg = "删除文件失败！")
            self.assertEqual(self.result['message'],'删除成功',msg = "删除文件失败！")
        else:
            self.assertNotEqual(self.result['result'], 'success', msg = "删除文件失败！")
            self.assertEqual(self.result['message'], arg1 + '不存在',msg = "删除文件失败！")


    @staticmethod
    def getTestFunc(arg1,arg2,arg3,arg4):
        def func(self):
            self.actions(arg1,arg2,arg3)
        return func

    def tearDown(self):
        print("【deletefile api】 访问的URL地址为：")
        print(self.url)
        print("【deletefile api】 测试数据为：")
        print(self.data)
        print("【deletefile api】 测试返回值：")
        print(self.result)
        print("【deletefile api】 测试结束...")
 

def generateTestCases(cases):
    arglists = []
    lenth = len(cases[0])
    for i in range(lenth):
        cas = cases[0][i]['name'] 
        ext = str(cases[0][i]['expect'])
        fae = cases[0][i]['file_name']
        arglists.append((fae, ext, cases[1], cas))
    for args in arglists:
        setattr(TestDeletefile, 'test_deletefile_{0}_{1}{1}_{3}'.format(args[0], args[1], args[2], args[3]), TestDeletefile.getTestFunc(*args) )


generateTestCases(main.get_test_data(type='deletefile'))



if __name__ == '__main__':
	unittest.main()

