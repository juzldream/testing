#!/bin/env python
#Filename:userLib.py


import re
from common import get_command_param,get_value


class userLib:

    '''
    all the methods function as follows:
    1)set the output of command 'jusers username'.
    2)get user attribute value such as UsrMax/UsrRun and so on.
    '''
    def __init__(self):
        self.UsrName = ""
        self.UsrMax = ""
        self.UsrNjobs = ""
        self.UsrPend = ""
        self.UsrRun = ""
        self.UsrSsusp = ""
        self.UsrUsusp = ""
        self.UsrRsv = ""
        self.UsrJLP = ""
    def setUsrBasicInfo(self,user_info):
        #para 'user_info' is the output of "jusers username"
        UsrName=re.findall(r'\bUser/Group:\s*(.+)\s*\n',user_info)
        if UsrName:
            self.UsrName=UsrName[0]
        user_parm_dict=get_command_param(user_info,"jusers")

        self.UsrMax = get_value("Max",user_parm_dict)
        self.UsrNjobs = get_value("JobsNum",user_parm_dict)
        self.UsrPend = get_value("Pend",user_parm_dict)
        self.UsrRun = get_value("Run",user_parm_dict)
        self.UsrSsusp = get_value("SSUSP",user_parm_dict)
        self.UsrUsusp = get_value("USUSP",user_parm_dict)
        self.UsrRsv = get_value("Rsv",user_parm_dict)
        self.UsrJLP = get_value("JL/P",user_parm_dict)


