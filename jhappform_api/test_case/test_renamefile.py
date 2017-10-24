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



class TestRenamefile(unittest.TestCase):
    """测试 appform 重命名文件 case："""

    def setUp(self):
        print("开始测试文件重命名【renamefile api】 ...")
     
    def clear(self):
        #some cleanup code
        pass

    def actions(self, arg1,arg2,arg3,arg4):
        self.url = arg4[0] + "renamefile?old_file_name=" + arg1 + "&new_file_name=" + arg2 + "&token=" + arg4[1]
        self.result = Tools().access_web(self.url)
        self.data = "期望值:" + arg3 + "\n源文件：" + arg1 + "\n新命名文件：" + arg2
        if arg3 == "1":    
            self.assertEqual(self.result['result'], 'success', msg = "重命名文件失败！")
        else:
            self.assertNotEqual(self.result['result'], 'success', msg = "重命名文件失败！")



    @staticmethod
    def getTestFunc(arg1,arg2,arg3,arg4,arg5):
        def func(self):
            self.actions(arg1,arg2,arg3,arg4)
        return func

    def tearDown(self):
        print("【renamefile api】 访问的URL地址为：")
        print(self.url)
        print("【renamefile api】 测试数据为：")
        print(self.data)
        print("【renamefile api】 测试返回值：")
        print(self.result)
        print("【renamefile api】 测试结束...")
 



def generateTestCases(cases):
    arglists = []
    lenth = len(cases[0])
    for i in range(lenth):
        cas = cases[0][i]['name'] 
        ext = str(cases[0][i]['expect'])
        ofa = cases[0][i]['old_file_name']
        nfa = cases[0][i]['new_file_name']
        arglists.append((ofa, nfa, ext, cases[1], cas))

    for args in arglists:
        setattr(TestRenamefile, 'test_renamefile_{2}{2}{2}{2}_{4}'.format(args[0], args[1], args[2], args[3], args[4]), TestRenamefile.getTestFunc(*args) )

generateTestCases(main.get_test_data(type='renamefile'))



if __name__ == '__main__':
	unittest.main()

