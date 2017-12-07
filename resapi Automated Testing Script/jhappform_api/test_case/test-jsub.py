#!/usr/bin/python3
#-*- coding:utf-8 -*-
#Date:23-10-2017
#Author:jhinno
#Version=.3


import sys
sys.path.append("..")
from tools.tools import *
import unittest
import main



class TestJsub(unittest.TestCase):
    """测试 appform 提交作业 case："""

    def setUp(self):
        print("开始测试提交作业【jsub api】 ...")

    def tearDown(self):
        print("【jsub api】 访问的URL地址为：")
        print(self.url)
        print("【jsub api】 测试数据为：")
        print(self.data)
        print("【jsub api】 测试返回值：")
        print(self.result)
        print("【jsub api】 测试结束...")
        print(self.exp)


    def actions(self, arg1,arg2,arg3,arg4,arg5,arg6,arg7,arg8,arg9,arg10):
        self.url = arg8[0] + 'jsub?appid=fluent&params={"JH_CAS":"' +  arg1 + '"JH_DAT":' + "1" + '"JH_DUALTIMESTEP:"' + "2" \
        + '"JH_TIMESTEP:"' + "3" + '"JH_ITERATION:"' + "4" + '"JH_AUTOSAVE_FREQUENCY:"' + "5" + '"JH_VERSION:"' + "6" + \
        '","JH_RELEASE":"' + arg2  + '","JH_GUI_ENABLED":"' + arg3 + '","JH_NCPU":"' + arg5 + '","JH_PROJECT":' + arg4 \
        + '"JOB_PRIORITY:"' + "7" + ',"JH_JOB_NAME":' + arg6 + '"}&token=' + arg8[1]
        self.result = Tools().access_web(self.url)
        self.exp = arg10
        self.data = "期望值:" + arg2 + "\n作业名：" + arg6 + "\ncas文件：" + arg1 + "\n版本号：" + arg2 + "\nCPU个数：" + arg6   
        if arg7 == "1":    
            self.assertEqual(self.result['result'], 'success', msg = self.result['message'] )
        else:
            self.assertNotEqual(self.result['result'], 'success', msg = self.result['message'])


    @staticmethod
    def getTestFunc(arg1,arg2,arg3,arg4,arg5,arg6,arg7,arg8,arg9,arg10):
        def func(self):
            self.actions(arg1,arg2,arg3,arg4,arg5,arg6,arg7,arg8,arg9,arg10)
        return func



def generateTestCases(cases):
    arglists = []
    lenth = len(cases[0])
    for i in range(lenth):
        cas = cases[0][i]['name'] 
        ext = str(cases[0][i]['expect'])
        fil = cases[0][i]['casfile']
        rel = cases[0][i]['relese']
        gui = cases[0][i]['gui']
        pjt = cases[0][i]['project']
        cpu = cases[0][i]['ncpu']
        jne = cases[0][i]['jobname']
        arglists.append((fil, rel, gui, pjt, cpu, jne, ext, cases[1], cas,{"k1":"exp"}))
    for args in arglists:
        setattr(TestJsub, 'test_jsub_{0}_{1}_{2}_{3}_{4}_{5}_{6}{6}_{8}{0}'.format(\
            args[0],args[1],args[2],args[3],args[4],args[5],args[6],args[7],args[8],args[9]), TestJsub.getTestFunc(*args) )


generateTestCases(main.get_test_data(type='jsub'))



if __name__ == '__main__':
	unittest.main()

