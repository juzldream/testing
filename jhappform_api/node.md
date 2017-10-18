## JHAppform REST api 接口使用说明：

###  作业管理

1. 登录 login api

	- URL ：http://192.168.0.157:8080/appform/ws/login?username=jhadmin&password=jhadmin
	- 成功返回值：

	```
	{
	    "result": "success",
	    "message": null,
	    "data": [
		{
		    "token": ""
		}
	    ]
	}
	```
	- 失败返回值：
	```
	{
	    "result": "failed",
	    "message": "002：许可证校验失败。详细信息：已超过许可证中并发用户数限制",
	    "data": null
	}
	```
2. 注销 logout api

	- URL:http://192.168.0.157:8080/appform/ws/logout?token=
	- 成功返回值：
	```
	{
	    "result": "success",
	    "message": "logout success.",
	    "data": null
	}
	```	
	- 失败返回值：
	```
	{
	    "result": "failed",
	    "message": "005：安全令牌必须输入。",
	    "data": null
	}
	```
3. 连接检查 ping api

	- URL:http://192.168.0.157:8080/appform/ws/ping?token=
	- 成功返回值：
	```
	{
	    "result": "success",
	    "message": "success",
	    "data": null
	}
	```
	- 失败返回值：
	```
	{
	    "result": "failed",
	    "message": "005：用户验证失败。",
	    "data": null
	}
	```
### 文件管理

1. 文件重命名 renamefile api

	- URL:http://192.168.0.157:8080/appform/ws/ping?token=
	- 成功返回值：
	```
	{
	    "result": "success",
	    "message": "success",
	    "data": null
	}
	```	
	- 失败返回值：
	```
	{
	    "result": "failed",
	    "message": "005：用户验证失败。",
	    "data": null
	}
	```
2. 删除文件 deletefile api

	- URL:http://192.168.0.157:8080/appform/ws/delete?token=
	- 成功返回值：
	```
	{
	    "result": "success",
	    "message": "success",
	    "data": null
	}
	```	
	- 失败返回值：
	```
	{
	    "result": "failed",
	    "message": "005：用户验证失败。",
	    "data": null
	}
	```

### 数据管理

1. 根据当前用户 scope 查询数据目录列表 spooles api

	- URL:http://192.168.0.157:8080/appform/ws/spoolers?token=
	- 成功返回值：
	```
	{
	    "result": "success",
	    "message": null,
	    "data": [
	        {
	            "createTime": "2017-09-18 17:38:51",
	            "jobProject": "workf",
	            "dataPath": "/apps/jhappform/spoolers//jhadmin/tmp_20170918173851",
	            "jobId": "844",
	            "jobUser": "jhadmin",
	            "jobName": "job3",
	            "deleteTime": "2017-12-18 01:00:00",
	            "dataName": "tmp_20170918173851"
	        },
	        {
	            "createTime": "2017-09-30 17:17:48",
	            "jobProject": "default",
	            "dataPath": "/apps/jhappform/spoolers//jhadmin/tmp_20170930171748",
	            "jobId": "1920",
	            "jobUser": "jhadmin",
	            "jobName": "hist",
	            "deleteTime": "2018-01-11 01:00:00",
	            "dataName": "tmp_20170930171748"
	        }
	    ]
	}
	```	
	- 失败返回值：

	```
	{
	    "result": "failed",
	    "message": "005：用户验证失败。",
	    "data": null
	}
	```


### 桌面管理

1. 根据当前用户 scope 查询桌面列表 desktops api

	- URL:http://192.168.0.157:8080/appform/ws/desktops?token=

	- 成功返回值：
		```
		{
		    "result": "success",
		    "message": null,
		    "data": [
		        {
		            "os": "linux",
		            "protocol": "vnc",
		            "host": "testplus",
		            "status": "running",
		            "content": "[Connection] host=192.168.158.120 port=5901 password=b1203d6326dbec91 [Options] Shared=True ColorLevel=3 FullColor=True FullScreen=True UseAllMonitors=True EnableToolbar=True autoreconnect=false ",
		            "id": "17119141719934",
		            "shareMe": "false",
		            "ownername": "jhadmin(jhadmin)",
		            "name": "gedit桌面",
		            "owner": "jhadmin",
		            "app_id": "gedit",
		            "createDate": "2017-09-29 14:49:11",
		            "isShare": "false"
		        }
		    ]
		}
		```
	- 失败返回值：
		```
		{
		    "result": "failed",
		    "message": "005：用户验证失败。",
		    "data": null
		}
		```
2. 申请桌面 desktopStart api

	- URL:http://192.168.0.157:8080/appform/ws/desktopStart?os=linux&appid=gedit&resource=linux&protocol=vnc&token=
		- 成功返回值：
		```
		{
		    "result": "success",
		    "message": null,
		    "data": [
		        {
		            "content": "[Connection] host=192.168.158.120 port=5901 password=a5a94983494672fa [Options] Shared=True ColorLevel=3 FullColor=True FullScreen=True UseAllMonitors=True EnableToolbar=True autoreconnect=false "
		        }
		    ]
		}
		```	
		- 失败返回值：
		```
		{
		    "result": "failed",
		    "message": "005：用户验证失败。",
		    "data": null
		}
		```

