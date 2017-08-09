#!/usr/bin/python
# -*- coding: UTF-8 -*-
#Date:25-14-2017
#Author:rzh
#Version=.1

import psycopg2
import pg
import urllib
import urllib2
import json
import logging
import time
import pwd
import os
import re
import commands
from urllib2 import Request, urlopen, URLError, HTTPError


###/* The log output to the console and files  */###
def putlog():
    logger = logging.getLogger("resapi test")
    logger.setLevel(logging.DEBUG)
    fh = logging.FileHandler("resapi.log")
    fh.setLevel(logging.DEBUG)
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s %(name)s %(levelname)s : %(message)s')
    fh.setFormatter(formatter)
    ch.setFormatter(formatter)
    logger.addHandler(fh)
    logger.addHandler(ch)
    return logger

putlog = putlog()


###/* the get request appform way  */###
def geturl(url):
    req = urllib2.Request(url)
    try:
        res_data = urllib2.urlopen(req)
        res = res_data.read()
        s = json.loads(res,strict=False)
        return s
    except HTTPError,e:
        log = url + " Server attempt failed. "  +str(e.code) + " \n"
	putlog.error(log)
    except URLError,e:
        log = url + " Connection refused. \n" 
        putlog.error(log)
    except ValueError,e:
        log = url + " Json string format is wrong. \n"
        putlog.error(log)
    except:
        log = url + " unkown error. \n"
        putlog.error(log)


# query job infomation .
def searchjobstate(jobid,env="/apps/unischeduler/"):
    jobinfo = "source " + env + "conf/profile.jhscheduler;jjobs -l " + str(jobid) + "| grep User"
    sh = commands.getstatusoutput(jobinfo)[1]
    cp = re.compile(r'Job <(.*)>, User <(.*)>, Project <(.*)>, Status <(.*)>, Queue <(.*)>,.*')
    jobst = cp.match(sh)
    s = jobst.groups(0)
    return s

    
# submit console job .
def subconsolejob(apivar):
    try:
        if pwd.getpwuid(os.getuid())[0] == "root":
            return "请使用普通用户提交作业。"
        else:
            # clear environment.
            cm = "source " + apivar['jhscheduler_top'] + "conf/profile.jhscheduler;for i in `jjobs -u all | awk '{print $1}' | grep -v JOBID`;do     jctrl kill $i; done"
            sh = commands.getstatusoutput(cm)
            if sh[0] == 0:
                # create EXIT job.
                cm = "source " + apivar['jhscheduler_top'] + "conf/profile.jhscheduler;jsub -P exit sleep 100"
                sh = commands.getoutput(cm)
                jobid = re.compile(r'.*<(\d*)>.*').match(sh).group(1)
                jobstate = searchjobstate(jobid,apivar['jhscheduler_top'])[3]
                if searchjobstate(jobid)[3] != "EXIT" and searchjobstate(jobid,apivar['jhscheduler_top'])[3] != "DONE":
                    cm = "source " + apivar['jhscheduler_top'] + "conf/profile.jhscheduler;jctrl kill " + jobid
                    sh = commands.getoutput(cm)
                    if searchjobstate(jobid,apivar['jhscheduler_top'])[3] == "EXIT":
                        exitjob = jobid
                # create DONE job .
                cm = "source " + apivar['jhscheduler_top'] + "conf/profile.jhscheduler;jsub -P done sleep 0.01"
                sh = commands.getoutput(cm)
                jobid = re.compile(r'.*<(\d*)>.*').match(sh).group(1)
                jobstate = searchjobstate(jobid,apivar['jhscheduler_top'])[3]
                donejob = jobid
		# create PEND job .
                cm = "source " + apivar['jhscheduler_top'] + "conf/profile.jhscheduler;jhosts -w | awk 'NR==2{print $4}'"
                nb = commands.getstatusoutput(cm)[1]
                cm ="source " + apivar['jhscheduler_top'] + "conf/profile.jhscheduler;jsub -P pend -n " + nb + " sleep 10000"
                sh = commands.getoutput(cm)
                jobid = re.compile(r'.*<(\d*)>.*').match(sh).group(1)
                jobstate = searchjobstate(jobid,apivar['jhscheduler_top'])[3]
                if searchjobstate(jobid)[3] == "PEND":
                    pendjob = jobid

                # create PSUSP job .
                cm ="source " + apivar['jhscheduler_top'] + "conf/profile.jhscheduler;jsub -P ususp -H sleep 10000"
                sh = commands.getoutput(cm)
                jobid = re.compile(r'.*<(\d*)>.*').match(sh).group(1)
                jobstate = searchjobstate(jobid,apivar['jhscheduler_top'])[3]
                if jobstate == "PSUSP":
                    psuspjob = jobid

                # create RUN job.
                cm = "source " + apivar['jhscheduler_top'] + "conf/profile.jhscheduler;jsub -P run sleep 90000"
                sh = commands.getoutput(cm)
                jobid = re.compile(r'.*<(\d*)>.*').match(sh).group(1)
                runjob = jobid

                # create USUSP job.
                cm = "source " + apivar['jhscheduler_top'] + "conf/profile.jhscheduler;jsub -P ususp sleep 100"
                sh = commands.getoutput(cm)
                jobid = re.compile(r'.*<(\d*)>.*').match(sh).group(1)
                cm = "source " + apivar['jhscheduler_top'] + "conf/profile.jhscheduler;jctrl stop " + jobid
                time.sleep(10)
                sh = commands.getoutput(cm)
                ususpjob = jobid

        return exitjob,donejob,pendjob,psuspjob,runjob,ususpjob
    except:
        log = "unkown error. \n"
        putlog.error(log)


# submit console jobs .
def subconsolenumjobs(apivar):
    if pwd.getpwuid(os.getuid())[0] == "root":
            return "请使用普通用户提交作业。"
    else:
        # clear environment.
        cm = "source " + apivar['jhscheduler_top'] + "conf/profile.jhscheduler;for i in `jjobs -u all | awk '{print $1}' | grep -v JOBID`;do     jctrl kill $i; done"
        sh = commands.getstatusoutput(cm)
        if sh[0] == 0:
            # create EXIT jobs.
            exitjobs = []
            for i in range(apivar['number']):
                cm = "source " + apivar['jhscheduler_top'] + "conf/profile.jhscheduler;jsub -P exit sleep 100"
                sh = commands.getoutput(cm)
                jobid = re.compile(r'.*<(\d*)>.*').match(sh).group(1)
                jobstate = searchjobstate(jobid,apivar['jhscheduler_top'])[3]
                if searchjobstate(jobid)[3] != "EXIT" and searchjobstate(jobid,apivar['jhscheduler_top'])[3] != "DONE":
                    cm = "source " + apivar['jhscheduler_top'] + "conf/profile.jhscheduler;jctrl kill " + jobid
                    sh = commands.getoutput(cm)
                    if searchjobstate(jobid,apivar['jhscheduler_top'])[3] == "EXIT":
                        exitjobs += [jobid]
            # create DONE jobs .
            donejobs = []
            for i in range(apivar['number']):
                cm = "source " + apivar['jhscheduler_top'] + "conf/profile.jhscheduler;jsub -P done sleep 0.01"
                sh = commands.getoutput(cm)
                jobid = re.compile(r'.*<(\d*)>.*').match(sh).group(1)
                jobstate = searchjobstate(jobid,apivar['jhscheduler_top'])[3]
                donejobs += [jobid]

            # create PEND jobs.
            pendjobs = []
            for i in range(apivar['number']):
                cm = "source " + apivar['jhscheduler_top'] + "conf/profile.jhscheduler;jhosts -w | awk 'NR==2{print $4}'"
                nb = commands.getstatusoutput(cm)[1]
                cm ="source " + apivar['jhscheduler_top'] + "conf/profile.jhscheduler;jsub -P pend -n " + nb + " sleep 10000"
                sh = commands.getoutput(cm)
                jobid = re.compile(r'.*<(\d*)>.*').match(sh).group(1)
                jobstate = searchjobstate(jobid,apivar['jhscheduler_top'])[3]
                if searchjobstate(jobid)[3] == "PEND":
                    pendjobs += [jobid]

            # create PSUSP jobs .
            psuspjobs = []
            for i in range(apivar['number']):
                cm ="source " + apivar['jhscheduler_top'] + "conf/profile.jhscheduler;jsub -P ususp -H sleep 10000"
                sh = commands.getoutput(cm)
                jobid = re.compile(r'.*<(\d*)>.*').match(sh).group(1)
                jobstate = searchjobstate(jobid,apivar['jhscheduler_top'])[3]
                if jobstate == "PSUSP":
                    psuspjobs += [jobid]
            # create RUN jobs.
            runjobs = []
            for i in range(apivar['number']):
                cm = "source " + apivar['jhscheduler_top'] + "conf/profile.jhscheduler;jsub -P run sleep 90000"
                sh = commands.getoutput(cm)
                jobid = re.compile(r'.*<(\d*)>.*').match(sh).group(1)
                runjobs += [jobid]

            # create USUSP jobs.
            ususpjobs = []
            for i in range(apivar['number']):
                cm = "source " + apivar['jhscheduler_top'] + "conf/profile.jhscheduler;jsub -P ususp sleep 100"
                sh = commands.getoutput(cm)
                jobid = re.compile(r'.*<(\d*)>.*').match(sh).group(1)
                cm = "source " + apivar['jhscheduler_top'] + "conf/profile.jhscheduler;jctrl stop " + jobid
                time.sleep(10)
                sh = commands.getoutput(cm)
                ususpjobs += [jobid]

            return (exitjobs,"EXIT"),(donejobs,"DONE"),(pendjobs,"PEND"),\
            (psuspjobs,"PSUSP"),(runjobs,"RUN"),(ususpjobs,"USUSP")


# According to the number of state query operation .
def statjobnum(apivar):
    try:
        if pwd.getpwuid(os.getuid())[0] == "root":
            return "请使用普通用户提交作业。"
        else:
            cm = "source " + apivar['jhscheduler_top'] + "conf/profile.jhscheduler;jjobs -u all | grep " + apivar['status'] + " | wc -l"
            sh = commands.getstatusoutput(cm)
            return sh[1]
    except:
        log = "unkown error. \n"
        putlog.error(log)


# scope 查询后台作业个数。 .
def queryjobnum(apivar):
    try:
        if pwd.getpwuid(os.getuid())[0] == "root":
            return "请使用普通用户提交作业。"
        else:
            cm = "source " + apivar['jhscheduler_top'] + "conf/profile.jhscheduler;jjobs -u all -a | grep -v JOBID | wc -l"
            sh = commands.getstatusoutput(cm)
            return sh[1]
    except:
        log = "unkown error. \n"
        putlog.error(log)


#提交一个带作业名字的作业
def onlysubjob(apivar):
    cm = "source " + apivar['jhscheduler_top'] + "conf/profile.jhscheduler;jsub -J testplan" + apivar['times'] + " sleep 10 "
    sh = commands.getoutput(cm)
    jobid = re.compile(r'.*<(\d*)>.*').match(sh).group(1)
    jobinfo = "source " + apivar['jhscheduler_top'] + "conf/profile.jhscheduler;jjobs -l " + str(jobid) + "| grep User"
    sh = commands.getstatusoutput(jobinfo)[1]
    cp = re.compile(r'Job <(.*)>, Job Name <(.*)>, User <(.*)>, Project <(.*)>,.*')
    jobst = cp.match(sh)
    s = jobst.groups(0)
    return s

#创建作业数据文件
def addjobfile(apivar):
    cm = "cd " + apivar['appform_top'] + "spoolers/jhadmin;mkdir plus_" + apivar['currentime'] + ";cd plus_" + \
    apivar['currentime'] + ";touch files.txt readme.md log.doc error.null jhinno.md appform.conf"
    sh = commands.getstatusoutput(cm)
    return sh


###/* operate postgresql 。*/###
def operatepsql(apivar):
    try:
        conn = psycopg2.connect(database=apivar['dbname'],user=apivar['user'],password=apivar['passwd'],host=apivar['host'],port=apivar['port'])
        cur = conn.cursor()
        if apivar['dml'] == "sele":
            cur.execute(apivar['sql'])
            rows = cur.fetchall()
            return rows
        if apivar['dml'] == "inst":
            cur.execute(apivar['sql'])
            conn.commit()
        if apivar['dml'] == "dele":
            cur.execute(apivar['sql'])
            conn.commit()
        cur.close()
        conn.close()
    except psycopg2.IntegrityError,e:
        log = "此作业id已经存在\n" 
        putlog.error(log)
    except:
        log = "unkown error. \n"
        putlog.error(log)
