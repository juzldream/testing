#!/bin/env python
#Filename:queueLib.py


import re
from common import get_value,get_command_param,get_res_use_or_threshold


class queueLib:
    '''
    all the methods function as follows:
    1)set the result from jqueues -l queuename and get info of queue such as queue name,status and so on.
    2)get queue attribute value such as QueName/QueMax and so on.
    '''
    def __init__(self):
        self.QueName=''
        self.QueUsers=[]
        self.QueHosts=[]
        self.QueStatus=''
        self.QueMax=''
        self.QuePRIO=''
        self.QueResSched={}
        self.QueResStop={}
        self.QueUjoblimit=''
        self.QuePendjobnum=''
        self.QueRunjobnum=''
        self.QueSsuspjobnum = ''
        self.QueUsuspjobnum = ''
        self.QueRSVSlotnum = ''
        self.QueExclu = ''
        self.QueFairShare = ''
        self.QuePrmt = []
        self.QueRunWdw = ''
        self.QueCpuLmt = ''
        self.QuePre = ''
        self.QuePost = ''

    def setBasicQueueInfo(self,queues_command_result):
        queue_name=re.findall(r'\bQUEUE:\s*(.+)\s*\n',queues_command_result)
        if queue_name:
            self.QueName=queue_name[0].strip()

        queue_parm_dict=get_command_param(queues_command_result,"jqueues -l")
        self.QueUsers=get_value("Users",queue_parm_dict)
        if self.QueUsers and self.QueUsers.replace(" ","") != "allusers":
           self.QueUsers=self.QueUsers.split()

        self.QueHosts=get_value("Hosts",queue_parm_dict)
        if self.QueHosts and self.QueHosts.replace(" ","") != "allhostsusedbytheschedulersystem":
           self.QueHosts=self.QueHosts.split()

        self.QuePrmt=get_value("Preemption",queue_parm_dict)
        self.QuePrmt=self.QuePrmt.split()

        self.QueStatus=get_value("stat.Status",queue_parm_dict)
        self.QueMax=get_value("stat.Max",queue_parm_dict)
        self.QuePRIO=get_value("stat.Prio",queue_parm_dict)
        self.QueThredload={}
        self.QueUjoblimit=get_value("stat.JL/U",queue_parm_dict)
        self.QuePendjobnum=get_value("stat.Pend",queue_parm_dict)
        self.QueRunjobnum=get_value("stat.Run",queue_parm_dict)
        self.QueSsuspjobnum = get_value("stat.SSUSP",queue_parm_dict)
        self.QueUsuspjobnum = get_value("stat.USUSP",queue_parm_dict)
        self.QueRSVSlotnum = get_value("stat.Rsv",queue_parm_dict)
        self.QueExclu = get_value("SchedulingPolicies",queue_parm_dict)
        self.QueFairShare = get_value("FairShare",queue_parm_dict)
        self.QueRunWdw = get_value("RunWindow",queue_parm_dict)
        self.QueCpuLmt = get_value("CpuLimit",queue_parm_dict)
        self.QuePre = get_value("PreExec",queue_parm_dict)
        self.QuePost = get_value("PostExec",queue_parm_dict)
        self.QueResSched = get_res_use_or_threshold(queues_command_result,"jqueues -l","sched")
        self.QueResStop=get_res_use_or_threshold(queues_command_result,"jqueues -l","stop")

