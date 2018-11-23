* 下载repo文件
`wget https://mirrors.tuna.tsinghua.edu.cn/docker-ce/linux/centos/docker-ce.repo`
* 修改repo文件配置
`:s@https://download.docker.com/@https://mirrors.tuna.tsinghua.edu.cn/docker-ce/@`

* 配置阿里云yum安装container-selinux
    ```
    wget -O /etc/yum.repos.d/CentOS-Base.repo http://mirrors.aliyun.com/repo/Centos-7.repo  
    yum install container-selinux
    ```
* Docker安装
    ```
    yum install Docker
    yum install docker-ce
    ```

* Docker 命令
    - 启动Docker
    ```
    systemctl start docker
    systemctl status docker
    systemctl stop docker
    ```
    - 显示Docker版本信息
    `docker --version`
    - 显示Docker环境信息
    `docker info`
    - 下载镜像
    `docker pull busybox`
    - 查看镜像
    `docker image ls`
    `docker image ls --no-trunc`
    - 删除镜像
    `docker image rm nginx:1.12-alpine`
    - 查看容器
    `docker container ls`
    `docker container ls -a`
    `docker ps`
    - 查看网络
    `docker network ls`
    - 启动busybox容器
    `docker container run --name bx -it busybox:latest `
    - 运行nginx
    `docker container run --name web1 -d nginx:1.14-alpine`
    - 显示容器详细信息
    `docker inspect bx`
    - 进入容器
    `docker container exec -it web1 /bin/sh`
    - 停止容器
    `docker container stop bx`
    - 查看容器日志
    `docker container logs web1`
* Docker 生命周期级命令

    ![Docker生命周期](https://mmbiz.qpic.cn/mmbiz_png/4iaE7bB4HCjciaic3Io8fF1ibyXQicwMDiamOAPCue3pdQ067x6qZxp7zprmn2WnQD5aO1MgV9VJNGEjADreoojU6YzA/0?wx_fmt=png)

* [清华大学开源软件镜像站](https://mirrors.tuna.tsinghua.edu.cn)