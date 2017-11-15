#!/usr/bin/python
#Filename:usersConfLib.py


from common import *
from myUtils import killAllJob
import hostsConfLib 

def addOrModifyUserA(userName,userInfo):
    conf_file = get_path("JHSCHEDULER_ENV","users.conf")
    result=read_conf(conf_file)
    exist_section,exist_name,section_site,name_site=parse_conf(result,"[User]",userName)
    if exist_section and exist_name:
        result[name_site]=userName+" " +userInfo
    elif exist_section and not exist_name:
        result[section_site+2]=result[section_site+2]+"\n"+userName+" " +userInfo
    elif not exist_section and not exist_section:
        user_section="[User]\n"
        user_title="USER_NAME      MAX_JOBS        JL/P\n"
        add_param=user_section+user_title+userName+"  "+userInfo
        result.append(add_param)
    result1="\n".join(result)
    result2=result1+"\n"
    write_conf(conf_file,result2)

def delUserA(userName):
    conf_file = get_path("JHSCHEDULER_ENV","users.conf")
    result=read_conf(conf_file)
    exist_section,exist_name,section_site,name_site=parse_conf(result,"[User]",userName)
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

def addOrModifyUserGroup(groupName,groupMember,userGroupTile):
    #userGroupTile="GROUP_NAME GROUP_MEMBER GROUP_ADMIN USER_SHARES"
    conf_file = get_path("JHSCHEDULER_ENV","users.conf")
    result=read_conf(conf_file)
    exist_section,exist_name,section_site,name_site=parse_conf(result,"[UserGroup]",groupName)
    if exist_section and exist_name:
        result[name_site]=groupName+" " +groupMember
    elif exist_section and not exist_name:
        result[section_site+2]=result[section_site+2]+"\n"+groupName+" " +groupMember
    elif not exist_section and not exist_name:
        user_group_section="[UserGroup]\n"
        add_param=user_group_section+userGroupTile+"\n"+groupName+"  "+groupMember
        result.append(add_param)
    result1="\n".join(result)
    result2=result1+"\n"
    write_conf(conf_file,result2)

def addOrModifyUserGroupA(groupName,groupMember):
    userGroupTile="GROUP_NAME GROUP_MEMBER GROUP_ADMIN USER_SHARES"
    groupMember=str(groupMember).replace('"',"").replace("'","")
    conf_file = get_path("JHSCHEDULER_ENV","users.conf")
    result=read_conf(conf_file)
    exist_section,exist_name,section_site,name_site=parse_conf(result,"[UserGroup]",groupName)
    if exist_section and exist_name:
        result[name_site]=groupName+" " +groupMember
    elif exist_section and not exist_name:
        result[section_site+2]=result[section_site+2]+"\n"+groupName+" " +groupMember
    elif not exist_section and not exist_name:
        user_group_section="[UserGroup]\n"
        add_param=user_group_section+userGroupTile+"\n"+groupName+"  "+groupMember
        result.append(add_param)
    result1="\n".join(result)
    result2=result1+"\n"
    write_conf(conf_file,result2)



def delUserGroupA(groupName):
    print groupName
    conf_file = get_path("JHSCHEDULER_ENV","users.conf")
    result=read_conf(conf_file)
    exist_section,exist_name,section_site,name_site=parse_conf(result,"[UserGroup]",groupName)
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


def modUserGroup(**args):
    #killalljobs = "jctrl kill -u all 0"
    #stdout, stderr, result1=execCommand(killalljobs,timeout=60)
    #if result1 !=0:
    #    print "'jctrl kill -u all 0' failed"
    #else:
    #    print "'jctrl kill -u all 0' successed"
    killAllJob()
    for (k,v) in args.items():
        addOrModifyUserGroupA(k,v)
    jhadmin_command()

def delUserGroup(*args):
    #print type(args)
    #print args
    #print len(args)
    #killalljobs = "jctrl kill -u all 0"
    #stdout, stderr, result1=execCommand(killalljobs,timeout=60)
    #if result1 !=0:
    #    print "'jctrl kill -u all 0' failed"
    #else:
    #    print "'jctrl kill -u all 0' successed"
    killAllJob()
    arg_list=str(args[0]).split(",")
    for group_list in arg_list:
        delUserGroupA(group_list.strip())
    jhadmin_command()

def delUserGroupAndHost(ug,**host):
    killAllJob()
    print ug
    print host
    ug_list=str(ug).split(",")
    for ug_tmp in ug_list:
        print ug_tmp
        delUserGroupA(ug_tmp.strip())
    for k,v in host.items():
        print k
        print v
        hostsConfLib.addOrModifyHost(k,v)
    jhadmin_command()

def modUser(**args):
    killAllJob()
    for (k,v) in args.items():
        addOrModifyUserA(k,v)
    jhadmin_command()

def delUser(*args):
    killAllJob()
    arg_list=str(args[0]).split(",")
    for group_list in arg_list:
        delUserA(group_list.strip())
    jhadmin_command()

def delUserAndHost(user,**host):
    killAllJob()
    user_list=str(user).split(",")
    for user_tmp in user_list:
        delUserA(user_tmp.strip())
    for k,v in host.items():
        hostsConfLib.addOrModifyHost(k,v)
    jhadmin_command()

def delUserAndUserGroupAndHost(user,ug,**host):
    killAllJob()
    user_list=str(user).split(",")
    ug_list=str(ug).split(",")
    for user_tmp in user_list:
        delUserA(user_tmp.strip())
    for ug_tmp in ug_list:
        delUserGroupA(ug_tmp.strip())
    for k,v in host.items():
        hostsConfLib.addOrModifyHost(k,v)
    jhadmin_command()

def delUserAndUserGroup(user,ug):
    killAllJob()
    print user
    print ug
    user_list=str(user).split(",")
    ug_list=str(ug).split(",")
    for user_tmp in user_list:
        delUserA(user_tmp.strip())
    for ug_tmp in ug_list:
        delUserGroupA(ug_tmp.strip())
    jhadmin_command()

