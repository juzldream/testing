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



class TestCopyfile(unittest.TestCase):
    """测试 appform copy文件 case："""

    def setUp(self):
        print("开始测试复制文件【copyfile api】 ...")


    def actions(self, arg1,arg2,arg3,arg4):
        self.url = arg4[0] + "copyfile?source_file_name=" + arg1 + "&target_file_name=" + arg2 + "&token=" + arg4[1]
        self.result = Tools().access_web(self.url)
        self.data = "期望值:" + arg3 + "\n源文件：" + arg1 + "\n目标文件：" + arg2
        if arg3 == "1":    
            self.assertEqual(self.result['result'], 'success', msg = "copy文件失败！")
            self.assertEqual(self.result['message'],'复制成功。',msg = "copy文件失败！")
        else:
            self.assertNotEqual(self.result['result'], 'success', msg = "copy文件失败！")
            self.assertEqual(self.result['message'], arg1 + '不存在',msg = "copy文件失败！")


    @staticmethod
    def getTestFunc(arg1,arg2,arg3,arg4,arg5):
        def func(self):
            self.actions(arg1,arg2,arg3,arg4)
        return func

    def tearDown(self):
        print("【copyfile api】 访问的URL地址为：")
        print(self.url)
        print("【copyfile api】 测试数据为：")
        print(self.data)
        print("【copyfile api】 测试返回值：")
        print(self.result)
        print("【copyfile api】 测试结束...")
 

def generateTestCases(cases):
    arglists = []
    lenth = len(cases[0])
    for i in range(lenth):
        cas = cases[0][i]['name'] 
        ext = str(cases[0][i]['expect'])
        sfn = cases[0][i]['source_file_name']
        tfn = cases[0][i]['target_file_name']
        arglists.append((sfn, tfn, ext, cases[1], cas))
    for args in arglists:
        setattr(TestCopyfile, 'test_copyfile_{0}_{1}_{2}{2}_{4}'.format(args[0], args[1], args[2], args[3], args[4]), TestCopyfile.getTestFunc(*args) )


generateTestCases(main.get_test_data(type='copyfile'))



if __name__ == '__main__':
	unittest.main()

