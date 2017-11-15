#!/usr/bin/env python
#Filename:jobLib.py


import re
from common import get_command_param,get_value

#def matchJobInfo(title,result):
#        print "go1"
#        print title
#        jobvalue = re.findall(r'+%s+\s*=\s*(.+)\n'%title,result)


class jobLib:
    '''
    all the methods function as follows:
    1)set the output of command 'jsub job' and get jobId/jobQueue.
    2)set the output of command 'jjobs -l' and get all the message of job.
    '''
    def __init__(self):
        self.jobId = ""
        self.jobUser = ""
        self.jobStatus = ""
        self.jobProject = ""
        self.jobName = ""
        self.jobCommand = ""
        self.jobQueue = ""
        self.jobSubmitHost = ""
        self.jobExecHost = ""
        self.jobExecHome = ""
        self.jobSubmitDir = ""
        self.jobExecDir = ""
        self.jobReqResource =""
        self.jobSubmitTime = ""
        self.jobExecTime = ""
        self.jobEndTime = ""
        self.jobPndRsn = ""
        self.jobSSndRsn = ""
        #self.jobSchedInfo = {}
        self.jobExecUser = ""
        self.jobResUsg = {}
        self.jobExitStat = ""
        self.jobPreCmd=""
        self.jobCpuTime=float(0.0)
        self.jobExitCode=""
        self.jobResvSlosts=int(0)
        self.jobResvHosts=""

    def setSubmitJob(self,result):
        '''
        set the output of command 'jsub job' and get jobId/jobQueue.
        '''
        result = result.replace('\n','').replace(' ','')
        self.jobId = re.findall(r'Job<(\d*)>',result)
        if self.jobId:
            self.jobId=self.jobId[0]
        self.jobQueue = re.findall(r'queue<(\w*)>',result)
        if self.jobQueue:
            self.jobQueue=self.jobQueue[0]

    def setBasicInfo(self,job_info):
        '''
        set the output of command 'jjob -l jobid' and get all the information of job.
        '''
        #print job_info
        jobId = re.findall(r'\s*\bJob\s*ID\s*:(.+)\s*\n', job_info)
        if jobId:
            self.jobId = jobId[0].strip()

        job_param_dict=get_command_param(job_info,"jjobs -l")
        self.jobName = get_value("Job Name",job_param_dict)
        self.jobQueue = get_value("Queue",job_param_dict)
        self.jobUser = get_value("User",job_param_dict)
        self.jobStatus = get_value("Status",job_param_dict)
        self.jobProject =  get_value("Project",job_param_dict)
        self.jobCommand = get_value("Command",job_param_dict)
        self.jobSubmitHost = get_value("Submitted.Host",job_param_dict)
        self.jobExecHost = get_value("Execution.Hosts",job_param_dict)
        self.jobSubmitDir = get_value("Submitted.CWD",job_param_dict)
        self.jobExecHome = get_value("Execution.Home",job_param_dict)
        self.jobExecDir =  get_value("Execution.CWD",job_param_dict)
        self.jobReqResource = get_value("Resource",job_param_dict)
        self.jobSubmitTime = get_value("Submitted.time",job_param_dict)
        self.jobExecTime = get_value("Execution.time",job_param_dict)
        self.jobEndTime = get_value("Exit.time",job_param_dict)
        self.jobPreCmd = get_value('PreCommand',job_param_dict)
        self.jobCpuTime = get_value('CpuTime',job_param_dict)
        self.jobExitCode = get_value('Exit.Code',job_param_dict) 
        self.jobResvSlots = get_value('Reserved.Slots',job_param_dict)
        self.jobResvHosts = get_value('Reserved.Hosts',job_param_dict) 
        ExitStatDone = get_value("Exit.Done",job_param_dict)
        ExitStatExit = get_value("Exit.Code",job_param_dict)
        if ExitStatDone:
            self.jobExitStat = ExitStatDone
        if ExitStatExit:
            self.jobExitStat = ExitStatExit
        self.jobPndRsn = get_value("PendingReasons",job_param_dict)
        self.jobSSndRsn = get_value("SuspendingReasons", job_param_dict)
        self.jobExecUser = get_value("Execution.User",job_param_dict)
        used_res_tmp = get_value("UsedResource",job_param_dict)
        if used_res_tmp:
            tmp1 = used_res_tmp.split(';')
            for list1 in tmp1:
                used_res = list1.split(':')
                if used_res:
                    key=used_res[0].strip()
                    value=used_res[1].strip()
                    self.jobResUsg[key]=value







