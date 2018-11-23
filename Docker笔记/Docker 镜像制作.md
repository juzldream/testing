* 基于容器制作镜像
`docker container commit -p c93dd2c325fc`
`docker commit -a "racher <11@qq.com>" -c 'CMD ["/bin/httpd","-f","-h","/data/html"]' -p t2 racher/web:v0.2`
* 镜像打标签
`docker image tag c93dd2c325fc racher/web:latest`
* 上传镜像
`docker image push registry.cn-hangzhou.aliyuncs.com/racher/web:v0.10`
* 下载镜像
`docker image pull 1576768715/web:latest`

* 镜像地址
    - https://quay.io
    - https://dev.aliyun.com/
    - https://hub.docker.com/
