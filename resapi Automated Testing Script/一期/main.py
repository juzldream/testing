#!/usr/bin/python
# -*- coding: UTF-8 -*-
#Date:10-05-2017
#Version=.1


import tool
import jobapi
import fileapi
import desktopapi
import dataapi
import time
import datetime
import os
import sys


default_encoding = 'utf-8'
if sys.getdefaultencoding() != default_encoding:
    reload(sys)
    sys.setdefaultencoding(default_encoding)



if __name__ == '__main__':

    begin = datetime.datetime.now()

    #定义URL地址，用户名，密码，时间戳，token ,unischeduler,jhappfrom,expect
    apivar = {'apiurl':'http://192.168.0.142:8080/appform/ws/',\
    'jhscheduler_top':'/apps/unischeduler/','appform_top':'/apps/jhappform/',\
    'times':str(int(time.time())),'access_token':' ','expect':''}


    #定义连接数据库参数。
    ###
    apivar['dbname'] = "trunk"        #修改为你的appform所使用的数据库名
    apivar['host'] = "192.168.149.120"    #修改为你的appform所使用的数据库ip地址
    apivar['user'] = "racher"             #修改为你的appform所使用的数据库用户名
    apivar['passwd'] = "123.com"          #修改为你的appform所使用的数据库密码
    apivar['port'] = "5432"               #修改为你的appform所使用的数据库端口号
    ####
    
    #完美的分割线。 
    btfi = "-------------------------------------------------------------------------------------------------------------------------------"

    #<一> 登录 appform ，成功返回 access_token值 。
    print btfi
    putlog = tool.putlog
    log = "start test login resapi...\n"    
    putlog.info(log) 

    #登录appform，给定错误的用户，进行登录测试。
    apivar['username'] = "jhinno"
    apivar['password'] = "Jhadmin123"
    apivar['expect'] = "false"
    putlog.info("case 1-1 test start ...\n")
    jobapi.login(apivar)
    putlog.info("case 1-1 test end ...\n")

    #登录appform，给定错误的密码，进行登录测试。
    apivar['username'] = "jhadmin"
    apivar['password'] = "8080"
    apivar['expect'] = "false"
    putlog.info("case 1-2 test start ...\n")
    jobapi.login(apivar)
    putlog.info("case 1-2 test end ...\n")

    #登录appform，给定正确的用户名及密码进行登录测试。
    # apivar['username'] = "jhadmin"  #修改为你的appform管理员
    # apivar['password'] = "jhadmin"  #修改为你的appform管理员密码
    # appform trunk login ...
    apivar['username'] = "GKKb%2boPTGWGyqWBbijvjCQ%3d%3d"  #修改为你的appform管理员
    apivar['password'] = "GKKb%2boPTGWGyqWBbijvjCQ%3d%3d"  #修改为你的appform管理员密码
    apivar['expect'] = "true"
    putlog.info("case 1-3 test start ...\n")
    access_token = jobapi.login(apivar)
    putlog.info("case 1-3 test end ...\n")


    #<二> ping 检查资源是否可用。
    print btfi
    log = "start test ping resapi...\n"
    putlog.info(log)
    
    #给定错误的access_token进行ping检查测试。
    apivar['access_token'] = "access_token"
    apivar['expect'] = "false"
    putlog.info("case 2-1 test start ...\n")
    p = jobapi.checkping(apivar)
    putlog.info("case 2-1 test end ...\n")

    #给定正确的access_token进行ping检查测试。
    apivar['access_token'] = access_token
    apivar['expect'] = "true"
    putlog.info("case 2-2 test start ...\n")
    p = jobapi.checkping(apivar)
    putlog.info("case 2-2 test end ...\n")

    
    # """
    #  <作业操作部分>    
    # """
    # putlog.info("************************************************************")
    # putlog.info("**********************作业操作部分**************************")
    # putlog.info("************************************************************")
    # #<三>提交 fluent 作业 ，传入 casfile ,release=[6.3.26|14.5.0],gui=[ture|false],ncpu=[2|8|12|16]  .
    # print btfi
    # # add casfile ,release=[6.3.26|14.5.0],gui=[ture|false],ncpu=[2|8|12|16]
    # apivar['casfile'] = "/apps/RACHER/jhadmin/fluent-test.cas"
    # apivar['relese'] = "14.5.0"
    # apivar['gui'] = "false"
    # apivar['ncpu'] = "2"

    # log = "start test submit fluent job ...\n"
    # putlog.info(log)

    # #给定正确的参数，进行fluent作业提交测试。
    # apivar['expect'] = "true"
    # putlog.info("case 3-1 test start ...\n")
    # jobid = jobapi.submitfluentjob(apivar)
    # putlog.info("case 3-1 test end ...\n")

    # #给定错误的cas文件，进行fluent作业提交测试。
    # apivar['casfile'] = "/apps/RACHER/jhadmin/pp"
    # apivar['expect'] = "false"
    # putlog.info("case 3-2 test start ...\n")
    # jobapi.submitfluentjob(apivar)
    # putlog.info("case 3-2 test end ...\n") 
 
    # # 提交带图形的fluent作业。
    # apivar['casfile'] = "/apps/RACHER/jhadmin/fluent-test.cas"
    # apivar['gui'] = "true"
    # putlog.info("case 3-3 test start ...\n")
    # jobapi.submitfluentjob(apivar)
    # putlog.info("case 3-3 test end ...\n")


    # #<四> 依据scope查询作业。
    # print btfi
    # log = "start test scope query job...\n"
    # putlog.info(log)
    # putlog.info("case 4-1 test start ...\n")
    # jobapi.jobscope(apivar)
    # putlog.info("case 4-1 test end ...\n") 


    # #<五> 依据作业ID查询作业信息 。
    # # add access_token variable.
    # print btfi
    # log = "start test according to the job id of job information resapi...\n"
    # putlog.info(log)

    # #给定不存在的作业id查询作业信息测试。
    # apivar['jobs'] = ('99999','')
    # apivar['expect'] = "false"
    # putlog.info("case 5-1 test start ...\n") 
    # jf = jobapi.searchIdjob(apivar)
    # putlog.info("case 5-1 test end ...\n")
    
    # #给定正确的作业id查询作业信息测试。
    # apivar['jobs'] = (tool.onlysubjob(apivar)[0],'1000')
    # #apivar['jobs'] = (jobid,'1000')
    # apivar['expect'] = "true"
    # putlog.info("case 5-2 test start ...\n")
    # fluentjob = jobapi.searchIdjob(apivar)
    # putlog.info("case 5-2 test end ...\n")


    # #<六> 依据作业id列表查询作业信息 
    # print btfi
    # log = "start test jobsbyid resapi...\n" 
    # putlog.info(log)

    # #给定正确的id号检查id列表测试。
    # apivar['jobs'] = tool.subconsolejob(apivar)
    # apivar['expect'] = "true"
    # putlog.info("case 6-1 test start ...\n")
    # jobapi.searchIdlistjob(apivar)
    # putlog.info("case 6-1 test end ...\n")

    # #给定错误的id号检查id列表测试。
    # apivar['expect'] = "false"
    # putlog.info("case 6-2 test start ...\n")
    # apivar['jobs'] = ('0','999999')
    # jobapi.searchIdlistjob(apivar)
    # putlog.info("case 6-2 test end ...\n")

    # #<七> 依据作业状态查询有哪些作业。
    # print btfi
    # log = "start test according to the job id of job number resapi...\n"
    # putlog.info(log)

    # #查询done状态的作业有哪些。
    # apivar['status'] = "DONE"
    # apivar['expect'] = "true"
    # putlog.info("case 7-1 test start ...\n") 
    # jobapi.searchstatejob(apivar)
    # putlog.info("case 7-1 test end ...\n") 

    # #查询run状态的作业有哪些。
    # apivar['status'] = "RUN"
    # putlog.info("case 7-2 test start ...\n") 
    # jobapi.searchstatejob(apivar)
    # putlog.info("case 7-2 test end ...\n") 

    # #查询pend状态的作业有哪些。
    # apivar['status'] = "PEND"
    # putlog.info("case 7-3 test start ...\n") 
    # jobapi.searchstatejob(apivar)
    # putlog.info("case 7-3 test end ...\n") 

    # #查询ususp状态的作业有哪些。
    # apivar['status'] = "USUSP"
    # putlog.info("case 7-4 test start ...\n") 
    # jobapi.searchstatejob(apivar)
    # putlog.info("case 7-4 test end ...\n") 

    # #查询psusp状态的作业有哪些。
    # apivar['status'] = "PSUSP"
    # putlog.info("case 7-5 test start ...\n")
    # jobapi.searchstatejob(apivar)
    # putlog.info("case 7-5 test end ...\n")

    # #查询exit状态的作业有哪些。
    # apivar['status'] = "EXIT"
    # putlog.info("case 7-6 test start ...\n")
    # jobapi.searchstatejob(apivar)
    # putlog.info("case 7-6 test end ...\n")

    # #查询NEW状态的作业有哪些。
    # apivar['status'] = "NEW"
    # putlog.info("case 7-7 test start ...\n")
    # jobapi.searchstatejob(apivar)
    # putlog.info("case 7-7 test end ...\n")


    # #<八> stop 作业。
    # print btfi
    # log = "start test stop job resapi...\n"
    # putlog.info(log)
    # apivar['jobs'] = tool.subconsolejob(apivar)
    # jobapi.stopjob(apivar)


    # #<九> resume 作业。
    # print btfi
    # log = "start test resume job resapi...\n"
    # putlog.info(log)
    # apivar['jobs'] = tool.subconsolejob(apivar)
    # jobapi.resumejob(apivar)


    # #<十> kill 作业。
    # print btfi
    # log = "start test kill job resapi...\n"
    # putlog.info(log)
    # apivar['jobs'] = tool.subconsolejob(apivar)
    # jobapi.killjob(apivar)


    # #<十一> peek 作业。
    # print btfi
    # log = "start test peek job resapi...\n"
    # putlog.info(log)
    # apivar['jobs'] = tool.subconsolejob(apivar)
    # apivar['expect'] = "true"
    # jobapi.peekjob(apivar)


    # #<十二> top 作业。
    # print btfi
    # log = "start test bot job resapi...\n"
    # putlog.info(log)
    # apivar['jobs'] = tool.subconsolejob(apivar)
    # apivar['expect'] = "true"
    # jobapi.topjob(apivar)
     
    
    # #<十三> bot 作业。
    # print btfi
    # log = "start test bot job resapi...\n"
    # putlog.info(log)
    # apivar['jobs'] = tool.subconsolejob(apivar)
    # apivar['expect'] = "true"
    # jobapi.botjob(apivar)


    # #<十四> 依据作业ids stop 作业。 
    # print btfi
    # log = "start test stop jobs resapi...\n" 
    # putlog.info(log)
    # apivar['number'] = 2
    # apivar['jobs'] = tool.subconsolenumjobs(apivar)
    # jobapi.stopjobs(apivar)


    # #<十五> 依据作业ids kill 作业。 
    # print btfi
    # log = "start test kill jobs resapi...\n" 
    # putlog.info(log)
    # apivar['number'] = 2
    # apivar['jobs'] = tool.subconsolenumjobs(apivar)
    # jobapi.killjobs(apivar)
   

    # #<十六> 依据作业ids resume 作业。 
    # print btfi
    # log = "start test resume jobs resapi...\n" 
    # putlog.info(log)
    # apivar['number'] = 2
    # apivar['jobs'] = tool.subconsolenumjobs(apivar)
    # jobapi.resumejobs(apivar)


    # #<十七> 依据作业名称查询作业信息 
    # print btfi
    # log = "start test jobsbyname resapi...\n" 
    # putlog.info(log)

    # #给定正确的作业名称查询作业
    # apivar['expect'] = "true"
    # putlog.info("case 17-1 test start ...\n")
    # apivar['jobsbyname'] = tool.onlysubjob(apivar)[1] 
    # jobapi.searchnamejob(apivar)
    # putlog.info("case 17-1 test end...\n")

    # #给定错误的作业名称查询作业
    # apivar['expect'] = "false"
    # putlog.info("case 17-2 test start ...\n")
    # apivar['jobsbyname'] = "jobnaems"
    # p = jobapi.searchnamejob(apivar)
    # putlog.info("case 17-2 test end...\n")


    # #<十八> 查询作业历史信息 
    # print btfi
    # log = "start test look at the history of the job resapi...\n" 
    # putlog.info(log)

    # #给定正确的作业号查询作业历史
    # apivar['expect'] = "true"
    # putlog.info("case 18-1 test start ...\n")
    # apivar['jobs'] = (tool.onlysubjob(apivar)[0],'1000')
    # jobapi.searchhistjob(apivar)
    # putlog.info("case 18-1 test end ...\n")

    # #给定错误的作业号查询作业历史
    # apivar['expect'] = "false"
    # putlog.info("case 18-2 test start ...\n")
    # apivar['jobs'] = ('0X','1000')
    # jobapi.searchhistjob(apivar)
    # putlog.info("case 18-2 test end ...\n")


    # #<十九> 查询多个作业历史信息 
    # print btfi
    # log = "start test jobsbyid resapi...\n" 
    # putlog.info(log)

    # #给定正确的ids查询作业历史。
    # apivar['jobs'] = tool.subconsolejob(apivar)
    # apivar['expect'] = "true"
    # putlog.info("case 19-1 test start ...\n")
    # p = jobapi.searchhistjobs(apivar)
    # putlog.info("case 19-1 test end ...\n")

    # #给定错误的ids查询作业历史。
    # apivar['expect'] = "false"
    # putlog.info("case 19-2 test start ...\n")
    # apivar['jobs'] = ('0','1000')
    # jobapi.searchhistjobs(apivar)
    # putlog.info("case 19-2 test end ...\n")


    #<二十> 依据作业id查询作业数据文件。 
    print btfi
    log = "start test flistbyid resapi...\n" 
    putlog.info(log)

    #给定正确的id查询作业数据文件。
    apivar['expect'] = "true"
    apivar['currentime'] = apivar['times']
    apivar['sql'] = "INSERT INTO datainfo VALUES ('plus', 'default', 'jhadmin', '/apps/jhappform/spoolers//jhadmin/plus_" + apivar['currentime'] + "', '" + apivar['currentime'] + "', '2017-06-21 15:08:06', null);"
    apivar['dml'] = "inst"
    #给数据表datainfo插入一条数据。
    tool.operatepsql(apivar)
    #给appform后台创建数据文件。
    tool.addjobfile(apivar)
    apivar['jobs'] = (apivar['currentime'],'1000')
    putlog.info("case 20-1 test start ...\n")
    jobapi.searchflistjob(apivar)
    putlog.info("case 20-1 test end ...\n")

    #给定错误的id查询作业数据文件。
    apivar['expect'] = "false"
    apivar['jobs'] = ("0",'1000')
    putlog.info("case 20-2 test start ...\n")
    jobapi.searchflistjob(apivar)
    putlog.info("case 20-2 test end ...\n")
    

    # """
    #  <文件管理部分>    
    # """
    # putlog.info("************************************************************")
    # putlog.info("**********************文件管理部分**************************")
    # putlog.info("************************************************************")
    # #<一>文件复制
    # print btfi
    # log = "start test copy file resapi...\n"
    # putlog.info(log)

    # #给定存在的文件
    # apivar['expect'] = "true"
    # apivar['file'] = "logs/portal.log"
    # putlog.info("case 1-1 test start ...\n")
    # cp = fileapi.copyfile(apivar)
    # putlog.info("case 1-1 test end..\n")

    # #给定不存在的文件
    # apivar['expect'] = "false"
    # apivar['file'] = "logs/log.txt.88"
    # putlog.info("case 1-2 test start ...\n")
    # fileapi.copyfile(apivar)
    # putlog.info("case 1-2 test end..\n")
    
    
    # #<二>重命名文件。
    # print btfi
    # log = "start test rename the file resapi...\n"
    # putlog.info(log)
    # #给定一个存在的文件。
    # apivar['expect'] = "true"
    # apivar['filename'] = cp 
    # putlog.info("case 2-1 test start ...\n")
    # rn = fileapi.renamefile(apivar)
    # putlog.info("case 2-1 test end..\n")

    # #给定一个不存在的文件。
    # apivar['expect'] = "false"
    # apivar['filename'] = "filexxxt.doc"
    # putlog.info("case 2-2 test start ...\n")
    # fileapi.renamefile(apivar)
    # putlog.info("case 2-2 test end..\n")

    # #<三>删除文件
    # print btfi
    # log = "start test delete file resapi...\n"
    # putlog.info(log)
    # #给定存在的文件
    # apivar['defile'] = rn
    # apivar['expect'] = "true"
    # putlog.info("case 3-1 test start ...\n")
    # fileapi.deletefile(apivar)
    # putlog.info("case 3-1 test end..\n")


    # #给定不存在的文件
    # apivar['defile'] = "/apptestpsp"
    # apivar['expect'] = "false"
    # putlog.info("case 3-2 test start ...\n")
    # fileapi.deletefile(apivar)
    # putlog.info("case 3-2 test end..\n")


    # #<四>指定目录创建文件夹
    # print btfi
    # log = "start test create folder resapi...\n"
    # putlog.info(log)
    
    # #给定一个存在的目录创建文件夹
    # apivar['expect'] = "true"
    # apivar['folder'] = "logs/"
    # apivar['isforce'] = "true"
    # putlog.info("case 4-1 test start ...\n")
    # fileapi.createfolder(apivar)
    # putlog.info("case 4-1 test end...\n")

    # #给定一个不存在的目录创建文件夹
    # apivar['expect'] = "true"
    # apivar['folder'] = "php/rp/"
    # apivar['isforce'] = "true"
    # putlog.info("case 4-2test start ...\n")
    # fileapi.createfolder(apivar)
    # putlog.info("case 4-2 test end...\n")


    # #<五>获取文件列表
    # print btfi
    # log = "start test get file list resapi...\n"
    # putlog.info(log)

    # #给定存在的目录获取文件列表
    # apivar['expect'] = "true"
    # apivar['list'] = "logs"
    # putlog.info("case 5-1 test start ...\n")
    # fileapi.getfilelist(apivar)
    # putlog.info("case 5-1 test end...\n")
    
    # #给定不存在的目录获取文件列表
    # apivar['expect'] = "false"
    # apivar['list'] = "//*"
    # putlog.info("case 5-2 test start ...\n")
    # fileapi.getfilelist(apivar)
    # putlog.info("case 5-2 test end...\n")


    # #<六>返回页面URL([jobmana、desktopmana、spoolermana])
    # print btfi
    # log = "start test get web url resapi...\n"
    # putlog.info(log)

    # #返回作业管理url
    # apivar['appname'] = "jobmana"
    # putlog.info("case 6-1 test start ...\n")
    # fileapi.getweburl(apivar)
    # putlog.info("case 6-1 test end...\n")

    # #返回桌面管理url
    # apivar['appname'] = "desktopmana"
    # putlog.info("case 6-2 test start ...\n")
    # fileapi.getweburl(apivar)
    # putlog.info("case 6-2 test end...\n")

    # #返回数据管理url
    # apivar['appname'] = "spoolermana"
    # putlog.info("case 6-3 test start ...\n")
    # fileapi.getweburl(apivar)
    # putlog.info("case 6-3 test end...\n")

    # #给定不存在应用返回url
    # apivar['appname'] = "jhinno.com"
    # putlog.info("case 6-4 test start ...\n")
    # fileapi.getweburl(apivar)
    # putlog.info("case 6-4 test end...\n")


    # #<七>下载文件
    # print btfi
    # log = "start test download file resapi...\n"
    # putlog.info(log)
    # putlog.info("case 7-1 test start ...\n")
    # apivar['path'] = apivar['appform_top'] + "logs/test"
    # fileapi.filedownload(apivar)
    # putlog.info("case 7-1 test end...\n")

    # putlog.info("case 7-2 test start ...\n")
    # apivar['expect'] = "true"
    # apivar['path'] = apivar['appform_top'] + "logs/jhinno.md"
    # fileapi.filedownload(apivar)
    # putlog.info("case 7-2 test end...\n")

    # putlog.info("case 7-3 test start ...\n")
    # apivar['expect'] = "false"
    # apivar['path'] = apivar['appform_top'] + "conf/appform.conf"
    # fileapi.filedownload(apivar)
    # putlog.info("case 7-3 test end...\n")


    # #<文件上传>
    # #通过fileclient攻击上传文件
    # print btfi
    # log = "start test file upload resapi...\n"
    # putlog.info(log)
    # putlog.info("case 8-1 test start ...\n")
    # apivar['expect'] = "true"
    # apivar['fileclient'] = "/apps/jhappform/bin/"
    # apivar['local'] = "/etc/sysconfig/network-scripts/ifdown-eth"
    # apivar['remote'] = "/apps/jhappform/logs/portal.log"
    # apivar['serverip'] = "192.168.0.142"
    # fileapi.fileuploadtool(apivar)
    # putlog.info("case 8-1 test end...\n")

    # #给定不存在的文件上传
    # putlog.info("case 8-2 test start ...\n")
    # apivar['expect'] = "false"
    # apivar['fileclient'] = "/apps/jhappform/bin/"
    # apivar['local'] = "/etc/sysconfig/network-scripts/ifdown-ethXX"
    # apivar['remote'] = "/apps/jhappform/logs/portal.log"
    # apivar['serverip'] = "192.168.0.142"
    # fileapi.fileuploadtool(apivar)
    # putlog.info("case 8-2 test end...\n")

    # #通过api上传文件
    # print btfi
    # log = "start test file upload resapi...\n"
    # putlog.info(log)
    # putlog.info("case 9-1 test start ...\n")
    # apivar['expect'] = "true"
    # apivar['ServerPath'] = "/apps/jhappform/logs"
    # apivar['file'] = "/apps/jhappform/conf/appform.conf"
    # fileapi.fileupload(apivar)
    # putlog.info("case 9-1 test end...\n")

    # putlog.info("case 9-2 test start ...\n")
    # apivar['expect'] = "false"
    # apivar['ServerPath'] = "/apps/jhappform/logs"
    # apivar['file'] = "/apps/jhappform/conf/autoCAD.cad"
    # fileapi.fileupload(apivar)
    # putlog.info("case 9-2 test end...\n")

    """
     <桌面管理部分>    
    """
    putlog.info("************************************************************")
    putlog.info("**********************桌面管理部分**************************")
    putlog.info("************************************************************")
   
    #
    #
    # #<一>申请桌面[vnc、jhapp]
    # #### 定义申请桌面参数。

    print btfi
    log = "start test apply desktop resapi...\n"
    putlog.info(log)
    apivar['sql'] = "DELETE FROM desktop;"
    apivar['dml'] = "dele"
    apivar['datainfo'] = tool.operatepsql(apivar)
    apivar['sql'] = "SELECT * FROM desktop;"
    apivar['dml'] = "sele"

    # #给定正确的参数申请桌面
    putlog.info("case 1-1 test start ...\n")
    apivar['expect'] = "true"
    apivar['os'] = "linux"
    apivar['appid'] = "gedit"
    apivar['resource'] = "linux"
    apivar['protocol'] = "vnc"
    desktopapi.applydesktop(apivar)
    putlog.info("case 1-1 test end ...\n")
   
    # #给定不存在的应用名申请桌面
    # putlog.info("case 1-2 test start ...\n")
    # apivar['expect'] = "false"
    # apivar['os'] = "linux"
    # apivar['appid'] = "rzhou"
    # apivar['resource'] = "linux"
    # apivar['protocol'] = "vnc"
    # desktopapi.applydesktop(apivar)
    # putlog.info("case 1-2 test end ...\n")


    # #给定不支持的协议名申请桌面
    # putlog.info("case 1-3 test start ...\n")
    # apivar['expect'] = "false"
    # apivar['os'] = "linux"
    # apivar['appid'] = "gedit"
    # apivar['resource'] = "source"
    # apivar['protocol'] = "prott"
    # desktopapi.applydesktop(apivar)
    # putlog.info("case 1-3 test end ...\n")


    # #<二>根据scope查找桌面列表
    # print btfi
    # log = "start test scope desktop resapi...\n"
    # putlog.info(log)
    # putlog.info("case 2-1 test start ...\n")
    # apivar['sql'] = "SELECT * FROM desktop;"
    # apivar['dml'] = "sele"
    # apivar['datainfo'] = tool.operatepsql(apivar)
    # desktopapi.desktopscope(apivar) 
    # putlog.info('---------------------------------------')   
    # putlog.info("case 2-1 test end...\n")


    # #<三>根据桌面id查询桌面列表
    # print btfi
    # log = "start test id desktop resapi...\n"
    # putlog.info(log)
    # #给定正确的桌面id查询
    # putlog.info("case 3-1 test start ...\n")
    # apivar['expect'] = "true"
    # apivar['desktopid'] = apivar['times']
    # apivar['sql'] = "INSERT INTO desktop VALUES ('" + apivar['desktopid'] + \
    # "', 'running', '2017-06-05 11:43:20', '', 'vnc', null, null, null, 'linux', 'gedit桌面', '" + apivar['desktopid'] + \
    #  "', 'jhadmin', null, 'testplus', '1', '46076', null, null, null, 't', 't', null, 'f8d22dfa74e64fef', 'testplus:1.0', " \
    # +"null, '/apps/jhappform/work/sessions/2017-06-05/7200047583687/7200047583687.log', 'gedit', 'vnc');"
    # apivar['dml'] = "inst"
    # apivar['datainfo'] = tool.operatepsql(apivar)
    # p = desktopapi.searchiddesktop(apivar)
    # print p
    # putlog.info("case 3-1 test end ...\n")

    # #给定不存在的桌面id查询
    # putlog.info("case 3-2 test start ...\n")
    # apivar['expect'] = "false"
    # apivar['desktopid'] = "0000"
    # desktopapi.searchiddesktop(apivar)
    # putlog.info("case 3-2 test end...\n")


    # #<四>根据桌面id列表查询桌面列表
    # print btfi
    # log = "start test ids desktop resapi...\n"
    # putlog.info(log)
    # putlog.info("case 4-1 test start ...\n")
    # apivar['expect'] = "true"
    # apivar['desktopid'] = (apivar['times'] +"01",apivar['times'] + "07")
    # apivar['sql'] = "INSERT INTO desktop VALUES ('" + apivar['desktopid'][0] + \
    # "', 'running', '2017-06-05 11:43:20', '', 'vnc', null, null, null, 'linux', 'gedit桌面', '" + apivar['desktopid'][0] + \
    #  "', 'jhadmin', null, 'testplus', '1', '46076', null, null, null, 't', 't', null, 'f8d22dfa74e64fef', 'testplus:1.0', ""null, '/apps/jhappform/work/sessions/2017-06-05/7200047583687/7200047583687.log', 'gedit', 'vnc'),('" + apivar['desktopid'][1] + \
    # "', 'running', '2017-06-05 11:43:20', '', 'vnc', null, null, null, 'linux', 'gedit桌面', '" + apivar['desktopid'][1]+ \
    #  "', 'jhadmin', null, 'testplus', '1', '46076', null, null, null, 't', 't', null, 'f8d22dfa74e64fef', 'testplus:1.0', ""null, '/apps/jhappform/work/sessions/2017-06-05/7200047583687/7200047583687.log', 'gedit', 'vnc');"
    # apivar['dml'] = "inst"
    # apivar['datainfo'] = tool.operatepsql(apivar)
    # desktopapi.searchidlistdesktop(apivar)
    # putlog.info("case 4-1 test end ...\n")

    # # #给定不存在的桌面id
    # putlog.info("case 4-2 test start ...\n")
    # apivar['expect'] = "false"
    # apivar['desktopid'] = ('000','000')
    # desktopapi.searchidlistdesktop(apivar)
    # putlog.info("case 4-2 test end ...\n")


    # #<五>根据桌面名称查询桌面列表
    # print btfi
    # log = "start test desktop name resapi...\n"
    # putlog.info(log)
    # putlog.info("case 5-1 test start ...\n")
    # #给定正确的桌面名称
    # apivar['expect'] = "true"
    # apivar['name'] = "gedit桌面"
    # apivar['sql'] = "SELECT * from desktop WHERE name = '" + apivar['name'] + "';"
    # apivar['dml'] = "sele"
    # apivar['datainfo'] = tool.operatepsql(apivar)
    # desktopapi.searchdesktopname(apivar)
    # putlog.info("case 5-1 test end ...\n")

    # # #给定错误的桌面名称
    # putlog.info("case 5-2 test start ...\n")
    # apivar['expect'] = "false"
    # apivar['name'] = "rzhouXX"
    # desktopapi.searchdesktopname(apivar)
    # putlog.info("case 5-2 test end ...\n")


    # #<六>关闭桌面
    # log = "start test close desktop resapi...\n"
    # putlog.info(log)
    # putlog.info("case 6-1 test start ...\n")
    # # 给定正确的桌面id
    # apivar['expect'] = "true"
    # apivar['desktopid'] = apivar['times'] + "119"
    # apivar['sql'] = "INSERT INTO desktop VALUES ('" + apivar['desktopid'] + \
    # "', 'running', '2022-06-05 11:43:20', '', 'vnc', null, null, null, 'linux', 'gedit桌面', '" + apivar['desktopid'] + \
    #  "', 'jhadmin', null, 'testplus', '1', '46076', null, null, null, 't', 't', null, 'f8d22dfa74e64fef', 'testplus:1.0', " \
    # +"null, '/apps/jhappform/work/sessions/2017-06-05/7200047583687/7200047583687.log', 'gedit', 'vnc');"
    # apivar['dml'] = "inst"
    # apivar['datainfo'] = tool.operatepsql(apivar)
    # apivar['sql'] = "SELECT * from desktop where id = '" +  apivar['desktopid'] + "'"
    # apivar['dml'] = "sele"
    # desktopapi.closedesktop(apivar)
    # putlog.info("case 6-1 test end ...\n")

    # # #给定错误的桌面id
    # putlog.info("case 6-2 test start ...\n")  
    # apivar['expect'] = "false"
    # apivar['desktopid'] = "000"
    # desktopapi.closedesktop(apivar)
    # putlog.info("case 6-2 test end ...\n")


    # # #共享桌面 [collaborato、observer]
    # log = "start test share desktop resapi...\n"
    # putlog.info(log)
    # putlog.info("case 7-1 test start ...\n")
    # #给定正确的桌面id交互共享桌面
    # apivar['expect'] = "true"
    # apivar['desktopid'] = apivar['times'] + "120"
    # apivar['sql'] = "INSERT INTO desktop VALUES ('" + apivar['desktopid'] + \
    # "', 'running', '2022-06-05 11:43:20', '', 'vnc', null, null, null, 'linux', 'gedit桌面', '" + apivar['desktopid'] + \
    #  "', 'jhadmin', null, 'testplus', '1', '46076', null, null, null, 't', 't', null, 'f8d22dfa74e64fef', 'testplus:1.0', " \
    # +"null, '/apps/jhappform/work/sessions/2017-06-05/7200047583687/7200047583687.log', 'gedit', 'vnc');"
    # apivar['dml'] = "inst"
    # apivar['datainfo'] = tool.operatepsql(apivar)
    # apivar['sharedmode'] = "collaborator"
    # apivar['users'] = ('user1','jhadmin')
    # apivar['sql'] = "SELECT * from desktop where id = '" + apivar['desktopid'] + "'"
    # apivar['dml'] = "sele"
    # apivar['datainfo'] = tool.operatepsql(apivar)
    # apivar['sql'] = "SELECT * FROM desktop_user WHERE desktop_id='" + apivar['desktopid'] + "' AND shared_mode='interact';"
    # apivar['dml'] = "sele"
    # desktopapi.sharedesktop(apivar)
    # putlog.info("case 7-1 test end ...\n")

    # #给定不存在的桌面id共享桌面
    # putlog.info("case 7-2 test start ...\n")
    # apivar['expect'] = "false"
    # apivar['desktopid'] = "123456789"
    # apivar['sharedmode'] = "collaborator"
    # apivar['users'] = ('user1','jhadmin')
    # desktopapi.sharedesktop(apivar)
    # putlog.info("case 7-2 test end ...\n")

    # #给定正确的桌面id观察共享桌面
    # putlog.info("case 7-3 test start ...\n")
    # apivar['expect'] = "true"
    # apivar['desktopid'] = apivar['times'] + "122"
    # apivar['sql'] = "INSERT INTO desktop VALUES ('" + apivar['desktopid'] + \
    # "', 'running', '2022-06-05 11:43:20', '', 'vnc', null, null, null, 'linux', 'gedit桌面', '" + apivar['desktopid'] + \
    #  "', 'jhadmin', null, 'testplus', '1', '46076', null, null, null, 't', 't', null, 'f8d22dfa74e64fef', 'testplus:1.0', " \
    # +"null, '/apps/jhappform/work/sessions/2017-06-05/7200047583687/7200047583687.log', 'gedit', 'vnc');"
    # apivar['dml'] = "inst"
    # apivar['datainfo'] = tool.operatepsql(apivar)
    # apivar['sharedmode'] = "observer"
    # apivar['users'] = ('user1','jhadmin')
    # apivar['sql'] = "SELECT * from desktop where id = '" + apivar['desktopid'] + "'"
    # apivar['dml'] = "sele"
    # apivar['datainfo'] = tool.operatepsql(apivar)
    # apivar['sql'] = "SELECT * FROM desktop_user WHERE desktop_id='" + apivar['desktopid'] + "' AND shared_mode='observe';"
    # apivar['dml'] = "sele"
    # desktopapi.sharedesktop(apivar)
    # putlog.info("case 7-3 test end ...\n")

    # #取消桌面共享
    # putlog.info("case 7-4 test start ...\n")
    # apivar['expect'] = "false"
    # apivar['desktopid'] = apivar['times'] + "122"
    # apivar['sharedmode'] = "observer"
    # apivar['users'] = ('pps','bbs')
    # apivar['off'] = "true"
    # desktopapi.sharedesktop(apivar)
    # putlog.info("case 7-4 test end ...\n")

    # #给定错误的桌面id观察共享桌面
    
    # putlog.info("case 7-5 test start ...\n")
    # apivar['expect'] = "false"
    # apivar['desktopid'] = "123456789"
    # apivar['sharedmode'] = "observer"
    # apivar['users'] = ('user1','jhadmin')
    # desktopapi.sharedesktop(apivar)
    # putlog.info("case 7-5 test end ...\n")


    """
    <数据管理部分>
    """
    # putlog.info("************************************************************")
    # putlog.info("**********************数据管理部分**************************")
    # putlog.info("************************************************************")
    # #<一>根据当前用户scope查询数据目录 
  
    # print btfi
    # log = "start test scope data resapi...\n"
    # putlog.info(log)
    # apivar['sql'] = "DELETE FROM datainfo;"
    # apivar['dml'] = "dele"
    # apivar['datainfo'] = tool.operatepsql(apivar)
    # apivar['jobid'] = apivar['times'] + str(5)
    # apivar['dataPath'] = "/apps/jhappform/spoolers//jhadmin/" + apivar['jobid']
    # apivar['sql'] = "INSERT INTO datainfo VALUES ('tom', 'default', 'jhadmin', '" + apivar['dataPath'] + "', " +\
    # apivar['jobid'] + ", '2017-05-31 17:59:55', null);"
    # apivar['dml'] = "inst"
    # apivar['datainfo'] = tool.operatepsql(apivar)
    # putlog.info("case 1-1 test start ...\n")
    # apivar['sql'] = "select * from datainfo;"
    # apivar['dml'] = "sele"
    # apivar['datainfo'] = tool.operatepsql(apivar)
    # dataapi.datascope(apivar)
    # putlog.info("case 1-1 test end ...\n")


    # #<二>根据作业id查询数据目录 
    # print btfi
    # log = "start test id data resapi...\n"
    # putlog.info(log)
    # putlog.info("case 2-1 test start ...\n")
    # # 给定正确的作业id查询数据目录
    # apivar['expect'] = "true"
    # apivar['jobid'] = apivar['times'] + str(4)
    # apivar['dataPath'] = "/apps/jhappform/spoolers//jhadmin/" + apivar['jobid']
    # apivar['sql'] = "INSERT INTO datainfo VALUES ('tom', 'default', 'jhadmin', '" + apivar['dataPath'] + "', " +\
    # apivar['jobid'] + ", '2017-05-31 17:59:55', null);"
    # apivar['dml'] = "inst"
    # apivar['datainfo'] = tool.operatepsql(apivar)
    # dataapi.searchidjobdir(apivar)
    # putlog.info("case 2-1 test end ...\n")

    # # 给定错误的作业id查询数据目录
    # putlog.info("case 2-2 test start ...\n")
    # apivar['expect'] = "false"
    # apivar['jobid'] = "0"
    # dataapi.searchidjobdir(apivar)
    # putlog.info("case 2-2 test end ...\n")


    # #<三>根据数据id列表查询数据目录
    # log = "start test ids data resapi...\n"
    # putlog.info(log)
    # putlog.info("case 3-1 test start ...\n")
    # apivar['expect'] = "true"
    # apivar['jobid'] = (apivar['times'] + str(99),apivar['times'] + str(66))
    # apivar['dataPath'] = ("/apps/jhappform/spoolers//jhadmin/" + apivar['jobid'][0],"/apps/jhappform/spoolers//jhadmin/" + apivar['jobid'][1])
    # apivar['sql'] = "INSERT INTO datainfo VALUES ('tom', 'default', 'jhadmin', '" +  apivar['dataPath'][0] + "', " + \
    # apivar['jobid'][0] + ", '2017-05-31 17:59:55', null),('tom', 'default', 'jhadmin', '" + apivar['dataPath'][0] + "', "\
    # + apivar['jobid'][1] + ", '2017-06-01 17:59:55', null);"
    # apivar['dml'] = "inst"
    # apivar['datainfo'] = tool.operatepsql(apivar)
    # dataapi.searchidsjobdir(apivar)  
    # putlog.info("case 3-1 test end ...\n")

    # putlog.info("case 3-2 test start ...\n")
    # apivar['expect'] = "false"
    # apivar['jobid'] = ("0","0")
    # dataapi.searchidsjobdir(apivar)  
    # putlog.info("case 3-2 test end ...\n")


    # #<四>根据数据目录名称查询数据目录列表
    # log = "start test dir data resapi...\n"
    # putlog.info(log)
    # # 给定正确的数据目录名称
    # putlog.info("case 4-1 test start ...\n")
    # apivar['expect'] = "true"
    # apivar['jobid'] = apivar['times'] + str(3)
    # apivar['dataPath'] = "/apps/jhappform/spoolers//jhadmin/" + apivar['jobid']
    # apivar['sql'] = "INSERT INTO datainfo VALUES ('tom', 'default', 'jhadmin', '" + apivar['dataPath'] + "', " + apivar['jobid'] + \
    # ", '2017-05-31 17:59:55', null);"
    # apivar['dml'] = "inst"
    # apivar['datainfo'] = tool.operatepsql(apivar)
    # dataapi.spoolersbyname(apivar)
    # putlog.info("case 4-1 test end ...\n")

    # # 给定正确的数据目录名称
    # putlog.info("case 4-2 test start ...\n")
    # apivar['expect'] = "false"
    # apivar['dataPath'] = "/apps/jhappform/spoolers//jhadmin/jhinnoTXT"
    # dataapi.spoolersbyname(apivar)
    # putlog.info("case 4-2 test end ...\n")

    #<五>立即删除数据目录
    log = "start test del data dir resapi...\n"
    putlog.info(log)
    # 给定正确的数据目录名称
    putlog.info("case 5-1 test start ...\n")
    apivar['expect'] = "true"
    apivar['jobid'] = apivar['times'] + str(2)
    apivar['dataPath'] = "/apps/jhappform/spoolers//jhadmin/" + apivar['jobid']
    apivar['sql'] = "INSERT INTO datainfo VALUES ('tom', 'default', 'jhadmin', '" + apivar['dataPath'] + "', " + apivar['jobid'] + \
    ", '2017-05-31 17:59:55', null);"
    apivar['dml'] = "inst"
    apivar['datainfo'] = tool.operatepsql(apivar)
    apivar['sql'] = "SELECT * from datainfo WHERE job_id = '559';"
    apivar['dml'] = "sele"
    dataapi.imdeldir(apivar)
    putlog.info("case 5-1 test end ...\n")
    
    #给定不存在的数据目录
    putlog.info("case 5-2 test start ...\n")
    apivar['expect'] = "false"
    apivar['jobid'] = "0"
    dataapi.imdeldir(apivar)
    putlog.info("case 5-2 test end ...\n")


    #<六>过期删除数据目录
    log = "start test expire del data dir resapi...\n"
    putlog.info(log)
    putlog.info("case 6-1 test start ...\n")
    apivar['expect'] = "true"
    apivar['jobid'] = apivar['times']
    #定义一天后删除时间
    onedayafter = (datetime.datetime.now() + datetime.timedelta(days = 1))
    otherStyleTime = onedayafter.strftime("%Y-%m-%d")
    apivar['expiration_time'] = otherStyleTime

    apivar['dataPath'] = "/apps/jhappform/spoolers//jhadmin/" + apivar['times']
    apivar['sql'] = "INSERT INTO datainfo VALUES ('tom', 'default', 'jhadmin', '" + apivar['dataPath'] + "', " + apivar['jobid'] + \
    ", '2017-05-31 17:59:55', null);"
    apivar['dml'] = "inst"
    apivar['datainfo'] = tool.operatepsql(apivar)
    apivar['sql'] = "SELECT * from datainfo WHERE delete_time = '" + apivar['expiration_time'] + " 01:00:00';"
    apivar['dml'] = "sele"
    dataapi.expiredeldir(apivar)
    putlog.info("case 6-1 test end ...\n")

    #设置3天前删除数据目录
    putlog.info("case 6-2 test start ...\n")
    apivar['expect'] = "false"
    apivar['jobid'] = apivar['times'] + str(1)
    threedayaago = (datetime.datetime.now() - datetime.timedelta(days = 3))
    otherStyleTime = threedayaago.strftime("%Y-%m-%d")
    apivar['expiration_time'] = otherStyleTime
    apivar['dataPath'] = "/apps/jhappform/spoolers//jhadmin/" + apivar['times']
    apivar['sql'] = "INSERT INTO datainfo VALUES ('tom', 'default', 'jhadmin', '" + apivar['dataPath'] + "', " + apivar['jobid'] + \
    ", '2017-05-31 17:59:55', null);"
    apivar['dml'] = "inst"
    apivar['datainfo'] = tool.operatepsql(apivar)
    dataapi.expiredeldir(apivar)    
    putlog.info("case 6-2 test end ...\n")


    #<二一> 注销 appform .
    print btfi
    log = "start test logout resapi...\n" 
    putlog.info(log)

    #给定一个错误的access_token值，进行appform注销测试。 
    apivar['expect']  = "false"
    apivar['access_token'] = "access_token"
    putlog.info("case 21-1 test start ...\n")
    lo = jobapi.logout(apivar)
    putlog.info("case 21-1 test end ...\n")

    #给定一个正确的access_token值，进行appform注销测试。
    apivar['expect'] = "true"
    apivar['access_token'] = access_token
    putlog.info("case 21-2 test start ...\n")
    lo = jobapi.logout(apivar)
    putlog.info("case 21-2 test end ...\n")
    print btfi


    end = datetime.datetime.now()
    print end - begin
