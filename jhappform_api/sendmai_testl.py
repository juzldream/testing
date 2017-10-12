#!/usr/bin/python
# -*- coding: UTF-8 -*-


import smtplib
from email.mime.text import MIMEText
from email.header import Header


def sendmail(Subject,no,name,title,url,error,msg):
            from_addr = "rzhou@jhinno.com"
            password  = "Juzl150702"
            to_addr1   = "1576768715@qq.com"
            to_addr   = "zhou@jhinno.com"
            # to_addr2   = "bzhang1@jhinno.com"


            # title = title
            # content = "rest api test."
            subject = Subject
            mail_msg = msg

            msg = MIMEText(mail_msg,'html','utf-8')
            msg["Subject"] = subject
            msg["From"]    = from_addr
            msg["To"]      = to_addr

            try:
                s = smtplib.SMTP_SSL("smtp.jhinno.com", 465)
                s.login(from_addr, password)
                s.sendmail(from_addr,[to_addr,to_addr1], msg.as_string())
                s.quit()
                return "Success!"
            except smtplib.SMTPException:
                return "Error :无法发送邮件"



Subject = "resapi test report."
no      = "001"
name    = "login"
title   = "login登录api测试。"
url     = "login?username=jhadmin&password=jhadmin"
error   = "445F0C4752AADC07982DEE4BD0E8B21447899E89CDF7DCC887883633D8A24D8E4A7F790CD928232D3D9A4254CF60554B869F04E4D1AE626D60B41552560DF7FD24968EED0D129BFBBBA7A9542BA6A96F [用户登录 CASE-EXPECT-TRUE] 测试: PASS。 "
msg = '<table border="1"><tr><th>测试环境</th><td>' + '"appform 4.0"' + '</td></tr>'
for x in range(0,2):
    msg += '<tr><th>问题编号</th><td>' + str(x) + '</td></tr><tr><th>测试api</th><td>' + name + \
    '</td></tr><tr><th>api访问地址</th><td>' + url + '</td></tr><tr><th>简单描述</th><td>' + title + \
    '</td></tr><tr><th>错误详细信息</th><td>'+ error + '</td></tr>'
msg += '</table>'

s = sendmail(Subject,no,name,title,url,error,msg)
print(s)

