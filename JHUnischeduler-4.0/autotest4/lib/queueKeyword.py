#!/bin/env python
#Filename:queueKeyword.py


import re
from queueLib import queueLib
from subprocess import Popen,PIPE
from common import get_value,execCommand

def queryQueinfo(qName,timeout=60):
    '''
    according the queue name,return the object of the queue.
    E.g: qName = 'normal'
    '''
    timeout=int(timeout)
    stdout, stderr, exitcode=execCommand("jqueues -l %s"%(qName),timeout)
    #print exitcode
    if stdout.replace(" ","")=="Normal:Nosuchqueue.\n":
        print stdout
        raise RuntimeError
    else:
        que = queueLib()
        que.setBasicQueueInfo(stdout)
        return que

def queryAllQueinfo(timeout=60):
    '''
    query the results from jqueues -l and return a list of all queues objects.
    '''
    #list of object
    all_queue_list = []
    #str = os.popen("jqueues -l").read()
    timeout=int(timeout)
    stdout, stderr, exitcode=execCommand("jqueues -l",timeout)
    #print exitcode
    queues_list = re.findall(r'\bQUEUE:\s*(.*)\s*\n',stdout)
    queue_num=len(queues_list)
    while queue_num:
        all_queue_list.append(queryQueinfo(queues_list[queue_num-1]))
        queue_num -= 1
    return all_queue_list

def getQueName(que):
    return que.QueName

def getQueUser(que):
    return que.QueUsers

def getQueHosts(que):
    return que.QueHosts

def getQueStatus(que):
    return que.QueStatus

def getQueMax(que):
    return que.QueMax

def getQuePRIO(que):
    return que.QuePRIO

def getQueThredload(que):
    return que.getThredload()

def getQueUjoblimit(que):
    return que.QueUjoblimit

def getQueCpuLmt(que):
    return que.QueCpuLmt

def getQuePendjob(que):
    return que.QuePendjobnum

def getQueRunjob(que):
    return que.QueRunjobnum

def getQueSsuspjob(que):
    return que.QueSsuspjobnum

def getQueUsuspjob(que):
    return que.QueUsuspjobnum

def getQueRSVSlot(que):
    return que.QueRSVSlotnum

def getQueExclu(que):
    return que.QueExclu

def getQueFairShare(que):
    return que.QueFairShare

def getQuePrmt(que):
    return que.QuePrmt

def getQuePre(que):
    return que.QuePre

def getQuePost(que):
    return que.QuePost

def getQueRunWdw(que):
    return que.QueRunWdw

def getQueResSched(que,resName):
    if que.QueResSched:
        return get_value(resName,que.QueResSched)
    else:
        return ""

def getQueResStop(que,resName):
    if que.QueResStop:
        return get_value(resName,que.QueResStop)
    else:
        return ""


