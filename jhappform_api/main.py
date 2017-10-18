#!/usr/bin/python3
#-*- coding:utf-8 -*-
#Date:04-10-2017
#Author:jhinno
#Version=.3




import smtplib
from email.mime.text import MIMEText
from email.header import Header

import unittest
import HTMLTestReportCN
import time
import os


from tools.tools import *



#测试case文件存放位置
test_dir = os.path.join(os.getcwd(), "test_case")
#测试报告存放位置
report_dir = os.path.join(os.getcwd(), "report")
#测试数据文件位置
data_case_dir = os.path.join(os.getcwd(), "test_data/data.json")

#读取case数据
CASES = Tools().readi_test_data(data_case_dir)


url = CASES['other_param'][0]['baseUrl'] + "login?username=" + \
	  CASES['other_param'][0]['loginUser'][0]['username'] + "&password=" + \
	  CASES['other_param'][0]['loginUser'][0]['password']
#获取访问appform资源的token
ACCESS_TOKEN = Tools().access_web(url)['data'][0]['token']


def get_test_data(type):
	global CASES
	global ACCESS_TOKEN

	test_Data = CASES[type][0]['data']
	base_Url = CASES['other_param'][0]['baseUrl']

	return (test_Data,(base_Url,ACCESS_TOKEN))


def all_case():
	discover = unittest.defaultTestLoader.discover(test_dir,pattern='test_*.py')
	return discover





if __name__ == '__main__':
	runner = unittest.TextTestRunner()

	now = time.strftime("%Y-%m-%d_%H-%M-%S", time.localtime())

	report_file = os.path.join(report_dir, "result_" + now + ".html")

	fp = open(report_file, "wb")



	runner = HTMLTestReportCN.HTMLTestRunner(
											stream = fp,
											title = 'JHAppform rest_api 自动化测试报告。',
											description = '用例执行情况：')


	runner.run(all_case())
	fp.close()

	Tools().send_mail(report_file)


