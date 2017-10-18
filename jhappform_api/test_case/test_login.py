#!/usr/bin/python3
#-*- coding:utf-8 -*-
#Date:22-09-2017
#Author:jhinno
#Version=.3



import sys
sys.path.append("..")
from tools.tools import *
import unittest
import os
import main


class TestLogin(unittest.TestCase):
    """测试 appform 登录 case:"""
    

    def setUp(self):
        print("开始测试登录【login api】 ...")


    def tearDown(self):
        print("【login api】 访问的URL地址为：")
        print(self.url)
        print("【login api】 测试返回值：")
        print(self.result)
        print("【login api】 测试结束...")
       

    def actions(self, arg1, arg2 ,arg3, arg4):
        self.url = arg4[0] + "login?username=" + arg1 + "&password=" + arg2
        self.result = Tools().access_web(self.url)  
        if arg3 == "0":
            self.assertNotEqual(self.result['result'],"success", msg = "用户:" + arg1 + "登录appform失败！用户名或密码错误，没有获取到token值。")
        else:
            self.assertEqual(self.result['result'],"success", msg = "用户：" + arg1 + "登录appform失败！")
            self.assertEqual(len(self.result['data'][0]['token']),160,msg="没有获得对应的token值。")



    @staticmethod
    def getTestFunc(arg1, arg2, arg3 ,arg4, arg5):
        def func(self):
            self.actions(arg1, arg2 , arg3, arg4)
        return func


def generateTestCases(cases):
    arglists = []
    lenth = len(cases[0])
    for i in range(lenth):
        cas = cases[0][i]['name'] 
        unm = cases[0][i]['username']
        pwd = cases[0][i]['password']
        ext = str(cases[0][i]['expect'])
        arglists.append((unm,pwd,ext,cases[1],cas))
    for args in arglists:
        setattr(TestLogin, 'test_login_{0}_{1}_{2}{2}_{4}'.format(args[0], args[1], args[2], args[3], args[4]),TestLogin.getTestFunc(*args))


generateTestCases(main.get_test_data(type='login'))



if __name__ =='__main__':
    unittest.main()



