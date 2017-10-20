#!/bin/sh
#FileName:getMsgLib.py

class msgLib:

    def __init__(self):
        self.jobId=""
        self.msgIndex=""
        self.putTime=""
        self.userName=""
        self.Desc=""

    def setBasicInfo(self,string):
        if string:
            info_list=string.strip().split("\n")
            title_list_tmp=info_list[0].strip().split('  ')
            msg_list_tmp=info_list[1].strip().split('  ')
            msg_dict=dict()
            title_list=[]
            msg_list=[]
            for i in title_list_tmp:
                 if len(i) != int(0):
                     title_list.append(i.strip())
            for i in msg_list_tmp:
                 if len(i) != int(0):
                     msg_list.append(i.strip())
            for j in range(0,len(title_list)):
                msg_dict[title_list[j]]=msg_list[j]
            self.jobId=msg_dict['JOB_ID']
            self.msgIndex=msg_dict['MSG_INDEX']
            self.putTime=msg_dict['PUT_TIME']
            self.userName=msg_dict['USER_NAME']
            self.Desc=msg_dict['DESCRIPTION']

        
