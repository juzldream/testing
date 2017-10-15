#!/usr/bin/python3
#-*- coding:utf-8 -*-
#Date:04-10-2017
#Author:jhinno
#Version=.3




import smtplib
from email.mime.text import MIMEText
from email.header import Header

import unittest
#import HTMLTestRunner  
import HTMLTestReportCN
import time
import os


from tools.get_access_token import * 
from tools.tools import *

test_dir = os.path.join(os.getcwd(), "test_case")

report_dir = os.path.join(os.getcwd(), "report")

data_case_dir = os.path.join(os.getcwd(), "test_data/data.json")




def all_case():
	discover = unittest.defaultTestLoader.discover(test_dir,pattern='test_*.py')
	return discover

def get_access_token(casefile):
	l = Tools()
	g = GetAccessToken()
	str = g.getToken(casefile)
	s = l.set_token(str)



if __name__ == '__main__':
	get_access_token(data_case_dir)


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

	# l = Tools()
	# l.send_mail(report_file)


