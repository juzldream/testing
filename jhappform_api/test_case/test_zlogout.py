#!/usr/bin/python3
#-*- coding:utf-8 -*-
#Date:12-10-2017
#Author:jhinno
#Version=.3

import sys
sys.path.append("..")
from tools.get_access_token import * 
from tools.tools import *
import unittest



class TestLogout(unittest.TestCase):
    """测试 appform 注销 case："""

    def setUp(self):
        print("开始测试登录【logout api】 ...")
     

    def actions(self, arg1):
        data_json = os.path.join(os.path.abspath('..'), "jhappform_api/test_data/data.json")
        datas = Tools().readi_test_data(data_json)
        self.url = datas['other_param'][0]['baseUrl'] + "logout?token=" + arg1 
        self.result = Tools().access_web(self.url)    
        self.assertNotEqual(self.result,'success', msg = "token值不正确，注销appform失败！")


    @staticmethod
    def getTestFunc(arg1, arg2):
        def func(self):
            self.actions(arg1)
        return func

    def tearDown(self):
        print("【logout api】 访问的URL地址为：")
        print(self.url)
        print("【logout api】 测试返回值：")
        print(self.result)
        print("【logout api】 测试结束...")

def generateTestCases():
    t = Tools()
    data_json = os.path.join(os.path.abspath('..'), "jhappform_api/test_data/data.json")
    data_case = Tools().readi_test_data(data_json)
    arglists = []
    lenth = len(data_case['logout'][0])
    for i in range(lenth):
        no  = i + 10 
        cse = "case" + str(i + 1)
        tkn = data_case['logout'][0][cse][0]['data']['token']
        arglists.append((tkn,no))
    arglists.append((t.read_token(),999))
    for args in arglists:
        setattr(TestLogout, 'test_logout_%s_%s'%(args[0] , args[1]), TestLogout.getTestFunc(*args) )


s = generateTestCases()



if __name__ == '__main__':
	unittest.main()

