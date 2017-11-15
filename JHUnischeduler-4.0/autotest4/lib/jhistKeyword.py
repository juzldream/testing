#!/bin/env python
#Filename:myUtils.py

import os
import re
from common import execCommand

def getJobRunTimeHist(jobid):
    jobid=jobid.replace('\n','')
    stdout, stderr, exitcode=execCommand("jhist -l %s|sed -n '$p'|awk '{print $3}'"%jobid)
    print stdout
    return stdout

def getJobExitCodeHist(jobid):
    jobid=jobid.replace('\n','')
    stdout, stderr, exitcode=execCommand("jhist -l %s"%jobid)
    print exitcode,stdout
    exit=re.findall(r'Exit with exit code \<(.*)\>.',stdout)
    return exit[0]

def getJobCpuTimeHist(jobid):
    jobid=jobid.replace('\n','')
    stdout, stderr, exitcode=execCommand("jhist -l %s"%jobid)
    output1=stdout.replace("\n","").replace(" ","")
    exitcode=re.findall(r'TheCPUtimeusedis(.*)seconds;',output1)
    return exitcode[0]
   
