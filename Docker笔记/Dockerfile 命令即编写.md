1. LAGEL、ADD、COPY、EXPOSE、WORKDIR、VOLUME、RUN命令使用

    ```
    # Description: test Docker LAGEL、ADD、COPY、EXPOSE、WORKDIR、VOLUME、RUN command .
    
    
    FROM busybox:latest
    MAINTAINER "RACHER <juzldream@fixmail.com>"
    
    #LABEL maintainer="RACHER <juzldream@foxmail.com>"
    ENV DOC_ROOT=/data/web/html/ \
        WEB_SERVER_PACKAGE="nginx-1.15.3.tar.gz"
    
    COPY index.html ${DOC_ROOT:-/data/web/html/}
    COPY yum.repos.d /etc/yum.repos.d/
    #ADD http://nginx.org/download/nginx-1.15.3.tar.gz /usr/local/src/ 
    
    WORKDIR /usr/local/
    ADD nginx-1.15.3.tar.gz ./src/
    
    #ADD nginx-1.15.3.tar.gz /usr/local/src/
    #ADD ${WEB_SERVER_PACKAGE} /usr/local/src/
    
    VOLUME /data/mysql/
    EXPOSE 80/tcp 11211/udp
    #RUN cd /usr/local/src/ $$ \
     #   tar -xf ${WEB_SERVER_PACKAGE} $$ \
      #  echo Dockerfile com test. > test.log   $$ \
    RUN yum -y install epel-release && \
        yum makecache && yum install vim
    ```

2. 编写一个 CentOS系统 安装lrzsz镜像

    ```
    # Description: test CentOS-7 install lrzsz.
    
    
    FROM centos
    MAINTAINER "RACHER <juzldream@fixmail.com>"
    
    RUN yum -y install epel-release && \
        yum -y makecache && yum -y install lrzsz
    ```
3. 基于busybox编写web服务器

    ```
    FROM busybox
    LABEL maintainer="racher <juzldream@foxmaix.com app=httpd>"
    
    ENV WEB_DOC_ROOT="/data/web/html/"
    
    RUN mkdir -p ${WEB_DOC_ROOT} && \
        echo '<h1>Busybox httpd server.</h1>' > ${WEB_DOC_ROOT}index.html
    
    #CMD /bin/httpd -f -h ${WEB_DOC_ROOT}
    #CMD ["/bin/sh","-c","/bin/httpd","-f","-h ${WEB_DOC_ROOT}"]
    ENTRYPOINT /bin/httpd -f -h ${WEB_DOC_ROOT}
    ```
4. 编写nginx镜像

    ```
    [root@testcent img3]# ls
    Dockerfile  entrypoint.sh  index.html
    [root@testcent img3]# cat entrypoint.sh index.html Dockerfile 
    #!/bin/sh
    #
    #
    
    cat > /etc/nginx/conf.d/www.conf << eof
    server {
            server_name $HOSTNAME;
            listen ${IP:-0.0.0.0}:${PORT:-80};
            root ${NGX_DOC_ROOT:-/usr/share/nginx/html};
    }
    eof
    exec "$@"
    <h1>new doc root fot nginx.</h1>
    FROM nginx:1.14-alpine
    
    #ARG nginx_tag="1.14-alpine"
    ARG author="racher <juzldream@foxmail.com>"
    
    LABEL maintainer=${author}
    
    ENV NGX_DOC_ROOT='/data/web/html/'
    
    ADD index.html ${NGX_DOC_ROOT} 
    ADD entrypoint.sh /bin/
    
    EXPOSE 80/tcp
    
    #HEALTHCHECK --start-period=3s CMD wge -O - -q http://${IP:-0.0.0.0}:${PORT:-80}/
    HEALTHCHECK --start-period=3s CMD wge -O - -q http://${IP:-0.0.0.0}:10080/
    
    CMD ["/usr/sbin/nginx","-g","daemon off;"]
    ENTRYPOINT ["/bin/entrypoint.sh"]
    ```

6. 构建Docker镜像

    `docker build -t tinyhttpd:v0.0.3 ./`
    
7. 运行镜像

    `docker container run --name tinyweb1 -P --rm tinyhttpd:v0.0.7 ls /usr/local/src/`