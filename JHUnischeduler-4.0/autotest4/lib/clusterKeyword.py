#!/bin/env python
#Filename:clusterKeyword.py


from clusterLib import clusterLib
from common import execCommand

def queryClusterInfo():
    '''
    get cluster info from command 'jversion jcluster' and return a cluster object.
    '''
    cmd = "jcluster ;jversion"
    stdout, stderr, exitcode=execCommand(cmd,timeout=60)
    #print exitcode
    clst = clusterLib()
    clst.setClusterInfo(stdout)
    return clst

def getMasterName(obj):
    return obj.getMstrName()

def getVersion(obj):
    return obj.getVrsion()

def getClusterName(obj):
    return obj.getClstrName()
