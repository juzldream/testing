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

4. 文件重命名 renamefile api

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
