#!/user/bin/python
#Filename:hostKeyword.py

import re
from hostLib import hostLib
from subprocess import Popen,PIPE
from common import get_value,bit_change,execCommand
import time

def QueryHostInfo(hostname):
    '''
    query the output of command 'jhosts -l hostname' and return a host object.
    '''
    cmd="jhosts -l %s"%hostname
    stdout, stderr, exitcode=execCommand(cmd,timeout=60)
    #print exitcode
    print stdout
    if exitcode:
        return ""
    else:
        host = hostLib()
        host.setHostBasicInfo(stdout)
        return host

def QueryHostStaticInfo(hostname):
    '''
    query the output of command 'jhosts -l hostname' and return a host object.
    '''
    cmd="jhhosts metrics %s"%hostname
    stdout, stderr, exitcode=execCommand(cmd,timeout=60)
    #print exitcode
    if exitcode:
        return ""
    else:
        host = hostLib()
        host.setHostStatBasInfo(stdout)
        return host

def QueryAllHostInfo():
    '''
    query the output of command 'jhosts -l' and return a list of all hosts objects.
    '''
    hosts=[]
    hostsname=[]
    stdout, stderr, exitcode=execCommand("jhosts -l ",timeout=60)
    #print exitcode
    hostsname = re.findall(r'\bHost:\s*(.*)\n', stdout)
    for i in range(len(hostsname)):
        hosts.append(QueryHostInfo(hostsname[i]))
        i=i+1
    return hosts

def getHostName(host):
    return host.hostname

def getHostStatus(host):
    return host.hoststatus

def getHostType(host):
    '''
    only the command of "jhosts -l hosts"  can use
    '''
    return host.hostType

def getHostSlots(host):
    return host.hostslots

def getHostModel(host):
    return host.hostModel

def getHostRunjob(host):
    return host.hostRunjob

def getHostRSV(host):
    return host.hostRSV

#def getHostRUN_WINDOW(host):
 #   return host.hostRUN_WINDOW

def getHostDISPATCH_WINDOW(host):
    return host.hostDISPATCH_WINDOW

#get host LOAD_THRESHOLDS.
def getHostThredSched(host,resName):
    if host.hostSchedload:
        return bit_change(get_value(resName,host.hostSchedload))
    else:
        return ""

def getHostThredStop(host,resName):
    if host.hostStopload:
        return bit_change(get_value(resName,host.hostStopload))
    else:
        return ""

#get host LOAD THRESHOLD USED FOR SCHEDULING.
def getHostReserved(host,resName):
    '''
    resName = { r15s | r1m | r15m | ut | pg | io | ls | it | tmp | swp | mem | cpuspeed }
    '''
    if host.hostResvRusage:
        return bit_change(get_value(resName,host.hostResvRusage))
    else:
        return ""

def getHostResTotal(host,resName):
    '''
    resName = { r15s | r1m | r15m | ut | pg | io | ls | it | tmp | swp | mem | cpuspeed }
    '''
    if host.hostTotalRusage:
        return bit_change(get_value(resName,host.hostTotalRusage))
    else:
        return ""

def getHostGroupMem(groupName):
    '''
    query the output of command 'jhostgroup' and return a hostgroup object.
    '''
    host_group_mem={}
    stdout, stderr, exitcode=execCommand("jhostgroup -r %s"%groupName,timeout=60)
    #print exitcode
    if stdout:
        host_group_mem = re.findall(r'\s*\bHosts\s*=\s*(.*)\s*\n',stdout)
        return host_group_mem
    else:
        raise RuntimeError

def getStatShareResResv(res):
    res=str(res)
    #this code for test:resv begin
    stdoutx, stderrx, exitcodex=execCommand("jhosts -s %s'"%res,timeout=20)
    print stdoutx, stderrx, exitcodex
    #this code for test:resv end
    stdout, stderr, exitcode=execCommand("jhosts -s %s|sed -n '$p'|awk '{print $3}'"%res,timeout=60)
    if exitcode:
        print 'exec "jhosts -s %s" failed'%res
        raise RuntimeError
    else:
        return stdout.strip()

def getStatShareResTotal(res):
    res=str(res)
    #this code for test:total begin
    stdoutx, stderrx, exitcodex=execCommand("jhosts -s %s'"%res,timeout=20)
    print stdoutx, stderrx, exitcodex
    #this code for test:total end
    stdout, stderr, exitcode=execCommand("jhosts -s %s|sed -n '$p'|awk '{print $2}'"%res,timeout=60)
    if exitcode:
        print 'exec "jhosts -s %s" failed'%res
        raise RuntimeError
    else:
        return stdout.strip()


def checkStatShareResResv(res_name,num,timeout=30):
    res_name=str(res_name)
    timeout=int(timeout)
    num=int(num)
    try:
        while timeout>0:
            stdout0, stderr0, exitcode0=execCommand("ps -ef|grep $JHSCHEDULER_TOP")
            print stdout0, stderr0, exitcode0
            print timeout
            stdout2, stderr2, exitcode2=execCommand("jhosts -s",timeout=30)
            print stdout2, stderr2, exitcode2
            stdout, stderr, exitcode=execCommand("jhosts -s %s|sed -n '$p'|awk '{print $3}'"%res_name,timeout=30)
            print "stdout=%s,stderr=%s,exitcode=%s"%(stdout, stderr, exitcode)
            if stdout and stdout.strip() and stdout.strip().isdigit() and int(stdout.strip())==num:
                return stdout
            else:
                timeout=timeout-1
                try:
                    time.sleep(2)
                except KeyboardInterrupt:
                    print ''
                    raise RuntimeError
    except KeyboardInterrupt:
        print ''
        raise RuntimeError
    if timeout==0:
        raise RuntimeError


def checkStatShareResTotal(res_name,num,timeout=30):
    res_name=str(res_name)
    timeout=int(timeout)
    num=int(num)
    try:
        while timeout>0:
            stdout0, stderr0, exitcode0=execCommand("ps -ef|grep $JHSCHEDULER_TOP")
            print stdout0, stderr0, exitcode0
            print timeout
            stdout2, stderr2, exitcode2=execCommand("jhosts -s",timeout=30)
            print stdout2, stderr2, exitcode2
            stdout, stderr, exitcode=execCommand("jhosts -s %s|sed -n '$p'|awk '{print $2}'"%res_name,timeout=30)
            print "stdout=%s,stderr=%s,exitcode=%s"%(stdout, stderr, exitcode)
            if stdout and stdout.strip() and stdout.strip().isdigit() and int(stdout.strip())==num:
                return stdout
            else:
                timeout=timeout-1
                try:
                    time.sleep(2)
                except KeyboardInterrupt:
                    print ''
                    raise RuntimeError
    except KeyboardInterrupt:
        print ''
        raise RuntimeError
    if timeout==0:
        raise RuntimeError

def checkHostResTotal(host,resName,num,timeout=30):
    host=str(host)
    res_name=str(resName)
    timeout=int(timeout)
    num=int(num)
    try:
        while timeout>0:
            stdout0, stderr0, exitcode0=execCommand("ps -ef|grep $JHSCHEDULER_TOP")
            print stdout0, stderr0, exitcode0
            print timeout
            host_info=QueryHostInfo(host)
            if host_info:
                res_value=get_value(res_name,host_info.hostTotalRusage)
                if res_value and res_value != "-" and int(res_value)==num:
                    print "%s:%s"%(res_name,res_value)
                    return res_value
                else:
                    print "%s:%s"%(res_name,res_value)
                    timeout=timeout-1
                    try:
                        time.sleep(2)
                    except KeyboardInterrupt:
                        print ''
                        raise RuntimeError
            else:
                print "hostinfo:%s"%host_info
                timeout=timeout-1
                try:
                    time.sleep(2)
                except KeyboardInterrupt:
                    print ''
                    raise RuntimeError

    except KeyboardInterrupt:
        print ''
        raise RuntimeError
    if timeout==0:
        raise RuntimeError

#checkStatShareResTotal("res1",3)
