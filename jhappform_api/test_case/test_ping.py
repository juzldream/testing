#!/usr/bin/python3
#-*- coding:utf-8 -*-
#Date:13-10-2017
#Author:jhinno
#Version=.3

import sys
sys.path.append("..")
from tools.get_access_token import * 
from tools.tools import *
import unittest



class TestPing(unittest.TestCase):
    """测试 appform 连接资源 case："""

    def setUp(self):
        print("开始测试登录【ping api】 ...")
     

    def actions(self, arg1):
        data_json = os.path.join(os.path.abspath('..'), "jhappform_api/test_data/data.json")
        datas = Tools().readi_test_data(data_json)
        self.url = datas['other_param'][0]['baseUrl'] + "ping?token=631D44080F69227B2F653B8C6ABD945747899E89CDF7DCC887883633D8A24D8E4A7F790CD928232D3D9A4254CF60554B869F04E4D1AE626D60B41552560DF7FD770323DD0AB49C51A939B26423B0B475" 
        self.result = Tools().access_web(self.url)    
        self.assertEqual(self.result, self.url, msg = "token值不正确，appform 资源不可用！")


    @staticmethod
    def getTestFunc(arg1 , arg2):
        def func(self):
            self.actions(arg1)
        return func

    def tearDown(self):
        print("【ping api】 访问的URL地址为：")
        print(self.url)
        print("【ping api】 测试返回值：")
        print(self.result)
        print("【ping api】 测试结束...")


def generateTestCases():
    t = Tools()
    
    data_json = os.path.join(os.path.abspath('..'), "jhappform_api/test_data/data.json")
    data_case = Tools().readi_test_data(data_json)
    arglists = []
    lenth = len(data_case['ping'][0])
    for i in range(lenth):
        no = i + 10
        cse = "case" + str(i + 1)
        png = data_case['ping'][0][cse][0]['data']['token']
        arglists.append((png,no))
    arglists.append((t.read_token(),999))
    for args in arglists:
        setattr(TestPing, 'test_ping_%s_%s'%(args[0], args[1]), TestPing.getTestFunc(*args) )


s = generateTestCases()



if __name__ == '__main__':
	unittest.main()

