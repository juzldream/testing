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



class TestDesktopshare(unittest.TestCase):
    """测试 appform 桌面共享 case："""

    def setUp(self):
        print("开始测试桌面共享【share api】 ...")


    def actions(self, arg1,arg2,arg3,arg4,arg5):
        self.url = arg5[0] + "desktop/share?id=" + arg1 + "&" + arg2 + "=" + arg3 + "&token=" + arg5[1]
        self.result = Tools().access_web(self.url)
        self.data = "期望值:" + arg4 + "\n桌面id：" + arg1 + "\n共享模式：" + arg2 + "\n共享用户：" + arg3
        if arg4 == "1":    
            self.assertEqual(self.result['result'], 'success', msg = "桌面共享失败！")
        else:
            self.assertNotEqual(self.result['result'], 'success', msg = "桌面共享失败！")



    @staticmethod
    def getTestFunc(arg1,arg2,arg3,arg4,arg5,arg6):
        def func(self):
            self.actions(arg1,arg2,arg3,arg4,arg5)
        return func

    def tearDown(self):
        print("【share api】 访问的URL地址为：")
        print(self.url)
        print("【share api】 测试数据为：")
        print(self.data)
        print("【share api】 测试返回值：")
        print(self.result)
        print("【share api】 测试结束...")
 

def generateTestCases(cases):
    arglists = []
    lenth = len(cases[0])
    for i in range(lenth):
        cas = cases[0][i]['name'] 
        ext = str(cases[0][i]['expect'])
        did = cases[0][i]['id']
        mod = cases[0][i]['mode']
        user= cases[0][i]['user']
        arglists.append((did, mod, user, ext, cases[1], cas))
    for args in arglists:
        setattr(TestDesktopshare, 'test_desktopshare_{0}_{1}_{2}_{3}{3}_{5}'.format(args[0], args[1], args[2], args[3], args[4],args[5]), TestDesktopshare.getTestFunc(*args) )


generateTestCases(main.get_test_data(type='sharedesktop'))



if __name__ == '__main__':
    unittest.main()

