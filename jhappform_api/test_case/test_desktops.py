#!/usr/bin/python3
#-*- coding:utf-8 -*-
#Date:16-10-2017
#Author:jhinno
#Version=.3

import sys
sys.path.append("..")
from tools.get_access_token import * 
from tools.tools import *
import unittest



class TestDesktops(unittest.TestCase):
    """测试 appform 根据当前用户 scope 查询桌面列表 case："""

    def setUp(self):
        print("开始测试appform根据当前用户 scope 查询桌面列表【desktops api】 ...")
     

    def actions(self, arg1, arg2):
        data_json = os.path.join(os.path.abspath('..'), "jhappform_api/test_data/data.json")
        datas = Tools().readi_test_data(data_json)
        self.url = datas['other_param'][0]['baseUrl'] + "desktops?token=" + arg1 
        self.result = Tools().access_web(self.url)
        if arg2 == "1":    
            self.assertEqual(self.result['result'], "success", msg = self.result['message'])
        else:
            self.assertNotEqual(self.result['result'], "success", msg = self.result['message'])

    @staticmethod
    def getTestFunc(arg1 , arg2, arg3):
        def func(self):
            self.actions(arg1, arg2)
        return func

    def tearDown(self):
        print("【desktops api】 访问的URL地址为：")
        print(self.url)
        print("【desktops api】 测试返回值：")
        print(self.result)
        print("【desktops api】 测试结束...")
        print("-----------------------------------")
        print("desktops api 返回的json串不正确。")


def generateTestCases():
    t = Tools()
    
    data_json = os.path.join(os.path.abspath('..'), "jhappform_api/test_data/data.json")
    data_case = Tools().readi_test_data(data_json)
    arglists = []
    lenth = len(data_case['desktops'][0])
    for i in range(lenth):
        no = "_no_" + str(i)
        cse = "case" + str(i + 1)
        png = data_case['desktops'][0][cse][0]['data']['token']
        ext = data_case['desktops'][0][cse][0]['data']['expect']
        arglists.append((png, ext, no))
    arglists.append((t.read_token(), str(1) ,"_" + str(lenth)))
    for args in arglists:
        setattr(TestDesktops, 'test_desktops_{1}{2}{2}'.format(args[0], args[1], args[2]), TestDesktops.getTestFunc(*args) )


s = generateTestCases()



if __name__ == '__main__':
	unittest.main()

