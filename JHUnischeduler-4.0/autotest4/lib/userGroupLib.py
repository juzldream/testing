#!/bin/env python
##Filename:userGroupLib.py


from common import get_command_param,get_value

class userGroupLib:
    '''
    all the methods function as follows:
    1)set the output of command 'jugroup'.
    2)get usergroup attribute value such as UsrGrpMem/UsrGrpName and so on.
    '''
    def __init__(self):
        self.uGroup = {}
        self.uGroupMem=[]
        self.uGroupAdmin=[]

    def setGrUserBasicInfo(self,user_group_info):
        self.uGroup=get_command_param(user_group_info,"jusergroup")
        self.uGroupMem=get_value("Users",self.uGroup).split()
        self.uGroupAdmin=get_value("Group Admin",self.uGroup).split()

