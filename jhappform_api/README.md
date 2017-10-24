## appform_restapi 接口自动化测试使用说明：

###  项目结构
`
	jhappform_api/
	├── main.py
	├── node.md
	├── report
	│   └── result_2017-10-24_14-01-25.html
	├── test_case
	│   ├── test_actionjob.py
	│   ├── test_actionjobs.py
	│   ├── test-applist.py
	│   ├── test_copyfile.py
	│   ├── test_deletefile.py
	│   ├── test_delspooler.py
	│   ├── test_desktopclose.py
	│   ├── test_desktopid.py
	│   ├── test_desktopids.py
	│   ├── test_desktopname.py
	│   ├── test_desktops.py
	│   ├── test_desktopstart.py
	│   ├── test_expirdelspooler.py
	│   ├── test_filelist.py
	│   ├── test_jobfileliet.py
	│   ├── test_jobid.py
	│   ├── test_jobids.py
	│   ├── test_jobname.py
	│   ├── test_jobs.py
	│   ├── test_jobstatus.py
	│   ├── test_jsub.py
	│   ├── test_login.py
	│   ├── test-mkdir.py
	│   ├── test_ping.py
	│   ├── test_renamefile.py
	│   ├── test_sharedesktop.py
	│   ├── test_spoolerid.py
	│   ├── test_spoolerids.py
	│   ├── test_spoolername.py
	│   ├── test_spoolers.py
	│   ├── test_url.py
	│   └── test_zlogout.py
	├── test_data
	│   └── data.json
	├── test.py
	└── tools
	    ├── HTMLTestReportCN.py
	    └── tools.py

	4 directories, 39 files

`

###  执行测试

1. 测试前需要搭建的appform环境并成功启动，修改data.json 文件  "baseUrl": "http://192.168.0.133:8080/appform/ws/", baseUrl值自己的环境ip地址；email_receiver值填写自己的邮箱地址，最终的测试结果会以html附件形式发送到邮箱里。

2. 可以在data.json文件增加新的测试数据。如，登录api在login 下增加：
`
	{
	    "name": "example",
	    "expect": "0",
	    "username": "a",
	    "password": "b"
	}
`
注 ：name 值不可重复，如果重复默认执行最后一个；expect 值是给定的值是否为正确值。

3. 执行步骤，只需在 http://192.168.0.43:8888/view/OnDemand/ ，构建一次 appform-restapi，只需在邮箱检查附件结果。