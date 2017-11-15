#!/bin/env python
#FileName:dealconfig

import os
import ConfigParser
import re
import platform
from subprocess import Popen,PIPE
from threading import Timer
import psutil

def get_path(path,confName):
    lsf_envdir = os.environ.get(path)#Get the path of configuer files
    try:
        #conf_file = os.path.join(lsf_envdir,"hosts.conf")
        conf_file = os.path.join(lsf_envdir,confName)
        if os.path.isfile(conf_file) and os.access(conf_file,os.R_OK) and os.access(conf_file, os.W_OK):
            return conf_file
        else:
            print "Please confirm the file of %s is readable and writable" % (conf_file)
            raise NameError
    except AttributeError:
        print "Please source environment variable of JH Scheduler or AUTOTEST_TOP!"
        raise NameError

def get_dir_path(path,confName):
    lsf_envdir = os.environ.get(path)
    conf_file = os.path.join(lsf_envdir,confName)
    if os.path.isdir(conf_file):
        readDir(conf_file) 
        return conf_file
    else:
        print "the dir of %s is not exist" % (conf_file)
        raise NameError

def readDir(dir):
    for lists in os.listdir(dir):
        path=os.path.join(dir,lists)
        print path
        if os.path.isdir(path):
            readDir(path)
        else:
            if os.path.isfile(path) and os.access(path,os.R_OK) and os.access(path, os.W_OK):
                continue
            else:
                print "Please confirm the file of %s is readable and writable" % (path)
                raise NameError

def isWindows():
    if platform.system().startswith("Win"):
        return True

    return False

def execCommand(cmd_args, timeout=60, env=None, logger=None):
    """
    Execute given command, and return stdout, stderr, exit_code
    :param cmd_args: Command and args array
    :param timeout: Return directly after wait for the given period of time
    :param env
    :param logger
    :return: Tuple of stdout, stderr, exit_code
    """

    if isWindows():
        proc = Popen(cmd_args, stdout=PIPE, stderr=PIPE, shell=True, env=env, close_fds=False)
    else:
        proc = Popen(cmd_args, stdout=PIPE, stderr=PIPE, shell=True, env=env, close_fds=True)

    timer = None
    timeout=int(timeout)
    if timeout > 0:
        timer = Timer(timeout, _terminateProc, [proc, cmd_args, logger])
        timer.start()

    (stdout, stderr) = proc.communicate()

    # Finished before timeout, then cancel the timer
    if timeout > 0:
        timer.cancel()

    return stdout, stderr, proc.returncode

def _terminateProc(proc, cmd_args=None, logger=None):
    """
    Terminate the given process
    :param proc: Specifies process to terminate
    :return: None
    """

    try:
        if proc.poll() is None:
            killProcTree(proc.pid)
    except:
        pass

    if cmd_args is not None:
        msg = "The process was killed due to timeout (pid: %d, cmd_args: %s)." % (proc.pid, cmd_args)
    else:
        msg = "The process was killed due to timeout (pid: %d)." % proc.pid

    if logger is not None:
        logger.error(msg)

def killProcTree(pid, includingParent=True):
    """
    Kill the children of the given process and the process if includingParent is true
    :param pid: Specifies PID, of which children are to kill
    :param includingParent: Specifies if kill the given process
    :return: None
    """

    parent = psutil.Process(pid)
    children = parent.children(recursive=True)
    for child in children:
        child.kill()

    psutil.wait_procs(children, timeout=int(5))
    if includingParent:
        parent.kill()
        parent.wait(5)

def get_command_param(str_result,command):
    '''
    set command basic info.
    '''
    try:
        command_parm_dict={}
        command_all_info=re.findall(r'\b(.+)\s*=\s*(.+)\s*\n',str_result)
        for command_parm in command_all_info:
            key=command_parm[0].strip()
            value=command_parm[1].strip()
            command_parm_dict[key]=value
        return command_parm_dict
    except IndexError:
        print 'the output format of %s is error'%command

def get_res_use_or_threshold(str_result,command,key):
    try:
        res_sched={}
        res_stop={}
        res_total={}
        res_resvd = {}
        res_sched_tmp=re.findall(r'\bResource.(.+) = LoadSched: (.+) , LoadStop: .+\s*\n',str_result)
        res_stop_tmp=re.findall(r'\bResource.(.+) = LoadSched: .+ , LoadStop: (.+)\s*\n',str_result)
        res_total_tmp=re.findall(r'\bResource.(.+) = Total: (.+) , Reserved: .+\s*\n',str_result)
        res_resvd_tmp=re.findall(r'\bResource.(.+) = Total: .+ , Reserved: (.+)\s*\n',str_result)
        res_sched=strip_list_blank(res_sched_tmp,command,"LoadSched")
        res_stop = strip_list_blank(res_stop_tmp,command,"LoadStop")
        res_total = strip_list_blank(res_total_tmp,command,"Total")
        res_resvd =strip_list_blank(res_resvd_tmp,command,"Reserved")
        #for k,v in res_resvd.items():
        #    print "key=%s,value=%s"%(k,v)
        if str(key)=="sched":
            return res_sched
        if str(key)=="stop":
            return res_stop
        if str(key)=="total":
            return res_total
        if str(key)=="resvd":
            return res_resvd

    except IndexError:
        print 'the output format of %s is error'%command


def strip_list_blank(params_list,command,param):
    params_dict={}
    if params_list:
        for list_unit in params_list:
            key=list_unit[0].strip()
            value=list_unit[1].strip()
            params_dict[key]=value
    #else:
    #    print "the output of %s has no resource %s info"%(command,param)
    return params_dict


def get_value(key,param_dict):
    if key in param_dict.keys():
        return param_dict[key]
    else:
        return ""

def bit_change(bit_param):
    param = re.match(r'([0|1-9]+\.[0-9]+|[0-9]+)\s*([A-Za-z]*)',bit_param)
    bit_value=param.group(1)
    bit_unit = param.group(2)
    print bit_value
    print bit_unit
    bit_param_value= int(-1)
    if bit_value>int(-1) :
        if bit_unit == 'K' or bit_unit == 'Kbytes':
            bit_param_value=float(bit_value)/1024
        elif bit_unit == 'G' or bit_unit == 'Gbytes':
            bit_param_value = float(bit_value)*1024
        elif bit_unit == 'T' or bit_unit == 'Tbytes':
            bit_param_value = float(bit_value)*1024*1024
        elif bit_unit == 'M' or bit_unit=='Mbytes':
            bit_param_value=float(bit_value)
        elif bit_unit == 'B' or bit_unit == 'Bbytes':
            bit_param_value=float(bit_value)/1024/1024
        else:
            bit_param_value=float(bit_value)
    else:
        print "the format of param is error"
    return bit_param_value

def jhadmin_command(timeout=60):
    timeout=int(timeout)
    stdouta, stderra, resulta=execCommand("jservice list",timeout)
    print "jservice list:begin"
    print stdouta, stderra, resulta
    stdout, stderr, result1=execCommand("whoami",timeout)
    print "who am i:%s, %s, %s"%(stdout, stderr, result1)
    stdout, stderr, result1=execCommand("echo y|jadmin jhdsreconfig",timeout)
    #print result1
    print "this g0 begin"
    print stdout, stderr, result1
    print 'this g0 end'
    if result1 !=0:
        print "execute jadmin jhdsreconfig failed"
    else:
        print "execute jadmin jhdsreconfig sucessed"
    stdout, stderr, result2=execCommand("echo y|jadmin schedreconfig",timeout)
    #print result2
    print "this g1 begin"
    print stdout, stderr, result2
    print 'this g1 end'
    if result2 !=0:
        print "execute jadmin schedreconfig failed"
    else:
        print "execute jadmin schedreconfig sucessed"
    
    stdoutb, stderrb, resultb=execCommand("jservice list",timeout)
    print "jservice list:end"
    print stdoutb, stderrb, resultb

def read_conf(conf_dir):
    f=open(conf_dir,'r')
    result=list()
    for line in f.readlines():
        line=line.strip()
        if not len(line) or line.startswith("#"):
            continue
        result.append(line)
    f.close()
    return result

def write_conf(conf_dir,result):
    f=open(conf_dir,'w')
    f.write(result)
    f.close()

def parse_conf(result,section,name):
    conf_length=len(result)
    exist_section=False
    exist_name=False
    section_site=int(-1)
    name_site=int(-1)
    symbol=False
    for i in range(0,conf_length):
        if section== result[i].split()[0]:
            exist_section=True
            section_site=i
            symbol=True
        if symbol and name.strip()==result[i].split()[0]:
            exist_name=True
            name_site=i
            break
        i+=i
    return exist_section,exist_name,section_site,name_site
def parse_que_conf(result,queName):
    conf_length=len(result)
    exist_name=False
    exist_next_section=False
    name_site=int(-1)
    next_section_site=(-1)
    queName_title="QUEUE_NAME="+queName.strip()
    for i in range(0,conf_length):
        if queName_title.strip()==result[i].strip().replace(" ",""):
            exist_name=True
            name_site=i
        elif exist_name and "[Queue]"==result[i].split()[0]:
            exist_next_section=True
            next_section_site=i
            break
        i+=i
    return exist_name,exist_next_section,name_site,next_section_site

class checkError(Exception):
    def __init__(self,errorInfo):
        Exception.__init__(self,errorInfo)
        self.errorInfo = errorInfo

class ConfigRewrite(ConfigParser.ConfigParser):
    def __init__(self,defaults=None):
        ConfigParser.ConfigParser.__init__(self)
    def optionxform(self, optionstr):
        return optionstr

class Config:
    def __init__(self, path):
        self.path = path
        self.section = []
        self.options = []
        self.items = []
        #self.cf = ConfigParser.ConfigParser(allow_no_value=True)
        self.cf = ConfigRewrite()
        self.cf.read(path)
    def get_section(self):
        try:
            self.section=self.cf.sections()
            return self.section
        except ConfigParser.NoSectionError:
            print "there are no sections"

    def get_options(self,sectionName):
        try:
            self.options=self.cf.options(sectionName)
            return self.options
        except ConfigParser.NoOptionError:
            print "there are no options"

    def get_items(self,sectionName):
        self.items=self.cf.items(sectionName)
        return self.items

    def add_section(self,sectionName):
        self.cf.add_section(sectionName)

    def add_options(self,sectionName,options,value=None):
        self.cf.set(sectionName,options,value)

    def del_section(self,sectionName):
        self.cf.remove_section(sectionName)
    def del_options(self,sectionName,options):
        self.cf.remove_option(sectionName,options)

    def write_file(self,path):
        self.cf.write(open(path,"w"))


