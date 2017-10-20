#!/bin/env python
#Filename:myUtils.py


import os
import re
from subprocess import Popen, PIPE
from common import bit_change,checkError,jhadmin_command,get_path,execCommand,get_dir_path
import retry
import time
import psutil

def killAllJob(num=10,timeout=60):
    timeout=int(timeout)
    try_num=int(num)
    try:
        while True:
            retry.checkRestartClusterStatus()
            stdout, stderr, exitcode=execCommand("jhosts",timeout)
            print "this is jhosts info:"
            print stdout, stderr, exitcode
            print "end"
            stdout, stderr, exitcode=execCommand("jctrl kill -u all 0",timeout)
            print "this is jctrl kill -u all 0 info"
            print stdout, stderr, exitcode
            if exitcode == int(0) and stdout == "No unfinished job found\n":
                result=retry.checkClusterStatus()
                if result.replace("\n","")=="cluster_ok":
                    print "'jctrl kill -u all 0' successful"
                    return "ok"
                else:
                    print 'the result of "jctrl kill -u all 0" is "No unfinished job found",jcluster is still not ok'
                    print "'jctrl kill -u all 0' failed"
                    raise RuntimeError
            else:
                try_num = try_num - int(1)
                try:
                    time.sleep(1)
                except KeyboardInterrupt:
                    print ''
                    raise RuntimeError
            if try_num == int(0):
                print 'after executing the command of "jctrl kill -u all 0 " 10 numeber,the job still run'
                raise RuntimeError
    except KeyboardInterrupt:
        print ''
        raise RuntimeError


def getInstalPth():
    '''
    get jhscheduler install dir on linux.
    '''
    try:
        lsf_envdir = os.environ.get('JHSCHEDULER_ENV')
        if lsf_envdir==None or lsf_envdir=='':
            curpath=os.path.normpath(os.path.join(os.getcwd(),os.path.dirname(__file__)))
            epath=os.path.split(curpath)
            lsf_envdir = epath[0] + '/conf'
        return lsf_envdir
    except IndexError:
        print "can not find the environment of JHSCHEDULER_ENV"


def servOnWin(serverIp,option):
    '''
    start or stop jhscheduler on windows.
    E.g:serverIp = "192.168.0.123" option = "stop"
    '''
    n = os.system('/automationtest/execClient -m %s -c "net %s jhscheduler"'%(serverIp,option))

def getSubHost(hosttype,timeout=60):
    '''
    get a specified type(LINUX64/NTX64) of host name used to submit job and the host status is ok.
    E.g: hosttype = 'NTX64'
    '''
    timeout=int(timeout)
    stdout, stderr, exitcode=execCommand("jhdshosts list",timeout)
    try:
        host_list=re.findall(r'\bHost:\s*(.+)\s*\n',stdout)
        type_list=re.findall(r'\s*\bType\s*=\s*(.*)\s*\n',stdout)
        stat_list=re.findall(r'\s*\bStatus\s*=\s*(.*)\s*\n',stdout)
    except:
        raise IndexError("the output")
    host_num=len(host_list)
    host_tmp=[]
    right_host=[]
    if host_list and type_list and stat_list:
        for i in range(0,host_num):
            if type_list[i].upper() == hosttype.upper() and stat_list[i].upper() == "OK":
                host_tmp.append(host_list[i])
        if host_tmp:
            for list_tmp in host_tmp:
                stdout1, stderr1, exitcode1=execCommand("jhosts %s"%list_tmp,timeout)
                #print exitcode
                stat_tmp=re.findall(r'\s*\bStatus\s*=\s*(.+)\s*\n',stdout1)
                if stat_tmp[0].upper()=="OK":
                    right_host.append(list_tmp)
            if len(right_host)>0:
                return right_host[0]
            else:
                return right_host
    else:
        raise IndexError("cannot find this kind of host in the output of 'jhhost list'")

def getSubQueue(timeout=60):
    '''
    get a queue and submit a job to the queue.
    '''
    cmd = "jqueues"
    timeout=int(timeout)
    stdout, stderr, exitcode=execCommand(cmd,timeout)
    #print exitcode
    que_list=re.findall(r'\s*\bQueue:\s*(.+)\s*\n',stdout)
    que_stat=re.findall(r'\s*\bStatus\s*=\s*(.+)\s*\n',stdout)
    que_len=len(que_stat)
    que=[]
    if que_stat:
        for i in range(0,que_len):
            if que_stat[i] == "Open:Active":
                que.append(que_list[i])
    if que:
        return que[0]
    else:
        return que

def containOneKeyword(result,keyWord):
    '''
    checks the result should contain keyword.
    '''
    tmp = result.replace('\n','')
    key = re.findall(r'\b%s\b'%keyWord,tmp)
    tmp1=" ".join(result.split('\n'))
    key1 = re.findall(r'\b%s\b'%keyWord,tmp1)
    if key != [] or key1 !=[]:
        return "contain the keyword"
    else:
        raise checkError("not contain")

def containTwoKeyword(result,keyWord1,keyWord2):
    '''
    checks the result should contain keyword1 and keyword2.
    '''
    tmp=" ".join(result.split('\n'))
    key1 = re.findall(r'\b%s\b'%(keyWord1),tmp)
    key2 = re.findall(r'\b%s\b'%(keyWord2),tmp)
    if key1 != [] and key2 != []:
        return "contain the two keywords"
    else:
        raise checkError("not contain")

def preSuite(conf_path):
    try:
        os.environ['JHSCHEDULER_TOP']
    except Exception as e:
        print "Error:please check the environment of JHSCHEDULER_TOP"
        raise e
    try:
        os.environ['AUTOTEST_TOP']
    except Exception as e:
        print "Error:please check the environment of AUTOTEST_TOP"
        raise e
    try:
        conf_file=get_dir_path('AUTOTEST_TOP',conf_path)
    except IndexError:
        print "can not find the file of %s"%conf_path
        raise NameError
    killAllJob()
    backconf("oldconf")
    jhadmin_command()
    copyConfFile(conf_file)
    jhadmin_command()
    print "preSuite successed"

def preTest():
    killAllJob()
    backconf("suitconf")
    jhadmin_command()
    print "preTest successed"

def postSuite():
    try:
        os.environ['JHSCHEDULER_TOP']
    except Exception as e:
        print "Error:please check the environment of JHSCHEDULER_TOP"
        raise e
    try:
        os.environ['AUTOTEST_TOP']
    except Exception as e:
        print "Error:please check the environment of AUTOTEST_TOP"
        raise e
    killAllJob()
    recoverconf(conf_name="oldconf")
    jhadmin_command()
    killDefault()
    print "postSuite successed"

def postJadminSuite(timeout=60):
    try:
        os.environ['JHSCHEDULER_TOP']
    except Exception as e:
        print "Error:please check the environment of JHSCHEDULER_TOP"
        raise e
    try:
        os.environ['AUTOTEST_TOP']
    except Exception as e:
        print "Error:please check the environment of AUTOTEST_TOP"
        raise e
    killAllJob()
    stdout, stderr, exitcode=execCommand("su jhadmin -c 'jadmin hopen all'", timeout) 
    stdout1, stderr1, exitcode1=execCommand("su jhadmin -c 'jadmin qopen all'", timeout) 
    stdout2, stderr2, exitcode2=execCommand("su jhadmin -c 'jadmin qact all'", timeout)
    if exitcode or exitcode1 or exitcode2:
        print "the err code of postJadminSuite is %s,%s,%s"%(exitcode,exitcode1,exitcode2) 
    recoverconf(conf_name="oldconf")
    jhadmin_command()
    print "postSuite successed"

def preSuiteBack():
    try:
        os.environ['JHSCHEDULER_TOP']
    except Exception as e:
        print "Error:please check the environment of JHSCHEDULER_TOP"
        raise e
    try:
        os.environ['AUTOTEST_TOP']
    except Exception as e:
        print "Error:please check the environment of AUTOTEST_TOP"
        raise e
    killAllJob()
    backconf("oldconf")
    jhadmin_command()
    print "preSuitBack successed"

#def postSingleNodeSuite(cmd):
#    killAllJob()
#    recoverconf(conf_name="oldconf")
#    jhadmin_command()
#    killDefault()
#    print "postSuite successed"


def postTest():
    killAllJob()
    recoverconf(conf_name="suitconf")
    jhadmin_command()
    print "postTest successed"

def backconf(conf_name):
    '''
    backup configuration file.
    '''
    try:
        installdir = os.environ.get('JHSCHEDULER_TOP')
    except IndexError:
        return "cannot find the environment of JHSCHEDULER_TOP"
    backup = os.path.exists("%s/%s"%(installdir,conf_name))
    backupfile = "cp -rp %s/conf %s/%s"%(installdir,installdir,conf_name)
    if False == backup:
        right1=os.system(backupfile)
        if right1!=0:
            print "backup the conf fail"
        else:
            print "backup the conf successed"
    else:
        print "error:backup configuration file already exists."

def mvConf(string):
    path =str(string).replace('\n','')
    try:
        installdir = os.environ.get('JHSCHEDULER_TOP')
    except IndexError:
        return "cannot find the environment of JHSCHEDULER_TOP"
    backup =os.path.exists("%s"%(path))
    if  True == backup:
        right2=os.system("\cp -rp  %s/*  %s/conf/"%(path,installdir))
        if right2!=0:
            print "mvconf function:back the conf failed"
        else:
            print "mvconf function:back the conf successed"
        #jhadmin_command()
    else:
        print "error:there is no backup configuration file."

def recoverconf(conf_name):
    '''
    restore the configuration file, kill all jobs and restart cluster .
    '''
    try:
        installdir = os.environ.get('JHSCHEDULER_TOP')
    except IndexError:
        return "cannot find the environment of JHSCHEDULER_TOP"
    backup = os.path.exists("%s/%s"%(installdir,conf_name))
    if  True == backup:
        result2=os.system("\cp -rp  %s/%s/*  %s/conf/"%(installdir,conf_name,installdir))
        result3=os.system("rm -rf %s/%s"%(installdir,conf_name))
        if result2 !=0 or result3!=0:
            print "can not remove %s"%conf_name
        else:
            print "remove %s successful"%conf_name 
    else:
        print "error:there is no %s file."%conf_name

def copyConfFile(conf_file):
    conf_file =str(conf_file).replace('\n','')
    try:
        installdir = os.environ.get('JHSCHEDULER_TOP')
    except IndexError:
        return "cannot find the environment of JHSCHEDULER_TOP"
    if os.path.isfile:
        right2=os.system("\cp -rp  %s/.  %s/conf/"%(conf_file,installdir))
        if right2!=0:
            print "copy the file of %s failed"%conf_file
        else:
            print "copy the file of %s successed"%conf_file
        #os.popen("jhscheduler restart")
    else:
        print "the dir of %s is not exist"%conf_file

def readyTest():
    '''
    restore the configuration file, kill all jobs and restart cluster .
    '''
    #jhadmin_command()
    print "begin checkRestartClusterStatus"
    retry.checkRestartClusterStatus() 
    print "end checkRestartClusterStatus"
    print "begin killAllJob"
    killAllJob()
    print "end killAllJob"
    print "readyTest successed"    

def endTest():
    '''
    restore the configuration file, kill all jobs and restart cluster .
    '''
    #jhadmin_command()
    killAllJob()
    print "endTest successed"    

def getCurrentTime():
    '''
    get the current system time
    '''
    cmd = 'date +%H:%M'
    tmp = Popen(cmd,stdout = PIPE, stderr = PIPE, shell = True)
    output = tmp.communicate()
    if output[1] != '':
        #print output[1]
        raise RuntimeError
    else:
        return output[0]

def normalPath(path):
    try:
        return os.path.abspath(path.replace('/', os.sep))
    except ValueError:  # http://ironpython.codeplex.com/workitem/29489
        return os.path.normpath(path.replace('/', os.sep))


def delFile(path):
    path =normalPath(path)
    backup  =os.path.exists("%s"%(path))
    if True ==backup:
        print "the dir is %s"%path
        result=os.remove(path)
        if result:
            print "'rm -rf %s' failed"%path
        else:
            print "'rm -rf %s' successed"%path
    else:
        print "error:there is no such file"


def compareString(str1,str2):
    '''
    Compare the two objects str1 and str2 and return an string(equal or unequal).
    '''
    result =  cmp(str(str1),str(str2))

    if result == 0:
        return "equal"
    else:
        return "unequal"

def compareResValue(res1,res2):
    res1=str(res1)
    res2=str(res2)
    res1Value=bit_change(res1)
    res2Value=bit_change(res2)
    if res1Value and res2Value:
        result =  int(res1Value) - int(res2Value)
        if result == 0:
            return "equal"
        elif result >0:
            return "greater"
        else:
            return "less"
    else:
        raise checkError("the format of param is error")


def checkRusageValue(total,reserved,used,checkRange=5):
    '''
    this function can check the value of the resource reservation within a certain range.
    '''
    checkRange = int(checkRange)
    print str(total)
    print str(used)
    print str(reserved)
    totalValue=bit_change(str(total))
    usedValue=bit_change(str(used))
    reservedValue=bit_change(str(reserved))
    if (totalValue > int(-1)) and (usedValue > int(-1))and (reservedValue > int(-1)):
        res_compare=(totalValue - usedValue - reservedValue)
        if abs(res_compare) <= checkRange :
            return "equal"
        else:
            raise checkError("unequal")
    else:
        raise checkError("the format of param is error")

def getFileDir(env="AUTOTEST_TOP"):
    try:
        path=os.getenv(env)
        path=normalPath(path)
        if path:
            return path
        else:
            print "The environment %s is None"%env
    except:
        print "Cannot get the specifical %s"%env

def getSbinPath(env="JHSCHEDULER_TOP"):
    path_tmp=getFileDir(env)
    path=os.path.join(path_tmp,'sbin')
    return path 

def delOutputFile():
    killAllJob() 
    tmp_dir=getFileDir()
    dir=tmp_dir+'/'+'spooler/output/'
    try:
        path=normalPath(dir)
        #print esub_file
        for list in os.listdir(path):
            file=os.path.join(dir,list)
            if os.path.isfile(file):
                os.remove(file)
            else:
                print "remove the %s failed"%file
    except:
        print "the %s is not exist"%dir

def getString(var):
    print var
    return var



def runCommand(cmd_args, timeout=60, env=None, logger=None):
    timeout=int(timeout)
    stdout, stderr, exitcode=execCommand(cmd_args, timeout)
    print "the result of runCommand is \nstdout=%s\nstderr=%s\nexitcode=%s"%(stdout, stderr, exitcode)
    if stderr:
        print exitcode
        stderr=stderr.strip()
        return stderr
    else:
        stdout=stdout.strip()
        return stdout

def runCommandA(cmd_args, timeout=60, env=None, logger=None):
    timeout=int(timeout)
    out=list[0]
    stdout, stderr, exitcode=execCommand(cmd_args, timeout)
    print "the result of runCommand is \nstdout=%s\nstderr=%s\nexitcode=%s"%(stdout, stderr, exitcode)
    out[0]=stderr
    out[1]=stdout
    out[2]=exitcode
    return out

def killJob(timeout=60):
    timeout=int(timeout)
    killAllJob(timeout)
    #stdout, stderr, exitcode=execCommand("jctrl kill -u all 0",timeout)
    #print result
    #if exitcode!=0:
    #    print "excute the command of 'jctrl kill -u all 0' failed"
    #else:
    #    print "excute the command of 'jctrl kill -u all 0' successed"

def removeEsub():
    killAllJob() 
    dir=getSbinPath()
    esub_path=os.path.join(dir,'esub')
    try:
        esub_file=normalPath(esub_path)
        #print esub_file
        if os.path.isfile(esub_file):
            os.remove(esub_file)
        else:
            print "remove the %s failed"%esub_file
    except:
        print "the %s is not exist"%esub_path

def removeEsubFile():
    dir=getSbinPath()
    esub_path=os.path.join(dir,'esub')
    try:
        esub_file=normalPath(esub_path)
        #print esub_file
        if os.path.isfile(esub_file):
            os.remove(esub_file)
        else:
            print "remove the %s failed"%esub_file
    except:
        print "the %s is not exist"%esub_path

def peekJob(string):
    cmd = string.replace('\n','')
    stdout, stderr, exitcode=execCommand(cmd)
    return exitcode,stdout

def usedUt(host,file,ut_stat,timeout=60):
    print "begin usedUt"
    timeout=int(timeout)
    cmd=file.replace('\n','')+"&"
    exitcode=os.system(cmd)
    if exitcode:
        raise RuntimeError
    i=int(0)
    while i<timeout:
        print i
        stdout, stderr, exitcode=execCommand("jhosts -l %s"%host,timeout)
        ut_tmp=re.findall(r'\bResource.ut\s*=\s*Total:\s*(.+)\s*,\s*Reserved:',stdout)  
        print "ut_tmp %s"%ut_tmp
        print  "ut_stat %s"%ut_stat
        ut=ut_tmp[0].strip().strip("%")
        ut_stat=str(ut_stat).strip().strip("%")
        if  int(ut)> int(ut_stat):
           try:
               time.sleep(10)
           except KeyboardInterrupt:
               raise RuntimeError
           return ut_tmp
        else:
           try:
               time.sleep(1)
           except KeyboardInterrupt:
               raise RuntimeError
           i=i+1

def checkUtValue(host,ut_stat,check_time=60):
    check_time=int(check_time)
    i=int(0)
    while i<check_time:
        stdout, stderr, exitcode=execCommand("jhosts -l %s"%host)
        ut_tmp=re.findall(r'\bResource.ut\s*=\s*Total:\s*(.+)\s*,\s*Reserved:',stdout)  
        ut=ut_tmp[0].strip().strip("%")
        print ut
        ut_stat=str(ut_stat).strip().strip("%")
        if  int(ut)> int(ut_stat):
           try:
               time.sleep(10)
           except KeyboardInterrupt:
               print "KeyboardInterrupt"
               raise RuntimeError
           return ut_tmp
        else:
           try:
               time.sleep(2)
           except KeyboardInterrupt:
               print "KeyboardInterrupt"
               raise RuntimeError
           i=i+1

def compareUt(ut1,ut2):
        if ut1 and ut2:
            ut1=str(ut1).strip().strip("%")
            print ut1
            ut2=str(ut2).strip().strip("%")
            if  int(ut1)> int(ut2):
               return True
            else:
               return False
        else:
            raise RuntimeError

def checkUt(host):
    host="jhosts -l %s"%host
    stdout, stderr, exitcode=execCommand(host)
    if stderr:
        raise RuntimeError
    else: 
        host_tmp=re.findall(r'\bHost:\s*(.+)\s*\n',stdout)
        ut_tmp=re.findall(r'\bResource.ut\s*=\s*Total:\s*(.+)\s*,\s*Reserved:',stdout) 
        if ut_tmp:
            return ut_tmp[0]
        else:
            return ut_tmp

def killUtProc(cmd,timeout=60):
    timeout=int(timeout)
    cmd_tmp=cmd.replace('\n','')
    while True: 
        cmd1="ps -ef|grep %s "%cmd_tmp+" -wc"
        stdout0, stderr0, exitcode0=execCommand(cmd1,timeout)
        num=int(stdout0)-int(2)
        if num>int(0):
            cmd="ps -ef|grep %s |awk '{print $2}'|sed -n '1p'"%cmd_tmp
            stdout, stderr, exitcode=execCommand(cmd)
            if exitcode:
                raise RuntimeError
            else:
                pid=stdout.replace('\n','').strip()
                killProcTree(pid,includingParent=True)
        else:
            return

def killProcTree(pid, includingParent=True, async=False, logger=None):
    """
    Kill the children of the given process and the process if includingParent is true
    :param pid: Specifies PID, of which children are to kill
    :param includingParent: Specifies if kill the given process
    :return: None
    """

    import psutil
    pid=int(pid)
    parent = psutil.Process(pid)
    children = parent.children(recursive=True)
    killnumstr = os.getenv('KILL_CHILDREN_LEVEL')
    if killnumstr is None:
        procsToKill = children[0:]

    else:
        try:
            killnum = int(killnumstr)
        except Exception:
            killnum = 2

        # FIXME: Simply treat each process has only one son
        procsToKill = children[0: killnum]

    if includingParent:
        procsToKill.append(parent)

    killProcTimeout = os.getenv('KILL_PROC_TIMEOUT')
    try:
        killProcTimeout = int(killProcTimeout)
    except Exception:
        killProcTimeout = 10

    if not async:
        try:
            _killProcTree(procsToKill, killProcTimeout)
        except Exception as ex:
            if logger is not None:
                logger.error("Failed to kill processes: %s", ex)
    else:
        import threading
        killThread = threading.Thread(target=_killProcTree, args=(procsToKill, killProcTimeout))
        killThread.start()


def _killProcTree(procs, timeout):

    if procs is None:
        return

    for proc in procs:
        try:
            proc.terminate()
        except Exception as ex:
            print "terminate error"
    goneList, aliveList = psutil.wait_procs(procs, timeout)
    if aliveList is None:
        return

    for proc in aliveList:
        try:
            proc.kill()
        except Exception as ex:
            print "kill proc failed"


def postJadmin(timeout=60):
    timeout=int(timeout)
    killAllJob()
    stdout, stderr, exitcode=execCommand("su jhadmin -c 'jadmin hopen all'", timeout)
    stdout1, stderr1, exitcode1=execCommand("su jhadmin -c 'jadmin qopen all'", timeout)
    stdout2, stderr2, exitcode2=execCommand("su jhadmin -c 'jadmin qact all'", timeout)
    if exitcode or exitcode1 or exitcode2:
        print "the error info of postJadmin is %s"%stderr

def shouldAlmostEqual(num1,num2,num3):
    try:
        num1=float(num1)
        num2=float(num2)
        num3=float(num3)
    except ValueError:
        print "the input value type of '%s %s %s' is not float or int"%(num1,num2,num3)
        raise RuntimeError   
    if abs(int(num1)-int(num2))<=int(num3):
        print "equal"
        return "close"
    else:
        print "Not equal"
        raise RuntimeError

def shouldLow(num1,num2):
    try:
        num1=float(num1)
        num2=float(num2)
    except ValueError:
        print "the input value type of '%s %s %s' is not float or int"%(num1,num2,num3)
        raise RuntimeError
    if num1<=num2:
        print "low"
        return "close"
    else:
        print "the %s is not lower than the %s"%(num1,num2)
        raise RuntimeError

def killUt(cmd):
    killUtProc(cmd)

def killDefault():
   result1=os.system("ps -ef|grep pi.sh|awk '{print $2}'|xargs kill -9")
   print result1
   result2=os.system("ps -ef|grep bc|awk '{print $2}'|xargs kill -9")
   print result2
   result3=os.system("ps -ef|grep testMlock|awk '{print $2}'|xargs kill -9")
   print result3


def compareMem(master,slave,timeout=60):
    '''
    the first host must be the one that run the autotest.
    '''
    print "begin compareMem"
    i=int(0)
    timeout=int(timeout)
    while True:
        cmd1="jhosts -l %s"%master
        stdout, stderr, exitcode=execCommand(cmd1,timeout)
        cmd2="jhosts -l %s"%slave
        stdout2, stderr2, exitcode2=execCommand(cmd2,timeout)
        print stderr,stderr2
        if stderr or stderr2:
            raise RuntimeError
        else: 
            ut_tmp=re.findall(r'\bResource.mem\s*=\s*Total:\s*(.+)\s*,\s*Reserved:',stdout)
            ut_tmp2=re.findall(r'\bResource.mem\s*=\s*Total:\s*(.+)\s*,\s*Reserved:',stdout2)
            checkRange = int(5)
            ut1=bit_change(str(ut_tmp[0]))
            ut2=bit_change(str(ut_tmp2[0]))
            if (ut1 > int(-1)) and (ut2 > int(-1)):
                res_compare=(ut2-ut1)
                if res_compare >=int(0):
                    if res_compare>checkRange:
                       return slave,master
                    else:
                       if i==int(0):
                           resumeMem("50")
                       try:
                           time.sleep(2)
                       except KeyboardInterrupt:
                           raise RuntimeError
                else:
                    if res_compare<int(-checkRange):
                       return master,slave
                    else:
                       if i==int(0):
                           resumeMem("50")
                       try:
                           time.sleep(2)
                       except KeyboardInterrupt:
                           raise RuntimeError
            else:
                raise checkError("the format of param is error")
            i=i+1

def resumeMem(num):
    auto_top=getFileDir() 
    cmd=auto_top+'/spooler/input/testMlock'
    result1=os.system("%s %s&"%(cmd,num))
    if result1:
        print "exec %s failed"%cmd

def getSubString(str,start,end=None):
    start=int(start)
    if end:
        end=int(end)
        return str[start:end]
    else:
        return str[start:]

def jadminJhdsSched(timeout=60):
    timeout=int(timeout)
    outa,outb,outc=execCommand('cat /apps/4.0/unischeduler/conf/hosts.conf')
    print outa,outb,outc
    stdouta, stderra, resulta=execCommand("jservice list",timeout)
    print "jservice listxx:begin"
    print stdouta, stderra, resulta
    print "jhostcc:begin"
    stdoutc, stderrc, resultc=execCommand("jhosts -l",timeout)
    print stdoutc, stderrc, resultc
    stdout, stderr, result1=execCommand("echo y|jadmin jhdsreconfig",timeout)
    #print result1
    print "this g2 begin"
    print stdout, stderr, result1
    print 'this g2 end'
    if result1 !=0:
        print "execute jadmin jhdsreconfig failed"
        raise RuntimeError
    else:
        print "execute jadmin jhdsreconfig sucessed"
    stdout, stderr, result2=execCommand("echo y|jadmin schedreconfig",timeout)
    #print result2
    print "this g3 begin"
    print stdout, stderr, result2
    print 'this g3 end'
    if result2 !=0:
        print "execute jadmin schedreconfig failed"
        raise RuntimeError
    else:
        print "execute jadmin schedreconfig sucessed"
    stdoutb, stderrb, resultb=execCommand("jservice list",timeout)
    stdoutd, stderrd, resultd=execCommand("jservice list",timeout)
    print "jservice listyy:begin"
    print stdoutb, stderrb, resultb
    print "jhostdd:begin"
    stdoutd, stderrd, resultd=execCommand("jhosts -l",timeout)
    print stdoutd, stderrd, resultd
    

def jadminJhds(timeout=60):
    timeout=int(timeout)
    stdout, stderr, result1=execCommand("echo y|jadmin jhdsreconfig",timeout)
    #print result1
    if result1 !=0:
        print "execute jadmin jhdsreconfig failed"
        raise RuntimeError
    else:
        print "execute jadmin jhdsreconfig sucessed"

def jadminSched(timeout=60):
    timeout=int(timeout)
    stdout, stderr, result2=execCommand("echo y|jadmin schedreconfig",timeout)
    #print result2
    if result2 !=0:
        print "execute jadmin schedreconfig failed"
        raise RuntimeError
    else:
        print "execute jadmin schedreconfig sucessed"

def jserviceRestartAll(timeout=60):
    timeout=int(timeout)
    stdout, stderr, result=execCommand("echo y|jservice restart all",timeout)
    #print result2
    if result !=0:
        print "execute jservice restart all failed"
        raise RuntimeError
    else:
        print "execute jservice restart all sucessed"

def stringEqual(str1,str2):
    print str1
    print str2
    if str1==str2:
       print "equal"
       return 'equal'
    else:
       print 'unequal'
       raise RuntimeError

def checkVersion(cmd,timeout=60):
    time=int(timeout)
    cmd=cmd.replace("\n","")
    stdout, stderr, exitcode=execCommand(cmd,time)
    if exitcode!=0:
        print "execute the command of 'jversion' failed "
        raise RuntimeError
    else: 
        version_info=re.findall(r'JH UniScheduler 4.\d{1},\s[a-zA-Z]+\s\d{2}\s\d{4}\nCopyright \(c\) 2017 Beijing Jing Hang Rui Chuang Software Co., Ltd. All Right Reserved.',stdout)
        if version_info:
            print version_info
            return version_info[0]
        else:
            print "the version info is %s"%version_info
            raise RuntimeError

def checkJhdsVersion(cmd,timeout=60):
    time=int(timeout)
    cmd=cmd.replace("\n","")
    stdout, stderr, exitcode=execCommand(cmd,time)
    if exitcode!=0:
        print "execute the command of 'jservice version' failed "
        raise RuntimeError
    else: 
        version_info=re.findall(r'JHDS 4.\d{1},\s[a-zA-Z]+\s\d{2}\s\d{4}\nCopyright \(c\) 2017 Beijing Jing Hang Rui Chuang Software Co., Ltd. All Right Reserved.',stdout)
        if version_info:
            print version_info
            return version_info[0]
        else:
            print "the version info is %s"%version_info
            raise RuntimeError




def getServicePid(serv,cmd='jservice list',timeout=60):
    timeout=int(timeout)
    cmd=cmd.replace("\n","")
    stdout, stderr, exitcode=execCommand(cmd,timeout)
    if exitcode == 0:
        service_info=stdout.strip("\n").strip("").split('Service:')
        print service_info
        length=len(service_info)
        j=0
        #print length
        for i in range(0,length):
            if serv in service_info[i]:
                print service_info[i]
                pid=re.findall(r'\n\s*PID\s*=\s*(\d+)',service_info[i])
                print pid
                if pid:
                    return pid[0].strip("\n").strip(" ")
                else:
                    return pid
            else:
                j=j+1
        if j==length:
            print "execute the command of %s failed "%cmd
            raise RuntimeError
    else: 
        print "execute the command of %s failed "%cmd
        raise RuntimeError

def checkServicePidChange(serv,pid,checkTime=60):
    checktime = int(checkTime)
    try:
        while True:
            print checkTime
            pid1=getServicePid(serv)
            print pid,pid1
            if pid and pid1 and pid != pid1:
                print "old pid:%s,new pid:%s"%(pid,pid1)
                return pid1
            else:
                time.sleep(1)
                checktime =checktime-int(1)
                print checktime
            if checktime == int(0):
                print "sched pid not change"
                raise RuntimeError
    except KeyboardInterrupt:
        print ''
        raise RuntimeError
  
def low(string1):
    if string1:
        return string1.lower()
    else:
        return string1
