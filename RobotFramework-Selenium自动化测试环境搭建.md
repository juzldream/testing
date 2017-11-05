## Robot Framework 环境配置
### windows 10 系统

1. Python 安装  2.7
2. wxPython 安装 (wxPython2.8-win32-unicode-2.8.12.1-py27.exe)
3. robotframework 安装
	- `pip install robotframework  3.0 ok`

4. robotframework-ride

	- `pip install robotframework-ride`


5. 启动 ride 编辑器

	- 双击 `E:\tools\Python\Python27\Scripts\ride.Py` 文件
	- `Win + R -> cmd -> python -> from robotide import main - > main()`
	- `Win + R -> cmd -> ride.py`
	- 支持bat文件，bat 文件内容：python -c "from robotide import main;main()"
	- 将ride.py创建快捷方式到桌面  


6. selenium2library安装
	- `pip install robotframework-selenium2library`


7. 浏览器准备，
   - Google Chrome 版本 62.0.3202.62（正式版本） （64 位），

   - webdriver地址：`http://chromedriver.storage.googleapis.com/index.html?path=2.33/chromedriver_win32.zip`
     解压放到 ：`C:\Windows\System32 `目录下


### CentOS 7 系统

1. 修改主机名
	- `hostnamectl set-hostname testplan`

2. 安装pip
	- `yum -y install epel-release`
	- `yum install python-pip`
	- `pip install --upgrade pip`

3. 安装ipython
	- `yum install gcc libffi-devel python-devel openssl-devel`
	- `pip install ipython`

4. 安装selenium

	- `pip install selenium`

5. 安装RobotFramework

	- `yum install wxPython`
	- `pip install robotframework `
	- `pip install robotframework-ride`
	- `pip install robotframework-selenium2library`

6. 安装PhantomJS

	[phantomjs下载地址](http://npm.taobao.org/dist/phantomjs/)
	- `tar -zxvf phantomjs-2.1.1-linux-x86_64.tar.bz2`
	- `export PHANTOMJS_HOME = /PATH/phantomjs-2.1.1/bin`

7. 测试脚本

	```
	In [1]: from selenium import webdriver

	In [2]: driver = webdriver.PhantomJS()

	In [4]: driver.get('http://www.baidu.com')

	In [5]: print driver.title
	百度一下，你就知道

	In [6]: driver.find_element_by_css_selector('#kw').send_keys('selenium')

	In [7]: driver.get_screenshot_as_file('/apps/baidu_index.png')
	Out[7]: True

	In [9]: driver.find_element_by_css_selector('#su').click()

	In [10]: print driver.title
	selenium_百度搜索

	In [11]: driver.get_screenshot_as_file('/apps/search_selenium.png')
	    ...: 
	Out[11]: True

	In [12]: driver.close()

	```
![robotfarmwork](https://mmbiz.qpic.cn/mmbiz_png/4iaE7bB4HCjfodlu3uJM0zvNwiaLlWDicIEm99d7cgAHlo2ItjDzh5aAB8caMFd3X24ISHOVojCOO2tImYLIR4Hdw/0?wx_fmt=png)
