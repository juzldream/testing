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
        print("start test ping ...")
     
    def clear(self):
        #some cleanup code
        pass

    def actions(self, arg1):
        data_json = os.path.join(os.path.abspath('..'), "jhappform_api/test_data/data.json")
        datas = Tools().readi_test_data(data_json)
        url = datas['other_param'][0]['baseUrl'] + "ping?token=" + arg1 
        s = Tools().access_web(url)    
        self.assertEqual(s['result'],'success', msg = "token值不正确，appform 资源不可用！")


    @staticmethod
    def getTestFunc(arg1, arg2):
        def func(self):
            self.actions(arg1)
        return func

    def tearDown(self):
        print("test end ping...")

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

