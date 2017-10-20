#!/bin/env python
#Filename:retry.py


import time
from subprocess import Popen, PIPE
import re
from common import execCommand

def checkHostStatus(hostName,status,checkTime=60):
    '''
    check host status in the special time.
    E.g:hostName = 'win7' status = 'closed' checkTime = 10
    '''
    checktime = int(checkTime)
    cmd = "jhosts -l "+hostName
    try:
        while True:
            stdout, stderr, exitcode=execCommand(cmd,timeout=60)
            #print exitcode
            print stdout
            result=re.findall(r'\s+\bStatus\s*=\s*(.+)\s*\n',stdout)
            if result and result[0] == status:
                return result[0]
            else:
                time.sleep(1)
                checktime -= int(1)
            if checktime == int(0):
                print "check host status error"
                raise RuntimeError
    except KeyboardInterrupt:
        print ''
        raise RuntimeError

def checkJobStatus(jobId,status,checkTime=60):
    '''
    check job status in the special time.
    E.g:jobId = 101 status = 'RUN' checkTime = 5
    '''
    cmd = "jjobs -l " + str(jobId)
    checktime = int(checkTime)
    try:
        while True:
            stdout, stderr, exitcode=execCommand(cmd,timeout=60)
            print stdout
            result = re.findall(r'\s+\bStatus\s*=\s*(.+)\s*\n',stdout)
            print result
            if result and result[0] == status:
                return result[0]
            else:
                time.sleep(1)
                checktime -= int(1)
            if checktime == int(0):
                print "check job status fail"
                raise RuntimeError
    except KeyboardInterrupt:
        print ''
        raise RuntimeError     

def checkClusterStatus(hoststatus='ok',checkTime=60):
    '''
    check cluster all of hosts status is ok in the special time.
    '''
    spendTime = int(checkTime)
    try:
        while True:
            print spendTime
            stdout0, stderr0, exitcode0=execCommand("jjobs -u all",timeout=60)
            print "this is jjobs -u all output:begin"
            print stdout0, stderr0, exitcode0
            print "jjobs -u all:end"
            stdout, stderr, exitcode=execCommand("jhosts stat -l",timeout=60)
            print "jhosts stat -l:\n%s"%stdout
            stat_list_a=re.findall(r'\s+\bStatus\s*=\s*(.*)\s*\n',stdout)
            stdout, stderr, exitcode=execCommand("jhosts -l",timeout=60)
            print "jhosts -l:\n%s"%stdout
            stat_list_b=re.findall(r'\s+\bStatus\s*=\s*(.*)\s*\n',stdout)
            print stat_list_a
            print stat_list_b
            host_num_a=0
            host_num_b=0
            host_num_a=len(stat_list_a)
            host_num_b=len(stat_list_b)
            if host_num_a != host_num_a or host_num_a==0 or host_num_b == 0:
                time.sleep(1)
                spendTime -= int(1)
            else: 
                i=0
                while i<host_num_a:
                    if stat_list_a[i].upper() == str(hoststatus).upper() and stat_list_b[i].upper()==str(hoststatus).upper():
                        i=i+1
                        if i==host_num_a:
                            try:
                                time.sleep(2)
                            except KeyboardInterrupt:
                                print ''
                                raise RuntimeError
                            print "the cluster status is ok"
                            return "cluster_ok"
                    else:
                        try:
                            time.sleep(1)
                        except KeyboardInterrupt:
                            print ''
                            raise RuntimeError
                        spendTime -= int(1)
                        break
            if spendTime == int(0):
                print "check cluster status fail"
                raise RuntimeError
    except KeyboardInterrupt:
        print ''
        raise RuntimeError       

def checkHistContain(cmd,num,checkTime=60):
    '''
    check host status in the special time.
    E.g:hostName = 'win7' status = 'closed' checkTime = 10
    '''
    checktime = int(checkTime)
    num = int(num)
    cmd = cmd.replace("\n","")
    try:
        while True:
            print checktime
            stdout, stderr, exitcode=execCommand(cmd,timeout=60)
            print stdout, stderr, exitcode
            if stdout.find("Pending: Requeue the job for the next run") != -1:
                num1=stdout.count("Pending: Requeue the job for the next run")
                print num1
                if num1 != num:
                    time.sleep(1)
                    checktime -= int(1)
                else:
                    print num1
                    print stdout
                    return stdout
            else:
                time.sleep(1)
                checktime -= int(1)
            if checktime == int(0):
                print "check string of 'Pending: Requeue the job for the next run' failed"
                raise RuntimeError
    except KeyboardInterrupt:
        print ''
        raise RuntimeError


def checkRestartClusterStatus(checkTime=60):
    '''
    check cluster all of hosts status is ok in the special time.
    '''
    spendTime = int(checkTime)
    try:
        while True:
            print spendTime
            stdout, stderr, exitcode=execCommand("jhosts stat -l",timeout=60)
            print "jhosts stat -l:\n%s"%stdout
            stat_list_a=re.findall(r'\s+\bStatus\s*=\s*(.*)\s*\n',stdout)
            stdout, stderr, exitcode=execCommand("jhosts -l",timeout=60)
            print "jhosts -l:\n%s"%stdout
            stat_list_b=re.findall(r'\s+\bStatus\s*=\s*(.*)\s*\n',stdout)
            print stat_list_a
            print stat_list_b
            host_num_a=0
            host_num_b=0
            host_num_a=len(stat_list_a)
            host_num_b=len(stat_list_b)
            if host_num_a != host_num_a or host_num_a==0 or host_num_b == 0:
                time.sleep(1)
                spendTime -= int(1)
            else: 
                i=0
                while i<host_num_a:
                    if (stat_list_a[i].upper() == "OK" or stat_list_a[i].upper()=="CLOSED_FULL") and (stat_list_a[i].upper() == "OK" or stat_list_a[i].upper()=="CLOSED_FULL"): 
                        i=i+1
                        if i==host_num_a:
                            time.sleep(2)
                            print "the cluster status is ok"
                            return "the cluster status is ok"
                    else:
                        time.sleep(1)
                        spendTime -= int(1)
                        break
            if spendTime == int(0):
                print "check cluster status fail"
                raise RuntimeError
    except KeyboardInterrupt:
        print ''
        raise RuntimeError       
