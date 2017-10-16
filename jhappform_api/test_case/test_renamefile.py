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
    """测试 appform 重命名文件 case："""

    def setUp(self):
        print("开始测试文件重命名【renamefile api】 ...")
     
    def clear(self):
        #some cleanup code
        pass

    def actions(self, arg1,arg2,arg3,arg4):
        data_json = os.path.join(os.path.abspath('..'), "jhappform_api/test_data/data.json")
        datas = Tools().readi_test_data(data_json)
        self.url = datas['other_param'][0]['baseUrl'] + "renamefile?old_file_name=" + arg1 + "&new_file_name=" + arg2 + "&token=" + arg3
        self.result = Tools().access_web(self.url)
        if arg4 == "1":    
            self.assertEqual(self.result['result'], 'success', msg = "重命名文件失败！")
        else:
            self.assertNotEqual(self.result['result'], 'success', msg = "重命名文件失败！")



    @staticmethod
    def getTestFunc(arg1,arg2,arg3,arg4,arg5):
        def func(self):
            self.actions(arg1,arg2,arg3,arg4)
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
    data_case = t.readi_test_data(data_json)
    arglists = []
    lenth = len(data_case['renamefile'][0])
    for i in range(lenth):
        no = "_no_" + str(i)
        cse = "case" + str(i + 1)
        ext = data_case['renamefile'][0][cse][0]['data']['expect']
        ofa = data_case['renamefile'][0][cse][0]['data']['old_file_name']
        nfa = data_case['renamefile'][0][cse][0]['data']['new_file_name']
        arglists.append((ofa, nfa, t.read_token(), ext, no ))
    for args in arglists:
        setattr(TestRenamefile, 'test_renamefile_{0}_{1}_{3}_{3}_{4}'.format(args[0], args[1], args[2], args[3], args[4]), TestRenamefile.getTestFunc(*args) )

s = generateTestCases()



if __name__ == '__main__':
	unittest.main()

