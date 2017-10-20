#!/bin/env python
#Filename:userGroupKeyword.py


import os
import re
from userGroupLib import userGroupLib
from subprocess import Popen,PIPE
from common import execCommand


def queryUsrGroup(grpName):
    '''
    query usergroup info from the param 'grpName' and return a usergroup object.
    '''
    stdout, stderr, exitcode=execCommand("jugroup -g %s"%(grpName),timeout=60)
    #print exitcode
    ug = userGroupLib()
    ug.setGrUserBasicInfo(stdout)
    return ug

def queryAllUserGroup():
    '''
    query all usergroup info and return a list of usergroup object.
    '''
    usrgroup = []
    #acccording to the output get group name
    stdout, stderr, exitcode=execCommand("jusergroup -l ",timeout=60)
    #print exitcode
    grp_all_name=re.findall(r'\bGroup:\s+(.+)\s*\n',stdout)
    for i in range(len(grp_all_name)):
        usrgroup.append(queryUsrGroup(grp_all_name[i]))
    return usrgroup

def getUserGroupMem(ug):
    return ug.uGroupMem
def getUserGroupAdmin(ug):
    return ug.uGroupAdmin
