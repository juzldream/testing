#!/usr/bin/python
#Filename:paramsConfLib.py


from common import *


def get_host_dict(sectionName):
    dict1={}
    options=[]
    items=[]
    path=get_path("JHSCHEDULER_ENV","params.conf")
    host_config=Config(path)
    sections=host_config.get_section()
    if sectionName in sections:
        items = host_config.get_items(sectionName)
    if len(items)>0:
        for list_tmp in items:
            dict1[list_tmp[0]] = list_tmp[1]
    else:
        print "the %s is error" % path
    return path,host_config, dict1

def addOrModifyParam(paramsName,value):
    '''
    add parameter from params.conf.
    E.g:
    paramsName = 'MBD_SLEEP_TIME' value = '10'
    '''
    paramsName=paramsName.strip()
    path,host_config,dict1=get_host_dict('Parameters')
    if paramsName in dict1.keys():
        host_config.del_options('Parameters',paramsName)
        host_config.add_options('Parameters',paramsName,value)
    else:
        host_config.add_options('Parameters',paramsName,value)
    host_config.write_file(path)

def delParam(paramsName):
    paramsName=paramsName.strip()
    path,host_config,dict1=get_host_dict('Parameters')
    if paramsName in dict1.keys():
        host_config.del_options('Parameters',paramsName)
    host_config.write_file(path)


