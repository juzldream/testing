#!/usr/bin/python
#Filename:jobKeyword.py


import re
from jobLib import jobLib
import time
from common import get_value,bit_change,execCommand

def submitEsubJob(string):
    cmd = string.replace('\n','')
    stdout, stderr, exitcode=execCommand(cmd)
    job = jobLib()
    job.setSubmitJob(stdout)
    return stdout,exitcode,job

def querySubmitInfo(string):
    '''
    query the output of command 'jsub job' and return a job object.
    E.g:
    string = 'jsub -P "test_project" -J "test_name" -R "rusage[mem=100]" sleep 10000'
    '''
    cmd = string.replace('\n','')
    stdout, stderr, exitcode=execCommand(cmd,timeout=60)
    print stdout
    print stderr
    job = jobLib()
    job.setSubmitJob(stdout)
    return job

def queryJobInfo(jobId,user="jhadmin"):
    '''
    query the output of command 'jjobs -l jobid' and return a job object.
    '''
    cmd="su %s -c 'jjobs -l %s'"%(user,str(jobId))
    stdout, stderr, exitcode=execCommand(cmd,timeout=60)
    #print exitcode
    job = jobLib()
    job.setBasicInfo(stdout)
    return job

def queryUserJobInfo(command):
    '''
    query the output of command 'jjobs -l' and return a list of all job objects.
    '''
    cmd_tmp = command.replace('\n','')
    stdout, stderr, exitcode=execCommand(cmd_tmp,timeout=60)
    #print exitcode
    jobId=re.findall(r'(?<=\b)Job ID:(.*)\n',stdout)
    print jobId
    return jobId

def getJobIdAll(command):
    lista=[]
    cmd_tmp = command.replace('\n','')
    stdout, stderr, exitcode=execCommand("%s|sed 1d|awk '{print $1}'"%cmd_tmp,timeout=60)
    print stdout, stderr, exitcode
    if exitcode==0 and stdout:
        print stdout
        lista=stdout.strip().split("\n")
        for i in lista:
            i.strip()
    return lista

def queryAllJobInfo(user="jhadmin"):
    '''
    query the output of command 'jjobs -l' and return a list of all job objects.
    '''
    jobList = []
    cmd = "su %s -c 'jjobs -l'"%(user)
    stdout, stderr, exitcode=execCommand(cmd,timeout=60)
    #print exitcode
    jobId=re.findall(r'(?<=\b)Job ID:(.*)\n',stdout)
    j = len(jobId)
    while j:
        tmp = queryJobInfo(jobId[j-1])
        jobList.append(tmp)
        j-=1
    return jobList

def getJobId(job):
    return job.jobId

def getJobUser(job):
    return job.jobUser

def getJobStatus(job):
    return job.jobStatus

def getJobName(job):
    return job.jobName

def getJobCommand(job):
    return job.jobCommand

def getJobQueue(job):
    return job.jobQueue

def getJobProject(job):
    return job.jobProject

def getJobSubmitHost(job):
    return job.jobSubmitHost

def getJobCpuTime(job):
    cpu_time=re.findall(r'used\s+(.*)\s+seconds',job.jobCpuTime)
    if cpu_time:
        return float(cpu_time[0])
    else: 
        return float(cpu_time)

def getJobExecHost(job):
    milti_host=[]
    try:
        hosts=re.findall(r'\d\sProcessors\s<[\d\*]*(.*)[\s\d\*]*(.*)>',job.jobExecHost)
    except:
        return job.jobExecHost
    if hosts:
        host_all ="".join(hosts[0])
        for i in host_all.split(" "):
            milti_host.append(i)
        for list_unit in milti_host:
            if list_unit == '':
                milti_host.remove(list_unit)
        if len(milti_host)==1:
            return "".join(milti_host)
        else:
            return milti_host
    else:
        return job.jobExecHost

def getJobReservedSlots(job):
    return job.jobResvSlots

def getJobReservedHosts(job):
    return job.jobResvHosts

def getJobExitCode(job):
    return job.jobExitCode

def getJobExecHome(job):
    return job.jobExecHome

def getJobSubmitDir(job):
    return job.jobSubmitDir

def getJobExecDir(job):
    return job.jobExecDir

def getJobReqResource(job):
    return job.jobReqResource

def getJobSubmitTime(job):
    return job.jobSubmitTime

def getJobExecTime(job):
    return job.jobExecTime

def getJobEndTime(job):
    return job.jobEndTime

def getJobPndRsn(job):
    return job.jobPndRsn

def getJobSpndRsn(job):
    return job.jobSSndRsn
def getJobPreCmd(job):
    return job.jobPreCmd

def getJobExecUser(job):
    return job.jobExecUser

def getJobRusageInfo(job,resName):
    '''
    resName = { MEM | SWAP | PGID | PIDs }
    '''
    if job.jobResUsg:
        print job.jobResUsg
        print get_value(resName,job.jobResUsg)
        return bit_change(get_value(resName,job.jobResUsg))
    else:
        return ""

def getJobOutput(job):
    jobid = job.jobId
    jobuser = job.jobUser
    cmd = "su %s -c 'jctrl peek %s'"%(jobuser,jobid)
    stdout, stderr, exitcode=execCommand(cmd,timeout=60)
    #print exitcode
    return stdout.replace('<< output from stdout >>','')

def getJobUsedProc(job):
    return job.jobExecHost

def getAndCheckJobUsedProc(jobid,timeout=30):
    timeout=int(timeout)
    for i in range(1,timeout):
        job=queryJobInfo(jobid)
        exec_host=getJobUsedProc(job)
        if exec_host:
            return exec_host
        else:
            time.sleep(1)
        if i==(timeout-1):
            raise IndexError("cannot get the job used processors %s"%jobid)

def getAndCheckJobExecHost(jobid,timeout=30):
    timeout=int(timeout)
    for i in range(1,timeout):
        cmd = "jjobs -l " + str(jobid)
        stdout, stderr, exitcode=execCommand(cmd,timeout=60)
        print stdout
        job=queryJobInfo(jobid)
        exec_host=getJobExecHost(job)
        if exec_host:
            return exec_host
        else:
            time.sleep(1)
        if i==(timeout-1):
            raise IndexError("cannot get the exec host %s"%jobid)

def getAndCheckJobRusageInfo(jobid,resName,timeout=60):
    '''
    resName = { MEM | SWAP | PGID | PIDs }
    '''
    timeout=int(timeout)
    for i in range(1,timeout):
        job=queryJobInfo(jobid)
        job_res=getJobRusageInfo(job,resName)
        if job_res!="":
            return job_res
        else:
            try:
                time.sleep(1)
            except (KeyboardInterrupt, EOFError, IOError):
                print ""
                raise RuntimeError
        if i==(timeout-1):
            raise IndexError("cannot get the value of %s"%resName)


