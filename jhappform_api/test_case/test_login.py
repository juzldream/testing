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



class TestLogin(unittest.TestCase):

     def setUp(self):
         print("start test login ...")
     
     def clear(self):
         #some cleanup code
         pass

     def actions(self, arg1, arg2):
         url = "http://192.168.5.128:8080/appform/ws/" + "login?username="  + arg1 + "&password=" + arg2
         s = Tools().access_web(url)
         self.assertTrue(s["data"][0]["token"], msg = "用户名或密码错误，没有获取到token值。登录appform失败！")


     @staticmethod
     def getTestFunc(arg1, arg2):
         def func(self):
             self.actions(arg1, arg2)
         return func

     def tearDown(self):
         print("test end login...")

def generateTestCases():
    data_json = os.path.join(os.path.abspath('..'), "jhappform_api/test_data/data.json")
    data_json = os.path.join(os.path.abspath('/scripts/testing/jhappform_api'), "test_data/data.json")
    data_case = Tools().readi_test_data(data_json)
    print(type(data_case))
    arglists = []
    lenth = len(data_case['login'][0])
    for i in range(lenth):
        cse = "case" + str(i + 1)
        unm = data_case['login'][0][cse][0]['data']['username']
        pwd = data_case['login'][0][cse][0]['data']['password']
        arglists.append((unm,pwd))
    for args in arglists:
        setattr(TestLogin, 'test_login_%s_%s'%(args[0], args[1]),TestLogin.getTestFunc(*args))
s = generateTestCases()

if __name__ =='__main__':
    unittest.main()



