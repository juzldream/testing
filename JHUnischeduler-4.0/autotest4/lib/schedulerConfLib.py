#!/bin/env python
#Filename:schedulerConfLib.py


from common import *

def get_host_dict(sectionName):
    dict1={}
    options=[]
    items=[]
    path=get_path("JHSCHEDULER_ENV","scheduler.conf")
    host_config=Config(path)
    sections=host_config.get_section()
    if sectionName in sections:
        items = host_config.get_items(sectionName)
    if len(items)>0:
        #print list1
        for list_tmp in items:
            #print list_tmp[0]
            #print list_tmp[1]
            dict1[list_tmp[0]] = list_tmp[1]
        #for k,v in dict1.items():
            #print "key=%s,value=%s"%(k,v)
    else:
        print "the %s is error" % path
    return path,host_config, dict1

def addOrModifySchedParam(paramsName,value):
    '''
    add parameter from params.conf.
    E.g:
    paramsName = 'MBD_SLEEP_TIME' value = '10'
    '''
    paramsName=paramsName.strip()
    path,host_config,dict1=get_host_dict('Scheduler')
    if paramsName in dict1.keys():
        host_config.del_options('Scheduler',paramsName)
        host_config.add_options('Scheduler',paramsName,value)
    else:
        host_config.add_options('Scheduler',paramsName,value)
    host_config.write_file(path)

def delSchedParam(paramsName):
    paramsName=paramsName.strip()
    path,host_config,dict1=get_host_dict('Scheduler')
    if paramsName in dict1.keys():
        host_config.del_options('Scheduler',paramsName)
    host_config.write_file(path)

