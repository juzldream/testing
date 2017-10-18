#!/usr/bin/python3
#-*- coding:utf-8 -*-
#Date:16-10-2017
#Author:jhinno
#Version=.3


import sys
sys.path.append("..")
from tools.tools import *
import unittest
import main



class TestDesktopStart(unittest.TestCase):
    """测试 appform 申请桌面 case："""

    def setUp(self):
        print("开始测试appform申请桌面【desktopStart api】 ...")
     

    def actions(self, arg1 , arg2, arg3, arg4 , arg5, arg6):

        self.url = arg5[0] + "desktopStart?os=" + \
                   arg1 + "&appid=" + arg2 + "&resource=" + arg3 + "&protocol=" + arg4 + "&token=" + arg5[1]
        self.result = Tools().access_web(self.url)

        if arg6 == "1":    
            self.assertEqual(self.result['result'], "success", msg = "self.result['message']")
        else:
            self.assertNotEqual(self.result['result'], "success", msg = "self.result['message']")


    @staticmethod
    def getTestFunc(arg1 , arg2, arg3, arg4 , arg5, arg6, arg7):
        def func(self):
            self.actions(arg1 , arg2, arg3, arg4 , arg5, arg6)
        return func

    def tearDown(self):
        print("【desktops api】 访问的URL地址为：")
        print(self.url)
        print("【desktops api】 测试返回值：")
        print(self.result)
        print("【desktops api】 测试结束...")




def generateTestCases(cases):
    arglists = []
    lenth = len(cases[0])
    for i in range(lenth):
        cas = cases[0][i]['name'] 
        ext = str(cases[0][i]['expect'])
        osm = cases[0][i]['OS']
        apd = cases[0][i]['appid']
        rce = cases[0][i]['resource']
        ptl = cases[0][i]['protocol']
        arglists.append((osm, apd, rce, ptl,  cases[1], str(ext), cas))

    for args in arglists:
        setattr(TestDesktopStart, 'test_desktopstart_{0}_{1}_{2}_{3}_{5}{5}{6}'.format(\
            args[0], args[1], args[2],args[3], args[4], args[5], args[6]), TestDesktopStart.getTestFunc(*args) )


generateTestCases(main.get_test_data(type='desktopStart'))



if __name__ == '__main__':
	unittest.main()

