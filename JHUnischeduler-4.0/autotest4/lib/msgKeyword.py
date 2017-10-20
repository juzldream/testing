#!/bin/env python
#Filename:msgLib.py

from msgLib import msgLib
from common import execCommand

def queryMsgInfo(cmd):   
    cmd = cmd.replace('\n','')
    stdout, stderr, exitcode=execCommand(cmd)
    if stdout:
        msg = msgLib()
        msg.setBasicInfo(stdout)
        return msg
    #else: 
    #    print "the output of %s is empty"%cmd
    #    return ""

def getMsgJobId(msg):
    return msg.jobId

def getMsgIndex(msg):
    return  msg.msgIndex
    
def getMsgPutTime(msg):
    return  msg.putTime

def getMsgUserName(msg):
    return  msg.userName

def getMsgDesc(msg):
    return  msg.Desc

