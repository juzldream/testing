#!/usr/bin/python
#Filename:queuesConfLib.py



from common import *
from myUtils import killAllJob
import hostsConfLib


def addOrModifyQueue(queName,queInfo):
    '''
    This function can only add a basic queue.
    eg:queName="host1" queInfo="PRIORITY=10\nPREEMPTION=PREEMPTIVE"
    '''
    queName=queName.strip()
    conf_file = get_path("JHSCHEDULER_ENV","queues.conf")
    result=read_conf(conf_file)
    conf_length=len(result)
    result_tmp=[]
    exist_name,exist_next_section,name_site,next_section_site=parse_que_conf(result,queName)
    if exist_name:
        if exist_next_section:
            for j in range(name_site,next_section_site):
                result[j]=""
        else:
            for j in range(name_site,conf_length):
                result[j]=""
        result[name_site]="QUEUE_NAME ="+queName+"\n" +queInfo
    else:
        result.append("[Queue]\n"+"QUEUE_NAME ="+queName+"\n" +queInfo)
    for list_tmp in result:
        if list_tmp:
            result_tmp.append(list_tmp)
    result1="\n".join(result_tmp)
    result2=result1+"\n"
    write_conf(conf_file,result2)

def delQueueA(queName):
    '''
    This function can only deleted the queue  by addQueue() added.
    '''
    conf_file = get_path("JHSCHEDULER_ENV","queues.conf")
    result=read_conf(conf_file)
    conf_length=len(result)
    result_tmp=[]
    exist_name,exist_next_section,name_site,next_section_site=parse_que_conf(result,queName)
    if exist_name:
        if  exist_next_section:
            for i in range(name_site-1,next_section_site):
                result[i]=""
        else:
            for j in range(name_site-1,conf_length):
                print result[j]
                result[j]=""
    for list_tmp in result:
        if list_tmp:
            result_tmp.append(list_tmp)
    result1="\n".join(result_tmp)
    result2=result1+"\n"
    write_conf(conf_file,result2)

def delQueue(*args):
    killAllJob()
    arg_list=str(args[0]).split(",")
    for group_list in arg_list:
        delQueueA(group_list.strip())
    jhadmin_command()

def delQueueAndHost(que,**host):
    killAllJob()
    que_list=str(que[0]).split(",")
    for que_tmp in que_list:
        delQueueA(que_tmp.strip())
    for k,v in host.items():
        hostsConfLib.addOrModifyHost(k,v)
    jhadmin_command()

