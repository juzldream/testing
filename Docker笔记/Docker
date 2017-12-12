Docker

安装
yum -y install docker

Windows 7、8安装

https://github.com/boot2docker/boot2docker

启动
service docker start

下载镜像
docker pull ubuntu

查看本地镜像
docker images



运行容器

交互式容器
docker run -it ubuntu /bin/bash

守护式容器

查看容器基本信息

docker ps
docker ps -a

docker inspect ae5
docker inspect -f {{.NetworkSettings.IPAddress}} fc5
docker inspect -f {{.ID}} ae5



停止容器

docker stop ea3

删除容器
docker rm ae5

	
docker info

列出镜像

docker images
docker images -a
docker images -q
docker images centos

REPOSITORY  创库
REGISTRY  
TAG  

查看镜像

docker inspect Ubuntu:14.04

删除镜像

docker rmi Ubuntu:14.04

构建镜像

docker commit  通过容器构建
docker build   通过Dockerfile文件构建

获取和推送镜像

查找镜像

https://registry.hub.docker.com

docker search Ubuntu
docker search Ubuntu -s 3

拉取镜像

docker pull Ubuntu:14.04

https://www.daocloud.io

推送镜像

docker push 