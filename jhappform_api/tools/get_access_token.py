#!/usr/bin/python3
#-*- coding:utf-8 -*-
#Date:12-10-2017
#Author:jhinno
#Version=.3


from tools.tools import *
import os

class Singleton(object):
    _instance = None
    def __new__(cls, *args, **kw):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls, *args, **kw)  
        return cls._instance  

class GetAccessToken(Singleton):
	"""获取登录appform获取token值。"""
	def __init_(self):
		self.token = None

	def getToken(self,datapath):
		try:
			tools = Tools()
			datas = tools.readi_test_data(datapath)
			url = datas['other_param'][0]['baseUrl'] + "login?username=" + \
				  datas['other_param'][0]['loginUser'][0]['username'] + \
				  "&password=" + datas['other_param'][0]['loginUser'][0]['password']
			s = tools.access_web(url)
			if s['result'] == "success":
				self.token = s['data'][0]['token']
				return self.token
		except TypeError:
			return "没有得到对应的有效值。"
