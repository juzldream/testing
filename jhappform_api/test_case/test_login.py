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
    """测试 appform 登录 case:"""
    

    def setUp(self):
        print("开始测试登录【login api】 ...")
     
    # def clear(self):
    #     #some cleanup code
    #     pass


    def tearDown(self):
        print("【login api】 访问的URL地址为：")
        print(self.url)
        print("【login api】 测试返回值：")
        print(self.result)
        print("【login api】 测试结束...")
       

    def actions(self, arg1, arg2 ,arg3):
        data_json = os.path.join(os.path.abspath('..'), "jhappform_api/test_data/data.json")
        datas = Tools().readi_test_data(data_json)
        self.url = datas['other_param'][0]['baseUrl'] + "login?username=" + arg1 + "&password=" + arg2
  
        self.result = Tools().access_web(self.url)  
        if arg3 == "0":
        
            self.assertNotEqual(self.result['result'],"success", msg = "用户:" + arg1 + "登录appform失败！用户名或密码错误，没有获取到token值。")
        else:
            self.assertEqual(self.result['result'],"success", msg = "用户：" + arg1 + "登录appform失败！")
            self.assertEqual(len(self.result['data'][0]['token']),160,msg="没有获得对应的token值。")



    @staticmethod
    def getTestFunc(arg1, arg2, arg3 ,arg4):
        def func(self):
            self.actions(arg1, arg2 , arg3)
        return func


def generateTestCases():
    data_json = os.path.join(os.path.abspath('..'), "jhappform_api/test_data/data.json")
    data_case = Tools().readi_test_data(data_json)
    print(type(data_case))
    arglists = []
    lenth = len(data_case['login'][0])
    for i in range(lenth):
        no = i + 10
        cse = "case" + str(i + 1)
        unm = data_case['login'][0][cse][0]['data']['username']
        pwd = data_case['login'][0][cse][0]['data']['password']
        ext = str(data_case['login'][0][cse][0]['data']['expect'])
        arglists.append((unm,pwd,ext,no))
    for args in arglists:
        setattr(TestLogin, 'test_login_%s_%s_%s_%s'%(args[0], args[1], args[2] , args[3]),TestLogin.getTestFunc(*args))

s = generateTestCases()



if __name__ =='__main__':
    unittest.main()



