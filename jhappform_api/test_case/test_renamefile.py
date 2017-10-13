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



class TestRenamefile(unittest.TestCase):
    """测试 appform 连接资源 case："""

    def setUp(self):
        print("start test ping ...")
     
    def clear(self):
        #some cleanup code
        pass

    def actions(self, arg1,arg2):
        print(arg1,arg2)
        t = Tools()
        data_json = os.path.join(os.path.abspath('..'), "jhappform_api/test_data/data.json")
        datas = t.readi_test_data(data_json)

        access_token = t.read_token()
        appform_top = datas['other_param'][0]['appform_top'] 
        # access_token = "62CF26204F88DFA5D810FBD1A53B2E7B47899E89CDF7DCC887883633D8A24D8E4A7F790CD928232D3D9A4254CF60554B869F04E4D1AE626D60B41552560DF7FD1D7D87FDA961649B126CAD224EB102C9"
        url = datas['other_param'][0]['baseUrl'] + "renamefile?old_file_name=" + appform_top + arg1 + "&new_file_name=" + appform_top + arg2 + "&token=" + access_token
        s = t.access_web(url)    
        # self.assertEqual(s['result'],'success', msg = "token值不正确，appform 资源不可用！")
        self.assertEqual(s['result'],'success', msg = "token值不正确，appform 资源不可用！")


    @staticmethod
    def getTestFunc(arg1,arg2,arg3):
        def func(self):
            self.actions(arg1,arg2)
        return func

    def tearDown(self):
        print("test end ping...")

def generateTestCases():
    t = Tools()
    
    data_json = os.path.join(os.path.abspath('..'), "jhappform_api/test_data/data.json")
    # data_json = "/scripts/testing/jhappform_api/test_data/data.json"
    data_case = Tools().readi_test_data(data_json)
    arglists = []
    lenth = len(data_case['renamefile'][0])
    for i in range(lenth):
        no = 10 + i 
        cse = "case" + str(i + 1)
        ofe = data_case['renamefile'][0][cse][0]['data']['old_file_name']
        nfe = data_case['renamefile'][0][cse][0]['data']['new_file_name']
        arglists.append((ofe,nfe,no))
    for args in arglists:
        
        setattr(TestRenamefile, 'test_renamefile_%s_%s_%s'%(args[0], args[1], args[2]), TestRenamefile.getTestFunc(*args) )


s = generateTestCases()



if __name__ == '__main__':
	unittest.main()

