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
        print("start test login ...")
     
    def clear(self):
        #some cleanup code
        pass

    def actions(self, arg1):
        data_json = os.path.join(os.path.abspath('..'), "jhappform_api/test_data/data.json")
        datas = Tools().readi_test_data(data_json)
        url = datas['other_param'][0]['baseUrl'] + "logout?token=" + arg1 
        s = Tools().access_web(url)    
        self.assertEqual(s['result'],'success', msg = "token值不正确，注销appform失败！")


    @staticmethod
    def getTestFunc(arg1):
        def func(self):
            self.actions(arg1)
        return func

    def tearDown(self):
        print("test end login...")

def generateTestCases():
    t = Tools()
    data_json = os.path.join(os.path.abspath('..'), "jhappform_api/test_data/data.json")
    data_case = Tools().readi_test_data(data_json)
    arglists = []
    lenth = len(data_case['logout'][0])
    for i in range(lenth):
        cse = "case" + str(i + 1)
        tkn = data_case['logout'][0][cse][0]['data']['token']
        arglists.append((tkn,))
    arglists.append((t.read_token(),))
    for args in arglists:
        setattr(TestLogout, 'test_func_%s'%(args[0]), TestLogout.getTestFunc(*args) )


s = generateTestCases()



if __name__ == '__main__':
	unittest.main()

