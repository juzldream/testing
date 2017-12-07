#!/usr/bin/python3
#-*- coding:utf-8 -*-
# date:2017-09-22
#Author:rzh
#Version=.1

import os
import time
import requests
import json

import smtplib  
from email.mime.text import MIMEText             
from email.mime.multipart import MIMEMultipart  
from email.header import Header


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
            #s = req.json()
            s = json.loads(req.text.replace('\n',' ')) 
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

    def read_token(self):
        try:
            fo = open('token.txt','r')
            tk = fo.read()

            return tk
            fo.close()
        except FileNotFoundError:
            return "没有找到文件或目录！"
        

    def set_token(self,str):
        try:
            fo = open('token.txt','w+')
            fo.write(str) 

            fo.close()
        except TypeError:
            return "没有获得token值！"
   


    def send_mail(self,Attachment,par):
        try:

            sender = "rzhou@jhinno.com"  
              

            receiver =  par

            sendfile = open(Attachment,"r").read()  
              
            att = MIMEText(sendfile,"base64","utf-8")  
            att["Content-Type"] = "application/octet-stream"  
            att["Content-Disposition"] = "attachment;filename = 'api_test_report.html'"  
              
            msg = MIMEMultipart('related')  
            msg['From'] = Header("API 自动化测试报告", 'utf-8')
            msg['To'] =  Header("测试组", 'utf-8')
            subject = 'JHAppform REST API 自动化测试报告'
            msg['Subject'] = Header('测试报告附件', 'utf-8')

            msg.attach(MIMEText(sendfile,'html','utf-8'))
            msg.attach(att)  
              


            smtp = smtplib.SMTP()  
            smtp.connect('mail.jhinno.com')  
            smtp.login('rzhou@jhinno.com','Juzl150702')  
            smtp.sendmail(sender,receiver.split(';'),msg.as_string())
            return "邮件发送成功"
        except smtplib.SMTPException:
            return "Error: 无法发送邮件"
