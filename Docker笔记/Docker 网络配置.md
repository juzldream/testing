### netns 用法
* 查看帮助

    ```
    [root@testcent ~]*  ip netns help
    Usage: ip netns list
           ip netns add NAME
           ip netns set NAME NETNSID
           ip [-all] netns delete [NAME]
           ip netns identify [PID]
           ip netns pids NAME
           ip [-all] netns exec [NAME] cmd ...
           ip netns monitor
           ip netns list-id
    ```
* 添加namespace

    `ip netns add ns1`

* 显示所有的虚拟网络命名空间
    
   ` ip netns list`
    `ls /var/run/netns`
    
* 显示ns1网络
    
    `ip netns exec ns1 ifconfig -a`
    
    `ip netns exec ns1 ip addr`

* 增加一对veth虚拟网卡
    
    `ip link add type veth`
    `ip link add name veth1.1 type veth peer name veth1.2`

* 查询添加测虚拟网卡

    `ip link show`
    `ip addr`

* 将veth1.2添加到ns1虚拟网络环境

    `ip link set dev veth1.2 netns ns1`

* 将虚拟网卡veth1改名为eth0并添加到ns2虚拟网络环境中
    ```
    ip link set dev veth1 name eth0 netns ns2
    ip netns exec ns2 ip addr  #查询ns2虚拟网络网卡情况
    ```
* 查询ns1虚拟网络配置
    `ip netns exec r1 ifconfig -a`

* 修改ns1虚拟网络网卡veth1.2名称为eth0
    `ip netns exec ns1 ip link set dev veth1.2 name eth0`

* 激活veth1.1网卡设备

    `ifconfig veth1.1 10.1.0.1/24 up`

* 设置虚拟网络环境ns2的eth0设备处于激活状态

    `ip netns exec ns1 ip link set eth0 up`

* 为虚拟网络环境ns2的eth0设备增加IP地址

    `ip netns exec ns2 ip address add 10.0.1.1/24 dev eth0 `   

* 激活ns1虚拟网络eth0网卡设备并设置ip地址

    `ip netns exec ns1 ifconfig eth0 10.1.0.2/24 up`

### docker容器4中网络模式

* 创建none网络容器，ifconfig命令查询只有lo

    `docker container run --name t1 -it --network none --rm busybox:latest`

* 创建桥接网络容器

    `docker container run --name t1 -it --network bridge --rm busybox:latest`

* 使用宿主机ip地址

    `docker container run --name b2 --network host -it busybox ` 

* 使用web2容器的ip地址

    `docker container run --name web2 --network container:web1 -it --rm busybox `

* 创建hostname为testcent主机名的容器

    `docker container run --name t1 -it --network bridge -h testcent --rm busybox:latest `

* 创建dns为114.114.114.114容器
    ```
    docker container run --name t1 -it --dns 114.114.114.114 --rm busybox:latest 
    
    docker container run --name t1 -it --dns 114.114.114.114 --dns-search juzldream.fun --add-host www.juzldream.fun:1.1.1.1 --rm busybox   
    ```

### 杂项

* 安装brctl用来管理以太网桥

    `  yum install bridge-utils -y`

* 查询网桥信息

    `brctl show ` 

* 查看nat防火墙配置

    `iptables -t nat -vnL  `





