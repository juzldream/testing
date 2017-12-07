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



class TestActionjobs(unittest.TestCase):
    """测试 appform 操作多个作业 case："""

    def setUp(self):
        print("开始测试操作（kill、resume、stop、hsit）多个作业【action api】 ...")


    def actions(self, arg1,arg2,arg3,arg4):
        self.url = arg4[0] + "jobs/" + arg2 + "?id="  + arg1 + "&token=" + arg4[1]
        self.result = Tools().access_web(self.url)
        self.data = "期望值:" + arg3 + "\n作业id：" + arg1 + "\n操作行为：" + arg2
        if arg3 == "1":    
            self.assertEqual(self.result['result'], 'success', msg = "操作失败！")
        else:
            self.assertNotEqual(self.result['result'], 'success', msg = "操作失败！")


    @staticmethod
    def getTestFunc(arg1,arg2,arg3,arg4,arg5):
        def func(self):
            self.actions(arg1,arg2,arg3,arg4)
        return func

    def tearDown(self):
        print("【action api】 访问的URL地址为：")
        print(self.url)
        print("【action api】 测试数据为：")
        print(self.data)
        print("【action api】 测试返回值：")
        print(self.result)
        print("【action api】 测试结束...")
 

def generateTestCases(cases):
    arglists = []
    lenth = len(cases[0])
    for i in range(lenth):
        cas = cases[0][i]['name'] 
        ext = str(cases[0][i]['expect'])
        idn = cases[0][i]['ids']
        exp = cases[0][i]['action']
        arglists.append((idn, exp, ext, cases[1], cas))
    for args in arglists:
        setattr(TestActionjobs, 'test_actionjobs_{0}_{1}_{2}{2}_{4}'.format(args[0], args[1], args[2], args[3], args[4]), TestActionjobs.getTestFunc(*args) )


generateTestCases(main.get_test_data(type='actionjobs'))



if __name__ == '__main__':
	unittest.main()

