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
         print("start test ...")
     
     def clear(self):
         #some cleanup code
         pass

     def actions(self, arg1, arg2):
         print(arg1,arg2)
         self.assertFalse(0, msg="登录失败了！")


     @staticmethod
     def getTestFunc(arg1, arg2):
         def func(self):
             self.actions(arg1, arg2)
         return func

     def tearDown(self):
         print("test end ...")

def generateTestCases():
    data_json = os.path.join(os.path.abspath('..'), "test_data/data.json")
    data_case = Tools().readi_test_data(data_json)
    arglists = []
    lenth = len(data_case['login'][0])
    for i in range(lenth):
        cse = "case" + str(i + 1)
        unm = data_case['login'][0][cse][0]['data']['username']
        pwd = data_case['login'][0][cse][0]['data']['password']
        arglists.append((unm,pwd))
    for args in arglists:
        setattr(TestLogin, 'test_func_%s_%s'%(args[0], args[1]),TestLogin.getTestFunc(*args))
s = generateTestCases()

if __name__ =='__main__':
    test_data = os.path.join(os.path.abspath('..'), "test_data/data.json")
    print(test_data)
    unittest.main()


# data_json = os.path.join(os.path.abspath('..'), "test_data/data.json")
# data_case = Tools().readi_test_data(data_json)
# lenth = len(data_case['login'][0])
# print(lenth)
# arglists = []
# for i in range(lenth):
#     cse = "case" + str(i + 1)
#     unm = data_case['login'][0][cse][0]['data']['username']
#     pwd = data_case['login'][0][cse][0]['data']['password']
#     arglists.append((unm,pwd))


# print(arglists)

