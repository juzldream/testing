#!/usr/bin/python3
#-*- coding:utf-8 -*-

import unittest
import HTMLTestRunner  
import time
import os

test_dir = os.path.join(os.getcwd(), "test_case")
report_dir = os.path.join(os.getcwd(), "report")

def all_case():
	discover = unittest.defaultTestLoader.discover(test_dir,pattern='test_*.py')
	return discover


if __name__ == '__main__':
	runner = unittest.TextTestRunner()

	now = time.strftime("%Y-%m-%d_%H-%M-%S", time.localtime())

	report_file = os.path.join(report_dir, "result_" + now + ".html")

	fp = open(report_file, "wb")
	runner = HTMLTestRunner.HTMLTestRunner(stream = fp,title = 'jhappform rest_api 自动化测试报告,测试结果如下：',description = '用例执行情况：')
	runner.run(all_case())
	fp.close()
