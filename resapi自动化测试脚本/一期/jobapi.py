#!/usr/bin/python
# -*- coding: UTF-8 -*-
#Date:25-14-2017
#Version=.1


import tool
import main
import time
import random
import sys


default_encoding = 'utf-8'
if sys.getdefaultencoding() != default_encoding:
    reload(sys)
    sys.setdefaultencoding(default_encoding)


putlog = tool.putlog


###/* loging appform , success ? retuen token : failed.  */###
def login(apivar):
    try:
        lgurl = apivar['apiurl'] + "login?username="  + apivar['username'] + "&password=" + apivar['password']
        s = tool.geturl(lgurl)
        if apivar['expect'] == "true":
            if s["result"] == "success":
                access_token = s["data"][0]["token"]
                log = lgurl + " appform 登录成功. \n\n成功获取token值为: " + access_token + "\n"
                putlog.info(log)
                log = "[用户登录 CASE-EXPECT-TRUE] 测试: PASS。" + "\n"
                putlog.info(log)
                return s["data"][0]["token"]
            else:
                log = lgurl + " appform login failed. \n" + s["message"] + "\n"
                putlog.info(log)
                log = "[用户登录 CASE-EXPECT-TRUE] 测试: FAILURE。" + "\n"
                putlog.error(log)
        else:
            if s["result"] == "success":
                log = "[用户登录 CASE-EXPECT-FALSE] 测试: Failure。" + "\n"
                putlog.error(log)
            else:
                log = lgurl + " appform login failed." + s["message"] + "\n"
                putlog.info(log)
                log = "[用户登录 CASE-EXPECT-FALSE] 测试: PASS。" + "\n"
                putlog.info(log)
    except KeyError,e:
        log = "apivar key值已被破坏，URL错误。无法登录appform。\n"
        putlog.error(log)
    except:
        log = "unkown error. \n"
        putlog.error(log)
        

###/* ping check whether the connection is available  */### 
def checkping(apivar,pl="true"):
    try:
        ckurl = apivar['apiurl'] + "ping?token=" + apivar['access_token'] 
        s = tool.geturl(ckurl)
        if apivar['expect'] == "true":
            if s["result"] == "success":
                if pl == "true":
                    log = ckurl + " 连接正常，appform 可以正常使用。\n"
                    putlog.info(log)
                    log = "[ping 资源 CASE-EXPECT-TRUE] 测试: PASS。" + "\n"
                    putlog.info(log)
            else:
                if pl == "true":
                    log = ckurl + " 连接失败，appform 无法正常使用。 \n"
                    putlog.info(log)
                    log = "[ping 资源 CASE-EXPECT-TRUE] 测试: Failure。" + "\n"
                    putlog.error(log)
        else:
            if s["result"] == "success":
                if pl == "true":
                    log = ckurl + " 连接正常，appform 可以正常使用。\n"
                    putlog.info(log)
                    log = "[ping 资源 CASE-EXPECT-FALSE] 测试: Failure。" + "\n"
                    putlog.error(log)
            else:
                if pl == "true":
                    log = ckurl + " 连接失败，appform 无法正常使用。 \n"
                    putlog.info(log)
                    log = "[ping 资源 CASE-EXPECT-FALSE] 测试: PASS。" + "\n"
                    putlog.info(log)
    except TypeError,e:
        log = "没能正确传入token值。\n"
        putlog.error(log)
    except:
        log = "unkown error. \n"
        putlog.error(log)


###/* logout appform */###
def logout(apivar):
    try:
        lourl = apivar['apiurl'] + "logout?token=" + apivar['access_token'] 
        s = tool.geturl(lourl)
        if apivar['expect'] == "true":
            if s['result'] == "success":
                log = lourl + " appform 注销成功。" + "\n"
                putlog.info(log)
                log = "[用户注销 CASE-EXPECT-TRUE] 测试: PASS。" + "\n"
                putlog.info(log)
            else:
                log = lourl + " appform 注销失败。" + s['message'] + "\n"
                putlog.info(log)
                log = "[用户注销 CASE-EXPECT-TRUE] 测试: FAILURE。" + "\n"
                putlog.error(log)
        else:
            if s['result'] == "success":
                log = lourl + " appform 注销成功。" + "\n"
                putlog.info(log)
                log = "[用户注销 CASE-EXPECT-FALSE] 测试: Failure。" + "\n"
                putlog.error(log)
            else:
                log = lourl + " appform 注销失败。" + s['message'] + "\n"
                putlog.info(log)
                log = "[用户注销 CASE-EXPECT-FALSE]: 测试 PASS。" + "\n"
                putlog.info(log)
    except TypeError,e:
        log = "没有正确传入token值。\n"
        putlog.info(log)
    except:
        log = "unkown error. \n"
        putlog.error(log)
  

###/* Submit Fluent Job  */###
def submitfluentjob(apivar):
    try:
        jfurl = apivar['apiurl'] + 'jsub?appid=fluent&params={"JH_CAS":"' + apivar['casfile'] + '","JH_RELEASE":"' + \
        apivar['relese'] + '","JH_GUI_ENABLED":"' + apivar['gui'] + '","JH_NCPU":"' + apivar['ncpu'] + \
        '","JH_PROJECT":"test","JH_JOB_NAME":"fluentest' + apivar['times'] + '"}&token=' + apivar['access_token']
        s = tool.geturl(jfurl)
        if apivar['expect'] == "true":
            if s["result"] == "success":
                jobid = str(s["data"][0]["jobid"])
                log = jfurl + "\n\nfluent 作业提交成功。作业号是: " + jobid + "\n"
                putlog.info(log)
                log = "[提交fluent作业 CASE-EXPECT-TRUE]: 测试 PASS。" + "\n"
                putlog.info(log)
                return jobid
            else:
                log = jfurl + "\n\nfluen 作业提交失败, " + s["message"] + "\n"
                putlog.info(log)
                log = "[提交fluent作业 	CASE-EXPECT-TRUE] 测试: Failure。" + "\n"
                putlog.error(log)
        else:
            if s["result"] == "success":
                log = "[提交fluent作业 CASE-EXPECT-FALSE] 测试: Failure。" + "\n"
                putlog.error(log)
            else:
                log = jfurl + "\n\nfluen 作业提交失败, " + s["message"] + "\n"
                putlog.info(log)
                log = "[提交fluent作业 CASE-EXPECT-FALSE]: 测试 PASS。" + "\n"
                putlog.info(log)
    except TypeError,e:
        log = "参数值传入不正确。\n"
        putlog.error(log)
    except:
        log = "unkown error. \n"
        putlog.error(log)


###/* 依据状态查询作业。 */###
def searchstatejob(apivar):
    try:
        sturl = apivar['apiurl'] + "jobsbystatus/" + apivar['status'] + "?token=" + apivar['access_token'] 
        s = tool.geturl(sturl)
        if s["result"] == "success":
            log = sturl + "\n\n" + apivar['status'] + " 状态的作业有 :" + str(len(s["data"])) + "\n"
            putlog.info(log)
            log = "[依据作业查询作业 CASE-EXPECT-TRUE] 测试: PASS。" + "\n"
            putlog.info(log)
        else:
            if int(tool.statjobnum(apivar)) > 0:
                log = "[依据状态查询作业 CASE-EXPECT-TRUE] 测试: FAILURE。" + "\n"
                putlog.info(log)
            else:
                log = sturl + "\n\n没有 " + apivar['status'] + "状态的作业。" + "\n"
                putlog.info(log)
                log = "[依据作业查询作业 CASE-EXPECT-TRUE] 测试: PASS。" + "\n"
                putlog.info(log)
    except:
        log = "unkown error. \n"
        putlog.error(log)


###/* 依据作业id查询作业信息。*/###
def searchIdjob(apivar,index=0,pl="true"):
    try:
        jobid = apivar['jobs'][index]
        jdurl = apivar['apiurl'] + "job/" + jobid + "?token=" + apivar['access_token'] 
        s = tool.geturl(jdurl)
        log = jdurl + "\n\njob id : " + jobid + " 信息查询成功。信息如下 : \n\n"
        if apivar['expect'] == "true":
            if s["result"] == "success":
                for k in s["data"][0].keys():
                    if not str(s["data"][0][k]):
                        pass
                    else:
                        log += k + " : " + str(s["data"][0][k]) + " "
                if pl == "true":
                    log += "\n"
                    putlog.info(log)
                    log = "[依据作业id查询作业信息 CASE-EXPECT-TRUE]: 测试 PASS。" + "\n"
                    putlog.info(log)
                return s["data"][0]["status"],s["data"][0]["id"],s["data"][0]["name"]
            else:
                log = jdurl + "\n\n没有查到此作业相关信息, " + s["message"] + "\n"
                if pl == "true":
                    putlog.info(log)
                    log = "[依据作业id查询作业信息 CASE-EXPECT-TRUE] 测试: Failure。" + "\n"
                    putlog.error(log)
        else:
            if s["result"] == "success":
                log = "[依据作业id查询作业信息 CASE-EXPECT-FALSE]: 测试 Failure。" + "\n"
                putlog.error(log)
            else:
                log = jdurl + "\n\n没有查到此作业相关信息, " + s["message"] + "\n"
                if pl == "true":
                    putlog.info(log)
                    log = "[依据作业id查询作业信息 CASE-EXPECT-FALSE] 测试: PASS。" + "\n"
                    putlog.info(log)
    except:
        log = "unkown error. \n"
        putlog.error(log)


###/* Stop 单个作业。 */###
# RUN stop USUSP, PEND stop PSUSP, EXIT DOEN .[RUN,USUSP,PEND,PSUSP,DONE,EXIT]
def stopjob(apivar):
    try:
        for x in range(len(apivar['jobs'])):
            sturl = apivar['apiurl'] + "job/stop/" + apivar['jobs'][x] + "?token=" + apivar['access_token'] + "\n"
            putlog.info("case 8-" + str(x + 1) +" test start ...\n")
            log = "当前要 stop 的作业号是："+ searchIdjob(apivar,x,pl="0")[1] + " 作业状态是：" + searchIdjob(apivar,x,pl="0")[0] + "\n"
            putlog.info(log)
            
            if searchIdjob(apivar,x,pl="0")[0] == "EXIT" or searchIdjob(apivar,x,pl="0")[0] == "DONE" \
            or searchIdjob(apivar,x,pl="0")[0] == "PSUSP" or searchIdjob(apivar,x,pl="0")[0] == "USUSP":
                s = tool.geturl(sturl)
                if s["result"] == "success":
                    time.sleep(3)
                    log = sturl + "\n作业 stop 成功，stop 后状态为：" + searchIdjob(apivar,x,pl="0")[0] + "\n"
                    putlog.info(log)
                    log = "[stop作业信息 CASE-EXPECT-TRUE]: 测试 Failure。" + "\n"
                    putlog.error(log)
                    putlog.info("case 8-" + str(x + 1) +" test end ...\n")
                else:
                    log = sturl
                    putlog.info(log)
                    log = "作业 stop 失败，" + s["message"] + "\n"
                    putlog.info(log)
                    log = "[stop作业信息 CASE-EXPECT-TRUE] 测试: PASS。" + "\n"
                    putlog.info(log)
                    putlog.info("case 8-" + str(x + 1) +" test end ...\n")
            else:
                s = tool.geturl(sturl)
                if s["result"] == "success":
                    time.sleep(3)
                    log = sturl + "\n作业 stop 成功，stop 后状态为：" + searchIdjob(apivar,x,pl="0")[0] + "\n"
                    putlog.info(log)
                    log = "[stop作业信息 CASE-EXPECT-FALSE] 测试: PASS。" + "\n"
                    putlog.info(log)
                    putlog.info("case 8-" + str(x + 1) +" test end ...\n")
                else:
                    log = sturl
                    putlog.info(log)
                    log = "作业 stop 失败，" + s["message"] + "\n"
                    putlog.error(log)
                    log = "[stop作业信息 CASE-EXPECT-FALSE]: 测试 Failure。" + "\n"
                    putlog.error(log)
                    putlog.info("case 8-" + str(x + 1) +" test end ...\n")
    except:
        log = "unkown error. \n"
        putlog.error(log)       
    

# ###/* resume 单个作业。 */###
def resumejob(apivar):
    try:
        for x in range(len(apivar['jobs'])):
            reurl = apivar['apiurl'] + "job/resume/" + apivar['jobs'][x] + "?token=" + apivar['access_token']
            putlog.info("case 9-" + str(x + 1) +" test start ...\n")
            log = "当前要 resume 的作业号是："+ searchIdjob(apivar,x,pl="0")[1] + " 作业状态是：" + searchIdjob(apivar,x,pl="0")[0] + "\n"
            putlog.info(log) 
            if searchIdjob(apivar,x,pl="0")[0] == "RUN" or searchIdjob(apivar,x,pl="0")[0] == "PEND" or searchIdjob(apivar,x,pl="0")[0] == "DONE" or searchIdjob(apivar,x,pl="0")[0] == "EXIT":
                s = tool.geturl(reurl)
                if s["result"] == "success":
                    log = "[resume作业信息 CASE-EXPECT-TRUE]: 测试 Failure。" + "\n"
                    putlog.error(log)
                    putlog.info("case 9-" + str(x + 1) +" test end ...\n")
                else:
                    log = reurl + "\n"
                    putlog.info(log)
                    log = "作业 resume 失败，" + s["message"] + "\n"
                    putlog.info(log)
                    log = "[resume作业信息 CASE-EXPECT-TRUE] 测试: PASS。" + "\n"
                    putlog.info(log)
                    putlog.info("case 9-" + str(x + 1) +" test end ...\n")
            else:
                s = tool.geturl(reurl)
                if s["result"] == "success":
                    time.sleep(3)
                    log = reurl + "\n\n作业 resume 成功，resume 后状态为：" + searchIdjob(apivar,x,pl="0")[0] + "\n"
                    putlog.info(log)
                    log = "[resume作业信息 CASE-EXPECT-FALSE] 测试: PASS。" + "\n"
                    putlog.info(log)
                    putlog.info("case 9-" + str(x + 1) +" test end ...\n")
                else:
                    log = reurl + "\n"
                    putlog.info(log)
                    log = "作业 resume 失败，" + s["message"] + "\n"
                    putlog.error(log)
                    log = "[resume作业信息 CASE-EXPECT-FALSE]: 测试 Failure。" + "\n"
                    putlog.error(log)
                    putlog.info("case 9-" + str(x + 1) +" test end ...\n")
    except:
        log = "unkown error. \n"
        putlog.error(log)   


# ###/* kill 单个作业。 */###
def killjob(apivar):
    try:
        for x in range(len(apivar['jobs'])):
            putlog.info("case 10-" + str(x + 1) +" test start ...\n")
            log = "当前要 kill 作业号是："+ searchIdjob(apivar,x,pl="0")[1] + " 作业状态是：" + searchIdjob(apivar,x,pl="0")[0] + "\n"
            putlog.info(log)
            kiurl = apivar['apiurl'] + "job/kill/" + apivar['jobs'][x] + "?token=" + apivar['access_token'] 
            if searchIdjob(apivar,x,pl="0")[0] == "EXIT" or searchIdjob(apivar,x,pl="0")[0] == "DONE":
                s = tool.geturl(kiurl)
                if s["result"] == "success":
                    time.sleep(3)
                    log = kiurl + "\n\n作业 kill 成功，kill 后状态为：" + searchIdjob(apivar,x,pl="0")[0] + "\n"
                    putlog.info(log)
                    log = "[kill作业信息 CASE-EXPECT-TRUE]: 测试 Failure。" + "\n"
                    putlog.error(log)
                    putlog.info("case 10-" + str(x + 1) +" test end ...\n")
                else:
                    log = kiurl + "\n"
                    putlog.info(log)
                    log = "作业 kill 失败，" + s["message"] + "\n"
                    putlog.info(log)
                    log = "[kill作业信息 CASE-EXPECT-TRUE] 测试: PASS。" + "\n"
                    putlog.info(log)
                    putlog.info("case 10-" + str(x + 1) +" test end ...\n")
            else:
                s = tool.geturl(kiurl)
                if s["result"] == "success":
                    time.sleep(3)
                    log = kiurl + "\n\n作业 kill 成功，kill 后状态为：" + searchIdjob(apivar,x,pl="0")[0] + "\n"
                    putlog.info(log)
                    log = "[kill作业信息 CASE-EXPECT-FALSE] 测试: PASS。" + "\n"
                    putlog.info(log)
                    putlog.info("case 10-" + str(x + 1) +" test end ...\n")
                else:
                    log = kiurl + "\n"
                    putlog.info(log)
                    log = "作业 kill 失败，" + s["message"] + "\n"
                    putlog.info(log)
                    log = "[kill作业信息 CASE-EXPECT-FALSE] 测试: Failure。" + "\n"
                    putlog.error(log)
                    putlog.info("case 10-" + str(x + 1) +" test end ...\n")
    except:
        log = "unkown error. \n"
        putlog.error(log)


# ###/* peek 单个作业。 */###
def peekjob(apivar):
    try:
        for x in range(len(apivar['jobs'])):
                putlog.info("case 11-" + str(x + 1) +" test start ...\n")
                log = "当前要 peek 作业号是："+ searchIdjob(apivar,x,pl="0")[1] + " 作业状态是：" + searchIdjob(apivar,x,pl="0")[0] + "\n"
                putlog.info(log)
                pkurl = apivar['apiurl'] + "job/peek/" + apivar['jobs'][x] + "?token=" + apivar['access_token'] 
                if searchIdjob(apivar,x,pl="0")[0] == "RUN" or searchIdjob(apivar,x,pl="0")[0] == "USUSP":
                    s = tool.geturl(pkurl)
                    if s["result"] == "success":
                        log = pkurl + "\n\n作业 peek 成功 " + s["message"]  + "\n"
                        putlog.info(log)
                        log = "[peek作业信息 CASE-EXPECT-TRUE]: 测试 PASS。" + "\n"
                        putlog.info(log)
                        putlog.info("case 11-" + str(x + 1) +" test end ...\n")
                    else:
                        log = pkurl + "\n"
                        putlog.info(log)
                        log = "作业 peek 失败，" + s["message"] + "\n"
                        putlog.info(log)
                        log = "[kill作业信息 CASE-EXPECT-TRUE] 测试: Failure。" + "\n"
                        putlog.info(log)
                        putlog.error("case 11-" + str(x + 1) +" test end ...\n")                
                else:
                    s = tool.geturl(pkurl)
                    if s["result"] == "success":
                        log = "[kill作业信息 CASE-EXPECT-FALSE] 测试: Failure。" + "\n"
                        putlog.info(log)
                        putlog.error("case 11-" + str(x + 1) +" test end ...\n") 
                    else:
                        log = pkurl + "\n\n作业 peek 成功" + s["message"] + "\n" 
                        putlog.info(log)
                        log = "[peek作业信息 CASE-EXPECT-FALSE]: 测试 PASS。" + "\n"
                        putlog.info(log)
                        putlog.info("case 11-" + str(x + 1) +" test end ...\n") 
    except:
        log = "unkown error. \n"
        putlog.error(log)


# ###/* top 单个作业。 */###
def topjob(apivar):
    try:
        for x in range(len(apivar['jobs'])):
            putlog.info("case 12-" + str(x + 1) +" test start ...\n")
            log = "当前要 top 作业号是："+ searchIdjob(apivar,x,pl="0")[1] + " 作业状态是：" + searchIdjob(apivar,x,pl="0")[0] + "\n"
            putlog.info(log)
            tpurl = apivar['apiurl'] + "job/top/" + apivar['jobs'][x] + "?token=" + apivar['access_token'] 
            if searchIdjob(apivar,x,pl="0")[0] == "PEND" or searchIdjob(apivar,x,pl="0")[0] == "PSUSP":
                s = tool.geturl(tpurl)
                if s["result"] == "success":
                    log = tpurl + "\n\n作业 top 成功\n"
                    putlog.info(log)
                    log = "[top作业信息 CASE-EXPECT-TRUE]: 测试 PASS。" + "\n"
                    putlog.info(log)
                    putlog.info("case 12-" + str(x + 1) +" test end ...\n")
                else:
                    log = tpurl + "\n"
                    putlog.info(log)
                    log = "作业 top 失败，" + s["message"] + "\n"
                    putlog.info(log)
                    log = "[top作业信息 CASE-EXPECT-TRUE] 测试: Failure。" + "\n"
                    putlog.info(log)
                    putlog.error("case 12-" + str(x + 1) +" test end ...\n") 
            else:
                s = tool.geturl(tpurl)
                if s["result"] == "success":
                    log = "[top作业信息 CASE-EXPECT-FALSE] 测试: Failure。" + "\n"
                    putlog.info(log)
                    putlog.error("case 12-" + str(x + 1) +" test end ...\n") 
                else:
                    log = tpurl + "\n\n作业 top 成功" + s["message"] + "\n" 
                    putlog.info(log)
                    log = "[top作业信息 CASE-EXPECT-FALSE]: 测试 PASS。" + "\n"
                    putlog.info(log)
                    putlog.info("case 12-" + str(x + 1) +" test end ...\n") 
    except:
        log = "unkown error. \n"
        putlog.error(log)


# ###/* bot 单个作业。 */###
def botjob(apivar):
    try:
        for x in range(len(apivar['jobs'])):
            putlog.info("case 13-" + str(x + 1) +" test start ...\n")
            log = "当前要 bot 作业号是："+ searchIdjob(apivar,x,pl="0")[1] + " 作业状态是：" + searchIdjob(apivar,x,pl="0")[0] + "\n"
            putlog.info(log)
            bturl = apivar['apiurl'] + "job/bot/" + apivar['jobs'][x] + "?token=" + apivar['access_token'] 
            if searchIdjob(apivar,x,pl="0")[0] == "PEND" or searchIdjob(apivar,x,pl="0")[0] == "PSUSP":
                s = tool.geturl(bturl)
                if s["result"] == "success":
                    log = bturl + "\n\n作业 top 成功\n"
                    putlog.info(log)
                    log = "[bot作业信息 CASE-EXPECT-TRUE]: 测试 PASS。" + "\n"
                    putlog.info(log)
                    putlog.info("case 13-" + str(x + 1) +" test end ...\n")
                else:
                    log = bturl + "\n"
                    putlog.info(log)
                    log = "作业 bot 失败，" + s["message"] + "\n"
                    putlog.info(log)
                    log = "[top作业信息 CASE-EXPECT-TRUE] 测试: Failure。" + "\n"
                    putlog.info(log)
                    putlog.error("case 13-" + str(x + 1) +" test end ...\n") 
            else:
                s = tool.geturl(bturl)
                if s["result"] == "success":
                    log = "[top作业信息 CASE-EXPECT-FALSE] 测试: Failure。" + "\n"
                    putlog.info(log)
                    putlog.error("case 13-" + str(x + 1) +" test end ...\n") 
                else:
                    log = bturl + "\n\n作业 bot 成功" + s["message"] + "\n" 
                    putlog.info(log)
                    log = "[top作业信息 CASE-EXPECT-FALSE]: 测试 PASS。" + "\n"
                    putlog.info(log)
                    putlog.info("case 13-" + str(x + 1) +" test end ...\n")
    except:
        log = "unkown error. \n"
        putlog.error(log)


# ###/* scope 作业。 */###
def jobscope(apivar):
    #try:
        scurl = apivar['apiurl'] + "jobs?token=" + apivar['access_token']
        s = tool.geturl(scurl)
        if s["result"] == "success":
            cl = int(tool.queryjobnum(apivar))
            al = len(s["data"])
            if cl == al:
                log = scurl + "\n\n根据scope查询作业个数成功。总共作业个数为：" + str(cl)  +  "\n"
                putlog.info(log)
                log = "[根据用户scope查询作业 CASE-EXPECT-TRUE] 测试: PASS。" + "\n"
                putlog.info(log)
            else:
                log = scurl + "\n\n根据scope查询作业个数不正确。" +  "\n"
                putlog.info(log)
                log = "[根据用户scope查询作业 CASE-EXPECT-TRUE] 测试: Failure。" + "\n"
                putlog.info(log)
        else:
            log = scurl + "\n\n根据scope查询作业个数失败。" +  "\n"
            putlog.info(log)
            log = "[根据用户scope查询作业 CASE-EXPECT-FALSE] 测试: Failure。" + "\n"
            putlog.info(log) 
    #except:
     #   log = "unkown error. \n"
      #  putlog.error(log)


###/* 依据作业id list 查询作业信息。*/###
def searchIdlistjob(apivar):
    try:
        jobs = ""
        for x in range(len(apivar['jobs']) - 1):
            jobs += apivar['jobs'][x] + ","
        jobs += apivar['jobs'][len(apivar['jobs']) - 1]
        ilurl = apivar['apiurl'] + "jobsbyid?id=" + jobs + "&token=" + apivar['access_token'] 
        s = tool.geturl(ilurl)
        if apivar['expect'] == "true":
            if s["result"] == "success":
                log = ilurl + "\n\njob id : " + jobs + " 信息查询成功。信息如下 : \n\n"
                putlog.info(log)
                log = ""
                for l in range(len(s["data"])):
                    for k in s["data"][l].keys():
                        if not str(s["data"][l][k]):
                            pass
                        else:
                            log += k + " : " + str(s["data"][l][k]) + " "
                log += "\n"
                putlog.info(log)
                log = "[依据作业id列表查询作业信息 CASE-EXPECT-TRUE]: 测试 PASS。" + "\n"
                putlog.info(log)
            else:
                log = ilurl + s["message"] + "\n"
                putlog.info(log)
                log = "[依据作业id列表查询作业信息 CASE-EXPECT-TRUE] 测试: Failure。" + "\n"
                putlog.error(log)
        else:
            if s["result"] == "success":
                log = "[依据作业id列表查询作业信息 CASE-EXPECT-FALSE] 测试: Failure。" + "\n"
                putlog.error(log)
            else:
                log = ilurl +  s["message"] + "\n"
                putlog.info(log)
                log = "[依据作业id列表查询作业信息 CASE-EXPECT-FALSE] 测试: PASS。" + "\n"
                putlog.info(log)
    except:
        log = "unkown error. \n"
        putlog.error(log)


###/* 依据作业名称查询作业信息。*/###
def searchnamejob(apivar):
    try:
        neurl = apivar['apiurl'] + "jobsbyname?name=" + apivar['jobsbyname'] + "&token=" + apivar['access_token'] 
        s = tool.geturl(neurl)
        if apivar['expect'] == "true":
            if s["result"] == "success":
                log = neurl + "\n\njob name : " + apivar['jobsbyname'] + " 信息查询成功。信息如下 : \n"
                putlog.info(log)
                log = ""
                for k in s["data"][0].keys():
                    if not str(s["data"][0][k]):
                        pass
                    else:
                        log += k + " : " + str(s["data"][0][k]) + " "
                log += "\n"
                putlog.info(log)
                log = "[依据作业名称查询作业信息 CASE-EXPECT-TRUE]: 测试 PASS。" + "\n"
                putlog.info(log)
            else:
                log = neurl + "\n\n没有查到此作业相关信息, " + s["message"] + "\n"
                putlog.info(log)
                log = "[依据作业名称查询作业信息 CASE-EXPECT-TRUE] 测试: Failure。" + "\n"
                putlog.error(log)
        else:
            if s["result"] == "success":
                log = "[依据作业名称查询作业信息 CASE-EXPECT-FALSE] 测试: Failure。" + "\n"
                putlog.error(log)
            else:
                log = neurl +  s["message"] + "\n"
                putlog.info(log)
                log = "[依据作业名称查询作业信息 CASE-EXPECT-FALSE] 测试: PASS。" + "\n"
                putlog.info(log)
    except:
        log = "unkown error. \n"
        putlog.error(log)


###/* 依据作业号查询作业历史信息。*/###
def searchhistjob(apivar,index=0):
    try:
        jobid = apivar['jobs'][index]
        hiurl = apivar['apiurl'] + "job/hist/" + jobid + "?token=" + apivar['access_token'] 
        s = tool.geturl(hiurl)
        if apivar['expect'] == "true":
            if s["result"] == "success":
                log = hiurl + "\n\njob id : " + jobid + " 历史信息查询成功。信息如下 : \n"
                putlog.info(log)
                log = s["data"][0]["jobhistory"] + "\n"
                putlog.info(log)
                log = "[依据作业id查询作业历史信息 CASE-EXPECT-TRUE]: 测试 PASS。" + "\n"
                putlog.info(log)
            else:
                log = hiurl + "\n\n没有查到此作业相关关历史信息, " + s["message"] + "\n"
                putlog.info(log)
                log = "[依据作业id查询作业历史信息 CASE-EXPECT-TRUE] 测试: Failure。" + "\n"
                putlog.error(log)
        else:
            if s["result"] == "success":
                log = "[依据作业id查询作业历史信息 CASE-EXPECT-FALSE] 测试: Failure。" + "\n"
                putlog.error(log)
            else:
                log = hiurl + s["message"] + "\n"
                putlog.info(log)
                log = "[依据作业id查询作业历史信息 CASE-EXPECT-FALSE] 测试: PASS。" + "\n"
                putlog.info(log)
    except:
        log = "unkown error. \n"
        putlog.error(log)


###/* 依据作业id列表查询作业历史信息。*/###
def searchhistjobs(apivar,index=0):
    jobs = ""
    for x in range(len(apivar['jobs']) - 1):
        jobs += apivar['jobs'][x] + ","
    jobs += apivar['jobs'][len(apivar['jobs']) - 1]
    hsurl = apivar['apiurl'] + "jobs/hist?id=" + jobs + "&token=" + apivar['access_token'] 
    s = tool.geturl(hsurl)
    if apivar['expect'] == "true":
        if s["result"] == "success":
            log = hsurl + "\n\njob id : " + jobs + " 历史信息查询成功。信息如下 : \n"
            putlog.info(log)
            log = "\n"
            for l in range(len(s["data"])):
                log += s["data"][l]["jobhistory"][0:135] + "\n"
            putlog.info(log)
            log = "[依据作业id列表查询作业历史信息 CASE-EXPECT-TRUE]: 测试 PASS。" + "\n"
            putlog.info(log)
        else:
            log = hsurl + "\n\n没有查到此作业相关关历史信息, " + s["message"] + "\n"
            putlog.info(log)
            log = "[依据作业id列表查询作业历史信息 CASE-EXPECT-TRUE] 测试: Failure。" + "\n"
            putlog.error(log)
    else:
        if s["result"] == "success":
            log = "[依据作业id列表查询作业历史信息 CASE-EXPECT-FALSE] 测试: Failure。" + "\n"
            putlog.error(log)
        else:
            log = hsurl + s["message"] + "\n"
            putlog.info(log)
            log = "[依据作业id列表查询作业历史信息 CASE-EXPECT-FALSE] 测试: PASS。" + "\n"
            putlog.info(log)


###/* 依据作业id查询作业数据文件。*/###
def searchflistjob(apivar,index=0):
    jobid = apivar['jobs'][index]
    fturl = apivar['apiurl'] + "jobs/flistbyid/" + jobid + "?token=" + apivar['access_token'] 
    s = tool.geturl(fturl)
    if apivar['expect'] == "true":
        if s['result'] == "success":
            log = fturl + "\n\njob id : " + jobid + " 信息查询成功。信息如下 : \n\n"
            for x in range(len(s['data'])):
                log += s["data"][x]["fileName"] + " "
            log += "\n"
            putlog.info(log)
            log = "[依据作业id查询作业数据文件 CASE-EXPECT-TRUE]: 测试 PASS。" + "\n"
            putlog.info(log)
        else:
            log = fturl + s["message"] + "\n"
            putlog.info(log)
            log = "[依据作业id查询作业数据文件 CASE-EXPECT-TRUE] 测试: Failure。" + "\n"
            putlog.error(log)
    else:
        if s['result'] == "success":
            log = "[依据作业id查询作业数据文件 CASE-EXPECT-TRUE] 测试: Failure。" + "\n"
            putlog.error(log)
        else:
            log = fturl  + s["message"] + "\n"
            putlog.info(log)
            log = "[依据作业id查询作业数据文件 CASE-EXPECT-FALSE] 测试: PASS。" + "\n"
            putlog.info(log)


###/* 依据作业ids kill 作业。*/###
def  killjobs(apivar):
    try:
        for x in range(len(apivar['jobs'])):
            putlog.info("case 15-" + str(x + 1) +" test start ...\n")
            log = "当前要 kill 作业号是：" + str(apivar['jobs'][x][0]) + " 作业状态是：" + apivar['jobs'][x][1] + "\n"
            putlog.info(log)
            jobs = ""
            for y in range(len(apivar['jobs'][x][0])):
                jobs += apivar['jobs'][x][0][y] + ","
            ksurl = apivar['apiurl'] + "jobs/kill?id=" + str(jobs) + "&token=" + apivar['access_token'] 
            if apivar['jobs'][x][1] == "EXIT" or apivar['jobs'][x][1] == "DONE":
                s = tool.geturl(ksurl)
                if s["result"] == "success":
                    log = ksurl + s["message"] + "\n"
                    putlog.info(log)
                    log = "[kill作业信息 CASE-EXPECT-TRUE]: 测试 PASS。" + "\n"
                    putlog.info(log)
                    putlog.info("case 15-" + str(x + 1) +" test end ...\n")
                else:
                    log = ksurl + "\n\n" + s["message"] + "\n"
                    putlog.info(log)
                    log = "[kill作业信息 CASE-EXPECT-TRUE] 测试: Failure。" + "\n"
                    putlog.info(log)
                    putlog.info("case 15-" + str(x + 1) +" test end ...\n")
            else:
                s = tool.geturl(ksurl)
                if s["result"] == "success":
                    putlog.info(s["message"])
                    log = ksurl + "\n\n作业 kill 成功，kill 后状态为： kill \n"
                    putlog.info(log)
                    log = "[kill作业信息 CASE-EXPECT-FALSE] 测试: PASS。" + "\n"
                    putlog.info(log)
                    putlog.info("case 15-" + str(x + 1) +" test end ...\n")
                else:
                    log = ksurl + "\n"
                    putlog.info(log)
                    log = "作业 kill 失败，" + s["message"] + "\n"
                    putlog.info(log)
                    log = "[kill作业信息 CASE-EXPECT-FALSE] 测试: Failure。" + "\n"
                    putlog.error(log)
                    putlog.info("case 15-" + str(x + 1) +" test end ...\n")      
    except:
        log = "unkown error. \n"
        putlog.error(log)


###/* 依据作业ids resume 作业。*/###
def resumejobs(apivar):
    try:
        for x in range(len(apivar['jobs'])):
            putlog.info("case 16-" + str(x + 1) +" test start ...\n")
            log = "当前要 resume 作业号是：" + str(apivar['jobs'][x][0]) + " 作业状态是：" + apivar['jobs'][x][1] + "\n"
            putlog.info(log)
            jobs = ""
            for y in range(len(apivar['jobs'][x][0])):
                jobs += apivar['jobs'][x][0][y] + ","
            rsurl = apivar['apiurl'] + "jobs/resume?id=" + str(jobs) + "&token=" + apivar['access_token'] 
            if apivar['jobs'][x][1] == "EXIT" or apivar['jobs'][x][1] == "DONE" or apivar['jobs'][x][1] == "RUN" or apivar['jobs'][x][1] == "PEND":
                s = tool.geturl(rsurl)
                if s["result"] != "success":
                    log = rsurl + s["message"] + "\n"
                    putlog.info(log)
                    log = "[resume作业信息 CASE-EXPECT-TRUE]: 测试 PASS。" + "\n"
                    putlog.info(log)
                    putlog.info("case 16-" + str(x + 1) +" test end ...\n")
                else:
                    log = rsurl + "\n\n" + s["message"] + "\n"
                    putlog.info(log)
                    log = "[resume作业信息 CASE-EXPECT-TRUE] 测试: Failure。" + "\n"
                    putlog.info(log)
                    putlog.info("case 16-" + str(x + 1) +" test end ...\n")
            else:
                s = tool.geturl(rsurl)
                if s["result"] == "success":
                    st = ""
                    for y in range(len(apivar['jobs'][x][0])):
                        jobs = apivar['jobs'][x][0][y]
                        jdurl = apivar['apiurl'] + "job/" + jobs + "?token=" + apivar['access_token'] 
                        time.sleep(3)
                        s = tool.geturl(jdurl)
                        st += s["data"][0]["status"] + " ,"
                    log = rsurl + "\n\n作业 kill 成功，kill 后状态为：" + st + "\n"
                    putlog.info(log)
                    log = "[resume作业信息 CASE-EXPECT-FALSE] 测试: PASS。" + "\n"
                    putlog.info(log)
                    putlog.info("case 16-" + str(x + 1) +" test end ...\n")
                else:
                    log = rsurl + "\n"
                    putlog.info(log)
                    log = "作业 resume 失败，" + s["message"] + "\n"
                    putlog.info(log)
                    log = "[resume作业信息 CASE-EXPECT-FALSE] 测试: Failure。" + "\n"
                    putlog.error(log)
                    putlog.info("case 16-" + str(x + 1) +" test end ...\n")   
    except:
        log = "unkown error. \n"
        putlog.error(log)


###/* 依据作业ids stop作业。*/###
def stopjobs(apivar):
    try:
        for x in range(len(apivar['jobs'])):
            putlog.info("case 14-" + str(x + 1) +" test start ...\n")
            log = "当前要 stop 作业号是：" + str(apivar['jobs'][x][0]) + " 作业状态是：" + apivar['jobs'][x][1] + "\n"
            putlog.info(log)
            jobs = ""
            for y in range(len(apivar['jobs'][x][0])):
                jobs += apivar['jobs'][x][0][y] + ","
            sturl = apivar['apiurl'] + "jobs/stop?id=" + str(jobs) + "&token=" + apivar['access_token'] 
            if apivar['jobs'][x][1] == "EXIT" or apivar['jobs'][x][1] == "DONE" or apivar['jobs'][x][1]=="USUSP" or apivar['jobs'][x][1] =="PSUSP":
                s = tool.geturl(sturl)
                if s["result"] != "success":
                    log = sturl + s["message"] + "\n"
                    putlog.info(log)
                    log = "[stop作业信息 CASE-EXPECT-TRUE]: 测试 PASS。" + "\n"
                    putlog.info(log)
                    putlog.info("case 14-" + str(x + 1) +" test end ...\n")
                else:
                    log = sturl + "\n\n" + s["message"] + "\n"
                    putlog.info(log)
                    log = "[stop作业信息 CASE-EXPECT-TRUE] 测试: Failure。" + "\n"
                    putlog.info(log)
                    putlog.info("case 14-" + str(x + 1) +" test end ...\n")
            else:
                s = tool.geturl(sturl)
                if s["result"] == "success":
                    st = ""
                    for y in range(len(apivar['jobs'][x][0])):
                        jobs = apivar['jobs'][x][0][y]
                        jdurl = apivar['apiurl'] + "job/" + jobs + "?token=" + apivar['access_token'] 
                        time.sleep(3)
                        s = tool.geturl(jdurl)
                        st += s["data"][0]["status"] + " ,"
                    log = sturl + "\n\n作业 stop 成功，stop 后状态为：" + st + "\n"
                    putlog.info(log)
                    log = "[stop作业信息 CASE-EXPECT-FALSE] 测试: PASS。" + "\n"
                    putlog.info(log)
                    putlog.info("case 14-" + str(x + 1) +" test end ...\n")
                else:
                    log = sturl + "\n"
                    putlog.info(log)
                    log = "作业 stop 失败，" + s["message"] + "\n"
                    putlog.info(log)
                    log = "[resume作业信息 CASE-EXPECT-FALSE] 测试: Failure。" + "\n"
                    putlog.error(log)
                    putlog.info("case 14-" + str(x + 1) +" test end ...\n")   
    except:
        log = "unkown error. \n"
        putlog.error(log)

