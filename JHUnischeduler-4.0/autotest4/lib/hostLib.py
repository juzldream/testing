#!/bin/env python
#Filename:hostlib.py


import re
from common import get_command_param,get_value,get_res_use_or_threshold


class hostLib:
    '''
    all the methods function as follows:
    1)set the output of command 'jhosts -l or jhhosts -l, and get host attribute value.
    2)get host attribute value such as hostname/hoststatus and so on.
    '''
    def __init___(self):
        self.hostname=""
        self.hoststatus=""
        #self.hostcpuf=""
        self.hostslots=""
        self.hostType=""
        self.hostModel=""
        self.hostNjobs=""
        self.hostSSUSPjob=""
        self.hostRunjob=""
        self.hostUSUSPjob=""
        self.hostRSV=""
        self.hostStaticload = []
        #self.hostRUN_WINDOW=""
        self.hostRESOURCES=""
        self.hostDISPATCH_WINDOW=""
        #self.hostRusageAll = []
        self.hostTotalRusage = {}
        self.hostResvRusage = {}
        self.hostStopload={}
        self.hostSchedload = {}
        self.resTotal=int(0)
        self.resResv=int(0)
        self.resInterv=int(0)
        self.resHost=""
 
    def setHostBasicInfo(self,host_info):
        hostname = re.findall(r'\s*\bHost:\s*(.*)\s*\n',host_info)
        if hostname:
            self.hostname =hostname[0].strip()

        host_param_dict=get_command_param(host_info,"jhosts -l")
        self.hostcpuf=get_value("Cpuf",host_param_dict)
        self.hoststatus = get_value("Status",host_param_dict)
        self.hostslots = get_value("Max",host_param_dict)
        self.hostNjobs = get_value("JobsNum",host_param_dict)
        self.hostRunjob = get_value("Run",host_param_dict)
        self.hostSSUSPjob = get_value("SSUSP",host_param_dict)
        self.hostUSUSPjob = get_value("USUSP",host_param_dict)
        self.hostRSV = get_value("Rsv",host_param_dict)
        self.hostDISPATCH_WINDOW = get_value("DISPATCH_WINDOW",host_param_dict)

        self.hostSchedload = get_res_use_or_threshold(host_info,"jhosts -l","sched")
        self.hostStopload = get_res_use_or_threshold(host_info,"jhosts -l","stop")
        self.hostTotalRusage = get_res_use_or_threshold(host_info,"jhosts -l","total")
        self.hostResvRusage = get_res_use_or_threshold(host_info,"jhosts -l","resvd")

    def setHostStatBasInfo(self,host_info):
        hostname = re.findall(r'\s*\bHost:\s*(.*)\n',host_info)
        if hostname:
            self.hostname =hostname[0]

        host_stat_param_dict=get_command_param(host_info,"jhosts -l")
        self.hostType=get_value("type",host_stat_param_dict)
        self.hostModel=get_value("model",host_stat_param_dict)

         
    def setResInfo(self,res_info):
        #res_tmp=re.findall(r's+(\w+)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\w+)',res_info)
        res_tmp=re.match(r'RESOURCE\s+TOTAL\s+RESERVED\s+INTERVAL\s+LOCATION\s+(\w+)\s+(\w+|-)\s+(\w+|-)\s+(\w+|-)\s+(\w+|-)',res_info)
        res_tmp1=re.findall(r'RESOURCE\s+TOTAL\s+RESERVED\s+INTERVAL\s+LOCATION\s+(\w+)\s+(\w+|-)\s+(\w+|-)\s+(\w+|-)\s+(\w+|-)',res_info)
        print res_tmp1
        if res_tmp:
            #self.resName=res_info[0]
            self.resTotal=res_tmp.group(2)
            #print "resTotal:%s"%self.resTotal
            self.resResv=res_tmp.group(3)
            #print "resResv:%s"%self.resResv
            self.resInterv=res_tmp.group(4)
            #print "resInterv:%s"%self.resInterv
            self.resHost=res_tmp.group(5)
            #print "resHost:%s"%self.resHost

