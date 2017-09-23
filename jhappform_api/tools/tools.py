#!/usr/bin/python3
#-*- coding:utf-8 -*-
# date:2017-09-22
#Author:rzh
#Version=.1

import os
import time
import requests
import json



class Tools():
    '''
    工具类函数。
    '''
    
    def __init__(self):
        '''
        初始化访问地址。
        '''

    def access_web(self,url):
        '''
        模仿浏览器访问url，返回json数据。
        '''
        try:
            req = requests.get(url=url)
            s = req.json() 
            return s      
        except requests.exceptions.ConnectTimeout:
            return "appform 请求超时！"
        except requests.exceptions.InvalidSchema:
            return "没有找到连接适配器！"
        except requests.exceptions.ConnectionError:
            return "appform 连接不上！"
        except :
                return "unkown error."

    def readi_test_data(self,case_file):
        '''
        读取json数据，用于api测试。
        '''
        try:
            f = open(case_file)
            s = json.load(f)
        except ValueError:
            return "给定的 json 数据格式有误！"
        except IOError:
            return "没有找到文件或文件读取失败！"
        else:
            return s

