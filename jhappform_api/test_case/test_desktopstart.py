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



class TestDesktopStart(unittest.TestCase):
    """测试 appform 申请桌面 case："""

    def setUp(self):
        print("开始测试appform申请桌面【desktopStart api】 ...")
     

    def actions(self, arg1 , arg2, arg3, arg4 , arg5, arg6):
        data_json = os.path.join(os.path.abspath('..'), "jhappform_api/test_data/data.json")
        datas = Tools().readi_test_data(data_json) 
        self.url = datas['other_param'][0]['baseUrl'] + "desktopStart?os=" + \
                   arg1 + "&appid=" + arg2 + "&resource=" + arg3 + "&protocol=" + arg4 + "&token=" + arg5
        self.arg5 = arg5
        self.result = Tools().access_web(self.url)

        if arg6 == "1":    
            self.assertEqual(self.result['result'], "success", msg = "self.result['message']")
        else:
            self.assertNotEqual(self.result['result'], "success", msg = "self.result['message']")


    @staticmethod
    def getTestFunc(arg1 , arg2, arg3, arg4 , arg5, arg6, arg7):
        def func(self):
            self.actions(arg1 , arg2, arg3, arg4 , arg5, arg6)
        return func

    def tearDown(self):
        print("【desktops api】 访问的URL地址为：")
        print(self.url)
        print("【desktops api】 测试返回值：")
        print(self.result)
        print("【desktops api】 测试结束...")
        print(self.arg5)



def generateTestCases():
    t = Tools()
    
    data_json = os.path.join(os.path.abspath('..'), "jhappform_api/test_data/data.json")
    data_case = t.readi_test_data(data_json)
    arglists = []
    lenth = len(data_case['desktopStart'][0])
    for i in range(lenth):
        cse = "case" + str(i + 1)

        osm = data_case['desktopStart'][0][cse][0]['data']['OS']
        apd = data_case['desktopStart'][0][cse][0]['data']['appid']
        rce = data_case['desktopStart'][0][cse][0]['data']['resource']
        ptl = data_case['desktopStart'][0][cse][0]['data']['protocol']
        ext = data_case['desktopStart'][0][cse][0]['data']['expect']
        no = "_no_" + str(i)

        arglists.append((osm, apd, rce, ptl,  t.read_token(), str(ext), no))

    for args in arglists:
        setattr(TestDesktopStart, 'test_desktopstart_{0}_{1}_{2}_{3}_{5}{6}{6}'.format(\
            args[0], args[1], args[2],args[3], args[4], args[5], args[6]), TestDesktopStart.getTestFunc(*args) )


s = generateTestCases()



if __name__ == '__main__':
	unittest.main()

