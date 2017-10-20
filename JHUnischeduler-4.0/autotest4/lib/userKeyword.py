#!/bin/env python
#Filename:userKeyword.py


from subprocess import Popen,PIPE
from userLib import userLib
from common import execCommand


def queryUserInfo(userName):
    '''
    get user info from the param 'userName' and return a user object.
    '''
    user = userLib()
    stdout, stderr, exitcode=execCommand("jusers %s"%(userName),timeout=30)
    if userName != '':
        user.setUsrBasicInfo(stdout)
    else:
        print "invalid user name"
    return user

def getUsrName(obj):
    return obj.UsrName

def getUsrMax(obj):
    return obj.UsrMax

def getUsrNjobs(obj):
    return obj.UsrNjobs

def getUsrPend(obj):
    return obj.UsrPend

def getUsrRun(obj):
    return obj.UsrRun

def getUsrSsusp(obj):
    return obj.UsrSsusp

def getUsrUsusp(obj):
    return obj.UsrUsusp

def getUsrRsv(obj):
    return obj.UsrRsv

def getUsrJLP(obj):
    return obj.UsrJLP

