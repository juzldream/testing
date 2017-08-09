#!/usr/bin/python
# -*- coding: UTF-8 -*-
#Date:05-24-2017
#Version=.1



import tool
import main
import time
import os
import xml.dom.minidom
import requests 
import json
import os
import commands
import urllib2
import json
from poster.encode import multipart_encode
from poster.streaminghttp import register_openers



time =  str(int(time.time()))
putlog = tool.putlog


###/* 文件重命名  */###
def renamefile(apivar):
    try:
        nefi = "rename_protal.log.bak" + time
        rnurl = apivar['apiurl'] + "renamefile?old_file_name=" + apivar['appform_top'] + "logs/" +apivar['filename'] + "&new_file_name=" + nefi + "&token=" + apivar['access_token']
        s = tool.geturl(rnurl)
        path = apivar['appform_top'] + "logs/" + nefi
        if apivar['expect'] == "true":
            if s["result"] == "success" and os.path.isfile(path):            
                log = rnurl + "\n\n文件重命名成功," + " portal.log 文件命名为："  + nefi + "\n"
                putlog.info(log)
                log = "[文件重命名 CASE-EXPECT-TRUE] 测试: PASS。" + "\n"
                putlog.info(log)
                return nefi
            else:
                log = rnurl + "\n\n文件重命名失败: " + s['message'] + "\n"
                putlog.info(log)
                log = "[文件重命名 CASE-EXPECT-TRUE] 测试: Failure。" + "\n"
                putlog.error(log)
        else:
            if s["result"] == "success" and os.path.isfile(path):            
                log = "[文件重命名 CASE-EXPECT-FALSE] 测试: Failure。" + "\n"
                putlog.error(log)
            else:
                log = rnurl + "\n\n文件重命名失败: " + s['message'] + "\n"
                putlog.info(log)
                log = "[文件重命名 CASE-EXPECT-FALSE] 测试: PASS。" + "\n"
                putlog.info(log)
    except:
        log = "unkown error. \n"
        putlog.error(log)


###/* 指定目录创建文件夹  */###
def createfolder(apivar):
    try:
        path = apivar['appform_top'] + apivar['folder'] + time
        cfurl = apivar['apiurl'] + "mkdir?dirpath=" + path + "&isforce=" + apivar['isforce'] + "&token=" + apivar['access_token']
        s = tool.geturl(cfurl)
        if apivar['expect'] == "true" and apivar['isforce'] == "true":
            if s["result"] == "success" and os.path.isdir(path):
                log = cfurl + "\n\n目录创建成功，成功创建的目录是：" + apivar['folder'] + time + "\n"
                putlog.info(log)
                log = "[目录创建 CASE-EXPECT-TRUE] 测试: PASS。" + "\n"
                putlog.info(log)
            else:
                log = cfurl + "创建目录失败。" + "\n"
                putlog.info(log)
                log = "[目录创建 CASE-EXPECT-TRUE] 测试: Failure。" + "\n"
                putlog.error(log)
        else:
            if s["result"] == "success" and os.path.isdir(path):
                log = cfurl  + "\n"
                putlog.info(log)
                log = "[目录创建 CASE-EXPECT-FALSE] 测试: Failure。" + "\n"
                putlog.error(log)
            else:
                log = cfurl + s['message'] + "\n"
                putlog.info(log)
                log = "[目录创建 CASE-EXPECT-FALSE] 测试: PASS。" + "\n"
                putlog.info(log)
    except:
        log = "unkown error. \n"
        putlog.error(log)


###/* 复制文件  */###
def copyfile(apivar):
    try:
        source_file_name = apivar['appform_top'] + apivar['file'] 
        target_file_name = apivar['appform_top'] + "logs/portal.log.bak" + time
        courl = apivar['apiurl'] + "copyfile?source_file_name=" + source_file_name + "&target_file_name=" + target_file_name +"&token=" + apivar['access_token']
        s = tool.geturl(courl)
        if apivar['expect'] == "true":
            if s["result"] == "success" and os.path.isfile(target_file_name):
                tarfile = os.path.basename(target_file_name)
                log = courl + "\n\n文件复制成功，portal.log 文件成功复制为：" + tarfile + "\n"
                putlog.info(log)
                log = "[文件复制 CASE-EXPECT-TRUE] 测试: PASS。" + "\n"
                putlog.info(log)
                return tarfile
            else:
                log = courl + "\n\n" + s['message'] + "\n"
                putlog.info(log)
                log = "[文件复制 CASE-EXPECT-TRUE] 测试: Failure。" + "\n"
                putlog.error(log)
        else:
            if s["result"] == "success" and os.path.isfile(target_file_name):
                log = "[文件复制 CASE-EXPECT-FALSE] 测试: Failure。" + "\n"
                putlog.error(log)
            else:
                log = courl + "\n\n" + s['message'] + "\n"
                putlog.info(log)
                log = "[文件复制 CASE-EXPECT-FALSE] 测试: PASS。" + "\n"
                putlog.info(log)
    except:
        log = "unkown error. \n"
        putlog.error(log)


###/* 删除文件  */###
def deletefile(apivar):
    try:
        defile = apivar['defile'] 
        deurl = apivar['apiurl'] + "deletefile?file_name=" + apivar['appform_top'] + "logs/" + defile  + "&token=" + apivar['access_token']
        s = tool.geturl(deurl)
        if apivar['expect'] == "true":
            if s['result'] == "success" and os.path.isfile(defile):
                log = deurl + "\n\n" + s['message'] + "\n"
                putlog.info(log)
                log = "[文件删除 CASE-EXPECT-TRUE] 测试: Failure。" + "\n"
                putlog.error(log)
            else:
                log = deurl + "\n\n" + defile + "文件删除成功" + "\n"
                putlog.info(log)
                log = "[文件删除 CASE-EXPECT-TRUE] 测试: PASS。" + "\n"
                putlog.info(log)
                putlog.info(s['message'])
        else:
            if s["result"] == "success" and os.path.isfile(defile) == "False":
                log = "[文件删除 CASE-EXPECT-FALSE] 测试: Failure。" + "\n"
                putlog.error(log)
            else:
                log = deurl + "\n\n" + s['message'] + "\n"
                putlog.info(log)
                log = "[文件删除 CASE-EXPECT-TRUE] 测试: PASS。" + "\n"
                putlog.info(log)
    except:
        log = "unkown error. \n"
        putlog.error(log)

###/* 获取文件列表  */###
def getfilelist(apivar):
    try:
        path = apivar['appform_top'] + apivar['list']
        fsurl = apivar['apiurl'] + "filelist?dir=" + path +"&token=" + apivar['access_token']
        s = tool.geturl(fsurl)
        if apivar['expect'] == "true":
            if s['result'] == "success" and len(s['data']) == len(os.listdir(path)):
                log = fsurl + "\n\n获取文件列表成功，总文件个数： " + str(len(s['data'])) + "个， 文件目录如下：" + "\n\n"
                for x in range(len(s['data'])):
                    log += os.listdir(path)[x] + " , "
                log += "\n"
                putlog.info(log)
                log = "[获取文件列表 CASE-EXPECT-TRUE] 测试: PASS。" + "\n"
                putlog.info(log)
            else:
                log = fsurl + s['message'] + "\n"
                putlog.info(log)
                log = "[获取文件列表 CASE-EXPECT-FALSE] 测试: Failure。" + "\n"
                putlog.error(log)
        else:
            if s['result'] == "success" and len(s['data']) == len(os.listdir(path)):
                log = "[获取文件列表 CASE-EXPECT-FALSE] 测试: Failure。" + "\n"
                putlog.error(log)
            else:
                log = fsurl + s['message'] + "\n"
                putlog.info(log)
                log = "[获取文件列表 CASE-EXPECT-TRUE] 测试: PASS。" + "\n"
                putlog.info(log)
    except:
        log = "unkown error. \n"
        putlog.error(log)

###/* 返回appform所有应用列表  */###
def getapplist(apivar):
    pass
###/* 返回页面URL[jobmana、desktopmana、spoolermana]  */###
def getweburl(apivar):
    try:
        wburl = apivar['apiurl'] + "url?appname=" + apivar['appname'] + "&token=" + apivar['access_token']
        path = apivar['appform_top'] + "conf/desktop/apps.xml"
        s = tool.geturl(wburl)
        if apivar['appname'] == "jobmana":
            jobsurl = xml.dom.minidom.parse(path).documentElement.getElementsByTagName("app")[0].getAttribute("url")
            if s['result'] == "success" and s['data'][0]['url'] == jobsurl:
                log = wburl + "\n\n" + "获取作业管理URl成功，作业管理URl为：" + s['data'][0]['url'] + "\n"
                putlog.info(log)
                log = "[获取作业管理URl CASE-EXPECT-TRUE] 测试: PASS。" + "\n"
                putlog.info(log)
            else:
                log = "[获取作业管理URl CASE-EXPECT-TRUE] 测试: Failure。" + "\n"
                putlog.error(log)
        elif apivar['appname'] == "desktopmana":
            deskurl = xml.dom.minidom.parse(path).documentElement.getElementsByTagName("app")[2].getAttribute("url")
            if s['result'] == "success" and s['data'][0]['url'] == deskurl:
                log = wburl + "\n\n" + "获取桌面管理URl成功，桌面管理URl为：" + s['data'][0]['url'] + "\n"
                putlog.info(log)
                log = "[获取桌面管理URl CASE-EXPECT-TRUE] 测试: PASS。" + "\n"
                putlog.info(log)
            else:
                log = "[获取桌面管理URl CASE-EXPECT-TRUE] 测试: Failure。" + "\n"
                putlog.error(log)
        elif apivar['appname'] == "spoolermana":
            spoourl = xml.dom.minidom.parse(path).documentElement.getElementsByTagName("app")[4].getAttribute("url")
            if s['result'] == "success" and s['data'][0]['url'] == spoourl:
                log = wburl + "\n\n" + "获取数据管理URl成功，数据管理URl为：" + s['data'][0]['url'] + "\n"
                putlog.info(log)
                log = "[获取数据管理URl CASE-EXPECT-TRUE] 测试: PASS。" + "\n"
                putlog.info(log)
            else:
                log = "[获取数据管理URl CASE-EXPECT-TRUE] 测试: Failure。" + "\n"
                putlog.error(log)
        else:
            if s['result'] != "success":
                log = wburl + "\n\n" +  s['message'] + "\n"
                putlog.info(log)
                log = "[获取页面URl CASE-EXPECT-FALSE] 测试: PASS。" + "\n"
                putlog.info(log)
            else:
                log = "[获取页面管理URl CASE-EXPECT-FALSE] 测试: Failure。" + "\n"
                putlog.error(log)
    except:
        log = "unkown error. \n"
        putlog.error(log)    


###/* 下载文件  */###
def filedownload(apivar):
    try:
        url = apivar['apiurl'] + 'filedownload' 
        data = {'path': apivar['path'] ,'token': apivar['access_token']}
        r = requests.get(url, params=data)
        s = json.loads(r.text.encode("utf-8"))
        if s['result'] == "failed":
            log = r.url + "\n\n" +  s['message'] + "\n"
            putlog.info(log)
            log = "[下载文件 CASE-EXPECT-TRUE] 测试: PASS。" + "\n"
            putlog.info(log)
    except ValueError,e:
        if r.content.strip() == '':
            log = r.url + "\n\n文件 " + os.path.basename(apivar['path']) + " 成功下载，此文件内容为空。 \n"
            putlog.info(log)
            log = "[下载文件 CASE-EXPECT-FALSE] 测试: PASS。" + "\n"
            putlog.info(log)
        else:
            log = r.url + "\n\n文件 " + os.path.basename(apivar['path']) + " 成功下载，且文件内容不为空。 \n"
            putlog.info(log)
            log = "[下载文件 CASE-EXPECT-FALSE] 测试: PASS。" + "\n"
            putlog.info(log)
    except:
        log = "unkown error. \n"
        putlog.error(log)   


###/* 上传文件  */###
def fileuploadtool(apivar):
    try:
        cm = apivar['fileclient'] + 'fileclient -m ' + apivar['serverip'] + ' -p 6522 -u -l ' + apivar['local'] + ' -r ' + apivar['remote'] + ' -n ' +  apivar['access_token']
        sh = commands.getstatusoutput(cm)
        if apivar['expect'] == "true":
            if sh[0] == 0:
                log = os.path.basename(apivar['local']) + "文件 上传到 " + os.path.basename(apivar['remote']) + " " + sh[1] + "\n"
                putlog.info(log)
                log = "[上传文件 CASE-EXPECT-TRUE] 测试: PASS。"  + "\n"
                putlog.info(log)
            else:
                log = "[上传文件 CASE-EXPECT-TRUE] 测试: Failure。" + "\n"
                putlog.error(log)
        else:
            if sh[0] == 0:
                log = "[上传文件 CASE-EXPECT-FALSE] 测试: Failure。" + "\n"
                putlog.error(log)
            else:
                log = os.path.basename(apivar['local']) + "文件 上传到 " + os.path.basename(apivar['remote']) + " " + sh[1] + "\n"
                putlog.info(log)
                log = "[上传文件 CASE-EXPECT-FALSE] 测试: PASS。"  + "\n"
                putlog.info(log)
    except:
       log = "unkown error. \n"
       putlog.error(log)   


###/* 上传文件  */###
def fileupload(apivar):
    try:
        register_openers()
        datagen,headers = multipart_encode({"ServerPath":apivar['ServerPath'],
                                            "token":apivar['access_token'],
                                            "file":open(apivar['file'],"rb")})
        req = urllib2.Request(apivar['apiurl'] + "fileupload",datagen,headers)
        res = urllib2.urlopen(req).read()
        s = json.loads(res)
        if apivar['expect'] == "true":
            if s['result'] == "success":
                log = apivar['apiurl'] + "fileupload?ServerPath?" + apivar['ServerPath'] + "&token=" + apivar['access_token'] + s['message'] + "\n"
                putlog.info(log)
                log = os.path.basename(apivar['file']) + " 文件" + s['message'] + "\n"
                putlog.info(log)
                log = "[上传文件 CASE-EXPECT-TRUE] 测试: PASS。" + "\n"
                putlog.info(log)
            else:
                log = "[上传文件 CASE-EXPECT-TRUE] 测试: Failure。" + "\n"
                putlog.error(log)
        else:
            if s['result'] == "success":
                log = "[上传文件 CASE-EXPECT-FALSE] 测试: Failure。" + "\n"
                putlog.error(log)
            else:
                log = "[上传文件 CASE-EXPECT-FALSE] 测试: PASS。" + "\n"
                putlog.info(log)
    except IOError,e:
        log = "给定的文件不存在。"
        putlog.info(log)
    except NoneType,e:
        log = "未获得上传相关信息。"
        putlog.info(log)
    except:
        log = "unkown error.\n"
        putlog.error(log)  
