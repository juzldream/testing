#!/usr/bin/python
# -*- coding: UTF-8 -*-
#Date:02-06-2017
#Version=.1


import tool
import main
import sys
import time
import urllib


default_encoding = 'utf-8'
if sys.getdefaultencoding() != default_encoding:
    reload(sys)
    sys.setdefaultencoding(default_encoding)


putlog = tool.putlog


###/* 申请桌面 。*/###
def applydesktop(apivar):
	try:
		deurl = apivar['apiurl'] + "desktopStart?os=" +  apivar['os'] + "&appid=" + apivar['appid'] + "&resource=" + apivar['resource'] + "&protocol=" + apivar['protocol'] + "&token=" + apivar['access_token']
		s = tool.geturl(deurl)
		if apivar['expect'] == "true":
			time.sleep(3)
			if s['result'] == "success":
				if tool.operatepsql(apivar):
					log = deurl + "\n\n申请 " + apivar['appid'] + " 成功，" + " 协议是：" +  apivar['protocol'] + "\n"
					putlog.info(log)
					log = "[申请桌面 CASE-EXPECT-TRUE]: 测试 PASS。" + "\n"
					putlog.info(log)
			else:
				putlog.info(s)
				putlog.info(s['message'])
				log = "[申请桌面 CASE-EXPECT-TRUE]: 测试 Failure。" + "\n"
				putlog.info(log)
		else:
			if s['result'] == "success": 
				log = "[申请桌面 CASE-EXPECT-FALSE]: 测试 Failure。" + "\n"
				putlog.info(log)
			else:
				log = deurl + "\n\n" + s['message'] + "\n"
				putlog.info(log)
				log = "[申请桌面 CASE-EXPECT-FALSE]: 测试 PASS。" + "\n"
				putlog.info(log)
	except:
	    log = "unkown error. \n"
	    putlog.error(log)


###/* 根据scope查询桌面列表 。*/###
def desktopscope(apivar):
	try:
		scurl = apivar['apiurl'] + "desktops?token=" + apivar['access_token']
		s = tool.geturl(scurl)
		if s['result'] == "success":
			if len(s['data']) == len(apivar['datainfo']):
				log = scurl + "\n\n" + "根据用户scope查询桌面列表成功"  "\n"
				putlog.info(log)
				log = "[依据用户scope查询桌面列表 CASE-EXPECT-TRUE]: 测试 PASS。" + "\n"
				putlog.info(log)
		else:
			log = scurl + "\n\n" + s['message'] + "\n"
			putlog.info(log)
			putlog.info(0.0)
			log = "[依据用户scope桌面列表 CASE-EXPECT-FALSE]: 测试 Failure。" + "\n"
			putlog.info(log)
	except IndexError,e:
		log = "没有找到桌面列表相关信息。"
		putlog.info(log)
	except:
	    log = "unkown error. \n"
	    putlog.error(log)


###/* 根据桌面id查询桌面列表 。*/###
def searchiddesktop(apivar):
	try:
		idurl = apivar['apiurl'] + "desktop/" + apivar['desktopid'] + "?token=" + apivar['access_token']
		s = tool.geturl(idurl)
		if apivar['expect'] == "true":
			if s['result'] == "success":
				if s['data'][0]['id'] == apivar['desktopid']:
					log = idurl + "\n\n" + "根据桌面id查询桌面列表成功。桌面id是：" + s['data'][0]['id'] + "\n"
					putlog.info(log)
					log = "[依据桌面id查询桌面列表 CASE-EXPECT-TRUE]: 测试 PASS。" + "\n"
					putlog.info(log)
			else:
				log = idurl + "\n\n[依据桌面id查询桌面列表 CASE-EXPECT-TRUE]: 测试 Failure。" + s['result'] +"\n"
				putlog.info(log)
		else:
			if s['result'] == "success":
				log = "[依据桌面id查询桌面列表 CASE-EXPECT-FALSE]: 测试 Failure。" + "\n"
				putlog.info(log)
			else:
				log = idurl + "\n\n" + s['message'] + "\n"
				putlog.info(log)
				log = "[依据桌面id查询桌面列表 CASE-EXPECT-FALSE]: 测试 PASS。" + "\n"
				putlog.info(log)
	except:
		log = "unkown error. \n"
		putlog.error(log)


###/* 根据桌面id查询桌面列表 。*/###
def searchidlistdesktop(apivar):
	try:
		deskids = ""
		for x in range(len(apivar['desktopid']) - 1 ):
			deskids = apivar['desktopid'][x] + ","
		deskids += apivar['desktopid'][len(apivar['desktopid']) - 1] 
		idurl = apivar['apiurl'] + "desktopsbyid?ids=" + deskids + "&token=" + apivar['access_token']
		s = tool.geturl(idurl)
		if apivar['expect'] == "true":
			if s['result'] == "success":
				newids = ""
				for y in range(len(s['data'])):
					newids += s['data'][y]['id'] + ","
				if  newids.encode('utf-8') == deskids + ",":
					log = idurl + "\n\n" + "根据桌面id列表查询桌面列表成功。桌面ids是：" + newids + "\n"
					putlog.info(log)
					log = "[依据桌面id列表查询桌面 CASE-EXPECT-TRUE]: 测试 PASS。" + "\n"
					putlog.info(log)
			else:
				log = "[依据桌面id列表查询桌面 CASE-EXPECT-TRUE]: 测试 Failure。" + "\n"
				putlog.info(log)
		else:
			if s['result'] == "success":
			    log = "[依据桌面id列表查询桌面 CASE-EXPECT-FALSE]: 测试 Failure。" + "\n"
			    putlog.info(log)
			else:
			    log = idurl + "\n\n" + s['message'] + "\n"
			    putlog.info(log)
			    log = "[依据桌面id列表查询桌面 CASE-EXPECT-FALSE]: 测试 PASS。" + "\n"
			    putlog.info(log)
	except:
		log = "unkown error. \n"
		putlog.error(log)


###/* 根据桌面名称查询桌面列表 。*/###
def searchdesktopname(apivar):
	try:
		name = urllib.quote(apivar['name']) 
		naurl = apivar['apiurl'] + "desktopsbyname?name=" + name + "&token=" + apivar['access_token']
		s = tool.geturl(naurl)
		if apivar['expect'] == "true":
		    if s['result'] == "success": 
		    	if len(s['data']) == len(apivar['datainfo']):
					log = naurl + "\n\n" + "根据桌面名称查询桌面列表成功。桌面列表总数为 ：" + str(len(s['data'])) + "\n"
					putlog.info(log)
					log = "[根据桌面名称查询桌面列表成功 CASE-EXPECT-TRUE]: 测试 PASS。" + "\n"
					putlog.info(log)
			else:
				log = "[根据桌面名称查询桌面列表成功 CASE-EXPECT-TRUE]: 测试 Failure。" + "\n"
				putlog.info(log)
		else:
			if s['result'] == "success": 
				log = "[根据桌面名称查询桌面列表成功 CASE-EXPECT-TRUE]: 测试 Failure。" + "\n"
				putlog.info(log)
			else:
				log = naurl + "\n\n" + s['message'] + "\n"
				putlog.info(log)
				log = "[根据桌面名称查询桌面列表成功 CASE-EXPECT-FALSE]: 测试 PASS。" + "\n"
				putlog.info(log)
	except:
		log = "unkown error. \n"
		putlog.error(log)


###/* 关闭桌面 。*/###
def closedesktop(apivar):
	try:
		clurl = apivar['apiurl'] + "desktopClose?id=" + apivar['desktopid'] + "&token=" + apivar['access_token']
		s = tool.geturl(clurl)
		if apivar['expect'] == "true":
			if s['result'] == "success":
				if tool.operatepsql(apivar):
					log = "[关闭桌面 CASE-EXPECT-TRUE]: 测试 Failure。" + "\n"
					putlog.info(log)
				else:
					log = clurl + "\n\n" + s['message'] + "\n"
					putlog.info(log)
					log = "[关闭桌面 CASE-EXPECT-TRUE]: 测试 PASS。" + "\n"
					putlog.info(log)
		else:
			if s['result'] == "success":
				log = "[关闭桌面 CASE-EXPECT-FALSE]: 测试 Failure。" + "\n"
				putlog.info(log)
			else:
				log = clurl + "\n\n" + s['message'] + "\n"
				putlog.info(log)
				log = "[关闭桌面 CASE-EXPECT-FALSE]: 测试 PASS。" + "\n"
				putlog.info(log)
	except:
		log = "unkown error. \n"
		putlog.error(log)


###/* 共享桌面 。*/###
def sharedesktop(apivar):
	try:
		users = ""
		for x in range(len(apivar['users']) - 1 ):
			users += apivar['users'][x] + ","
		users += apivar['users'][len(apivar['users']) - 1 ]
		shurl = apivar['apiurl'] + "desktop/share?id=" + apivar['desktopid'] + "&" + apivar['sharedmode'] + "=" + users + "&token=" + apivar['access_token']
		s = tool.geturl(shurl)
		if apivar['expect'] == "true":
			if s['result'] == "success":
				userst = ""
				for i in range(len(tool.operatepsql(apivar)) - 1 ):
					userst += tool.operatepsql(apivar)[i][1] + ","
				userst += tool.operatepsql(apivar)[len(tool.operatepsql(apivar)) - 1][1]
				if users == userst:
					log = shurl + "\n\n" + s['message'] + "\n"
					putlog.info(log)
					log = "[共享桌面 CASE-EXPECT-TRUE]: 测试 PASS。" + "\n"
					putlog.info(log)
			else:
				putlog.info(shurl)
				log = "[共享桌面 CASE-EXPECT-TRUE]: 测试 Failure。" + "\n"
				putlog.info(log)
		else:
			if s['result'] == "success":
				if apivar['off'] == "true":
					log = "[取消桌面 CASE-EXPECT-FALSE]: 测试 PASS。" + "\n"
					putlog.info(log)
				else:
					log = "[共享桌面 CASE-EXPECT-FALSE]: 测试 Failure。" + "\n"
					putlog.info(log)				
			else:
				log = shurl + "\n\n" + s['message'] + "\n"
				putlog.info(log)
				log = "[共享桌面 CASE-EXPECT-FALSE]: 测试 PASS。" + "\n"
				putlog.info(log)
	except:
		log = "unkown error. \n"
		putlog.error(log)
