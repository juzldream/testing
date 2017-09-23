1. taiga 用户使用的是192.168.0.31 Samba AD 域服务器域账号

2. 域配置信息如下：
```
CN=jhadmin,CN=Users,DC=xadev,DC=com
administrator JHadmin999

Server Role:           active directory domain controller
Hostname:              jhserver
NetBIOS Domain:        XADEV
DNS Domain:            xadev.com
DOMAIN SID:            S-1-5-21-2931584764-424765662-1872811250

~     
```
3. taiga添加账号，在192.168.0.31服务器执行以下命令即可（taiga账号默认密码为：JHinno.666）
```
samba-tool user add jhadmin JHinno.666 --mail-address=jhadmin@jhinno.com
```
4. 文件服务器

    * IP地址：192.168.0.135
    * 管理员：root
    * 密码   ：123.com

4. 文件服务器使用的是192.168.0.188 Windows Server2008 R2 AD 域控服务器

    * 管理员：administrator
    * 密   码：Letmein123


5. 批量创建Samba账号
```
[root@jhserver ~]# cat /samusers.txt 
qpjiang
rkzhang
...
```
```
#!/bin/sh
# add smb user scripts.
# version:1.0
# date:17-02-25
# author:rzhou 

for line in `cat /samusers.txt`;do
        #echo $line
	echo -e "JHinno.666\nJHinno.666" |smbpasswd -a $line -s 
done
```
6. 修改Samba账号密码
```
#!/bin/sh
# add smb user scripts.
# version:1.0
# date:17-02-25
# author:rzhou 

read -p "Please enter your username." username
read -p "Please enter the password you need to modify." password
echo -e "$password\n$password" |smbpasswd -a $username -s
```
7. 磁盘配额
```
#!/bin/bash
#data:2017-06-06
#author:rzhou

for x in `cat users.txt`
do
   #将 ydu 用户的 50G QUOTA 复制给其他用户。
    edquota -p rzhou $x
    su - $x -c "exit;" 
done 

```
8. samba-tool 工具使用
    * samba-tool -h 
    * samba-tool user list
    *  samba-tool user delete your_domain_user
    *  samba-tool user disable your_domain_user
    *  samba-tool user enable your_domain_user
    *  samba-tool user add your_domain_user

9. 参考

    [Samba-tool 工具使用](https://linux.cn/article-8070-1.html)