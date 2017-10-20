#!/usr/bin/python
#Filename:hostsConfLib.py


from common import *
from myUtils import killAllJob,removeEsubFile

def addOrModifyHost(hostName,hostInfo):
    hostInfo=str(hostInfo).replace('"',"").replace("'","") 
    conf_file = get_path("JHSCHEDULER_ENV","hosts.conf")
    result=read_conf(conf_file)
    exist_section,exist_name,section_site,name_site=parse_conf(result,"[Host]",hostName)
    if exist_section and exist_name:
        result[name_site]=hostName+" " +hostInfo
    if exist_section and exist_name is False:
        result[section_site+2]=result[section_site+2]+"\n"+hostName+" " +hostInfo
    result1="\n".join(result)
    result2=result1+"\n"
    write_conf(conf_file,result2)

def delHost(hostName):
    conf_file = get_path("JHSCHEDULER_ENV","hosts.conf")
    result=read_conf(conf_file)
    exist_section,exist_name,section_site,name_site=parse_conf(result,"[Host]",hostName)
    if exist_section and exist_name:
        result[name_site]=""
    result1="\n".join(result)
    result2=result1+"\n"
    write_conf(conf_file,result2)

def addOrModifyHostGroup(groupName,groupMember):
    conf_file = get_path("JHSCHEDULER_ENV","hosts.conf")
    result=read_conf(conf_file)
    exist_section,exist_name,section_site,name_site=parse_conf(result,"[HostGroup]",groupName)
    if exist_section and exist_name:
        result[name_site]=groupName+" " +groupMember
    elif exist_section and exist_name is False:
        result[section_site+2]=result[section_site+2]+"\n"+groupName+" " +groupMember
    elif exist_section is False and exist_section is False:
        host_title="[HostGroup]\nGROUP_NAME    GROUP_MEMBER\n"
        add_param=host_title+groupName+"  "+groupMember
        result.append(add_param)
    result1="\n".join(result)
    result2=result1+"\n"
    write_conf(conf_file,result2)

def delHostGroupA(groupName):
    conf_file = get_path("JHSCHEDULER_ENV","hosts.conf")
    result=read_conf(conf_file)
    exist_section,exist_name,section_site,name_site=parse_conf(result,"[HostGroup]",groupName)
    length=len(result)
    if exist_section and exist_name:
        if name_site==length-1 and section_site==length-3:
            result[section_site]=""
            result[section_site+1]=""
            result[name_site]=""
        else:
            result[name_site]=""
    result1="\n".join(result)
    result2=result1+"\n"
    write_conf(conf_file,result2)

def change_host_slot(host1,num1,host2,num2):
    addOrModifyHost(host1,num1)
    addOrModifyHost(host2,num2)
    jhadmin_command()

def modHostInfo(**args):
    killAllJob()
    for (k,v) in args.items():
        addOrModifyHost(k,v)
    jhadmin_command()

def modHostInfoAndDelEsub(**args):
    killAllJob()
    removeEsubFile()
    for (k,v) in args.items():
        addOrModifyHost(k,v)
    jhadmin_command()


    
def modHostGroup(**args):
    killAllJob()
    for (k,v) in args.items():
        addOrModifyHostGroup(k,v)
    jhadmin_command()

def delHostGroup(*args):
    killAllJob()
    arg_list=str(args[0]).split(",")
    for group_list in arg_list:
        delHostGroupA(group_list.strip())
    jhadmin_command()

def delHostGroupAndHost(ug,**host):
    killAllJob()
    print ug
    print host
    ug_list=str(ug).split(",")
    for ug_tmp in ug_list:
        print ug_tmp
        delHostGroupA(ug_tmp.strip())
    for k,v in host.items():
        print k
        print v
        addOrModifyHost(k,v)
    jhadmin_command()

