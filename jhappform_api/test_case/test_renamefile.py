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
        print("开始测试登录【renamefile api】 ...")
     
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
        self.url = datas['other_param'][0]['baseUrl'] + "renamefile?old_file_name=" + appform_top + arg1 + "&new_file_name=" + appform_top + arg2 + "&token=" + access_token
        self.result = t.access_web(self.url)    
        self.assertEqual(self.result['result'],'success', msg = "token值不正确，appform 资源不可用！")


    @staticmethod
    def getTestFunc(arg1,arg2,arg3):
        def func(self):
            self.actions(arg1,arg2)
        return func

    def tearDown(self):
        print("【renamefile api】 访问的URL地址为：")
        print(self.url)
        print("【renamefile api】 测试返回值：")
        print(self.result)
        print("【renamefile api】 测试结束...")


def generateTestCases():
    t = Tools()
    
    data_json = os.path.join(os.path.abspath('..'), "jhappform_api/test_data/data.json")
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

