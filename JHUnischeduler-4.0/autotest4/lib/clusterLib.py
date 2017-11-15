#!/bin/env python
#Filename:clusterLib.py


import re

class clusterLib:
    '''
    all the methods function as follows:
    1)set the output of command 'jversion' and 'jcluster'.
    2)get cluster attribute value such as MasterName/ClusterName and so on.
    '''
    def __init__(self):
        self.MasterName = ''
        self.ClusterName = ''
        self.Version = ''
    def setClusterInfo(self,result):
        try:
            self.Version = re.findall(r'\s*(\bJH UniScheduler 4.0,.*)\n',result)[0]
            self.MasterName = re.findall(r'\s*\bMy master name is (.+)',result)[0]
            self.ClusterName = re.findall(r'\s*\bMy cluster name is (.+)',result)[0]
        except IndexError:
            print 'some cluster info not find!'
    def getMstrName(self):
        return self.MasterName
    def getClstrName(self):
        return self.ClusterName
    def getVrsion(self):
        return self.Version

