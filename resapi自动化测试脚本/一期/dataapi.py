#!/usr/bin/python
# -*- coding: UTF-8 -*-
#Date:25-14-2017
#Version=.1

import tool
import main
import time
import random
import sys
import os


default_encoding = 'utf-8'
if sys.getdefaultencoding() != default_encoding:
    reload(sys)
    sys.setdefaultencoding(default_encoding)


putlog = tool.putlog



# ###/* scope 作业。 */###
def datascope(apivar):
    try:
        dsurl = apivar['apiurl'] + "spoolers?token=" +  apivar['access_token']
        s = tool.geturl(dsurl)
        if s['result'] == "success":
            if len(s['data']) == len(apivar['datainfo']):
                log = ""
                for x in range(len(s['data'])):
                     log += str(x + 1) + " : " + s['data'][x]['dataPath'] + " , "
                log = dsurl + "\n\n" + "根据用户scope查询数据目录成功，查询到 " + str(len(s['data'])) + " 条数据目录，数据目录如下：" + "\n" + log + "\n"
                putlog.info(log)
                log = "[依据用户scope查询数据目录 CASE-EXPECT-TRUE]: 测试 PASS。" + "\n"
                putlog.info(log)
        else:
            log = ds + "\n\n" + s['message'] + "\n"
            putlog.info(log)
            log = "[依据用户scope查询数据目录 CASE-EXPECT-FALSE]: 测试 Failure。" + "\n"
            putlog.info(log)
    except:
        log = "unkown error. \n"
        putlog.error(log)


###/* 依据作业id查询数据目录。 */###
def searchidjobdir(apivar):
    try:
        drurl = apivar['apiurl'] + "spooler/" + apivar['jobid'] + "?token=" + apivar['access_token'] 
        s = tool.geturl(drurl)
        if apivar['expect'] == "true":
            if s['result'] == "success":
                if apivar['dataPath'] == s['data'][0]['dataPath'].encode('utf-8'):
                    log = drurl + "\n\n" + "根据作业id查询数据目录成功。数据目录是：" + s['data'][0]['dataPath'].encode('utf-8') + "\n"
                    putlog.info(log)
                    log = "[依据作业id查询数据目录 CASE-EXPECT-TRUE]: 测试 PASS。" + "\n"
                    putlog.info(log)
            else:
                log = "[依据作业id查询数据目录 CASE-EXPECT-TRUE]: 测试 Failure。" + "\n"
                putlog.info(log)
        else:
            if s['result'] == "success":
                log = "[依据作业id查询数据目录 CASE-EXPECT-FALSE]: 测试 Failure。" + "\n"
                putlog.info(log)
            else:
                log = drurl + "\n\n" + s['message'] + "\n"
                putlog.info(log)
                log = "[依据作业id查询数据目录 CASE-EXPECT-FALSE]: 测试 PASS。" + "\n"
                putlog.info(log)
    except:
        log = "unkown error. \n"
        putlog.error(log)


###/* 依据作业id列表查询数据目录。 */###
def searchidsjobdir(apivar):
    try:
        jobids =""
        for x in range(len(apivar['jobid']) -1 ):
            jobids += apivar['jobid'][x] + "," 
        jobids += apivar['jobid'][len(apivar['jobid']) -1]
        dsurl = apivar['apiurl'] + "spoolersbyid?ids=" + jobids + "&token=" + apivar['access_token'] 
        s = tool.geturl(dsurl)
        if apivar['expect'] == "true":
            if s['result'] == "success":
                dataPath = ""
                for x in range(len(s['data'])):
                    dataPath += str(x) + " : " + s['data'][x]['dataPath'] + " 。 "
                log = dsurl + "\n\n" + "根据作业id列表查询数据目录成功。数据目录是：" + dataPath + "\n"
                putlog.info(log)
                log = "[依据作业id查询数据目录 CASE-EXPECT-TRUE]: 测试 PASS。" + "\n"
                putlog.info(log)
            else:
                log = "[依据作业id列表查询数据目录 CASE-EXPECT-TRUE]: 测试 Failure。" + "\n"
                putlog.info(log)
        else:
            if s['result'] == "success":
                log = "[依据作业id列表查询数据目录 CASE-EXPECT-FALSE]: 测试 Failure。" + "\n"
                putlog.info(log)
            else:
                log = dsurl + "\n\n" + s['message'] + "\n"
                putlog.info(log)
                log = "[依据作业id列表查询数据目录 CASE-EXPECT-FALSE]: 测试 PASS。" + "\n"
                putlog.info(log)
    except:
        log = "unkown error. \n"
        putlog.error(log)


###/* 依据数据目录名称查询数据目录列表。 */###
def spoolersbyname(apivar):
    try:
        name = os.path.basename(apivar['dataPath'])
        snurl = apivar['apiurl'] + "spoolersbyname?name=" + name + "&token=" + apivar['access_token']
        s = tool.geturl(snurl)
        if apivar['expect'] == "true":
            if s['result'] == "success": 
                log = snurl + "\n\n" + "根据数据目录名称查询数据目录成功。数据目录是：" + s['data'][0]['dataPath'] + "\n"
                putlog.info(log)
                log = "[依据数据目录名称查询数据目录 CASE-EXPECT-TRUE]: 测试 PASS。" + "\n"
                putlog.info(log)
            else:
                log = "[依据数据目录名称查询数据目录 CASE-EXPECT-TRUE]: 测试 Failure。" + "\n"
                putlog.info(log)
        else:
            if s['result'] == "success":
                    log = "[依据数据目录名称查询数据目录 CASE-EXPECT-FALSE]: 测试 Failure。" + "\n"
                    putlog.info(log)
            else:
                log = snurl + "\n\n" + s['message'] + "\n"
                putlog.info(log)
                log = "[依据数据目录名称查询数据目录 CASE-EXPECT-FALSE]: 测试 PASS。" + "\n"
                putlog.info(log)
    except:
        log = "unkown error. \n"
        putlog.error(log)



###/* 立即删除数据目录。 */###
def imdeldir(apivar):
    try:
        deurl = apivar['apiurl'] + "/spooler/del/" + apivar['jobid'] + "?token=" + apivar['access_token']
        s = tool.geturl(deurl)
        if apivar['expect'] == "true":
            if s['result'] == "success": 
                if tool.operatepsql(apivar):
                    log = "[立即删除数据目录 CASE-EXPECT-TRUE]: 测试 Failure。" + "\n"
                    putlog.info(log)
                else:
                    log = deurl + "\n\n" + os.path.basename(apivar['dataPath']) + "数据目录删除成功。" + "\n"
                    putlog.info(log)
                    log = "[立即删除数据目录 CASE-EXPECT-TRUE]: 测试 PASS。" + "\n"
                    putlog.info(log)
        else:
            if s['result'] == "success": 
                log = "[立即删除数据目录 CASE-EXPECT-FALSE]: 测试 Failure。" + "\n"
                putlog.info(log)
            else:
                log = deurl + "\n\n" + s['message'] + "\n"
                putlog.info(log)
                log = "[立即删除数据目录 CASE-EXPECT-FALSE]: 测试 PASS。" + "\n"
                putlog.info(log)
    except:
        log = "unkown error. \n"
        putlog.error(log)


###/* 过期删除数据目 */###
def  expiredeldir(apivar):
    try:
        exurl = apivar['apiurl'] + "/spooler/purge?id=" + apivar['jobid'] + "&expiration_time=" + apivar['expiration_time'] + "&token=" + apivar['access_token']
        s = tool.geturl(exurl)
        if apivar['expect'] == "true":
            if s['result'] == "success": 
                if tool.operatepsql(apivar):
                    log = exurl + "\n\n" + apivar['expiration_time'] + " 号将删除数据目录。" + "\n"
                    putlog.info(log)
                    log = "[过期删除数据目录 CASE-EXPECT-TRUE]: 测试 PASS。" + "\n"
                    putlog.info(log)
            else:
                putlog.info(s)
                putlog.info(exurl)
                log = "[过期删除数据目录 CASE-EXPECT-TRUE]: 测试 Failure。" + "\n"
                putlog.info(log)
        else:
            if s['result'] == "success": 
                    log = "[过期删除数据目录 CASE-EXPECT-FALSE]: 测试 Failure。" + "\n"
                    putlog.info(log)
            else:
                log = exurl + "\n\n" + s['message'] + "\n"
                putlog.info(log)
                log = "[过期删除数据目录 CASE-EXPECT-FALSE]: 测试 PASS。" + "\n"
                putlog.info(log)
    except:
       log = "unkown error. \n"
       putlog.error(log)
