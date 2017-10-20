FROM gpmidi/centos-6.5

MAINTAINER Fanbin Kong "kongxx@hotmail.com"

RUN yum install -y sudo tar wget openssh-server openssh-clients openssl openssl-devel subversion
RUN yum install -y epel-release
RUN yum install -y python-setuptools
RUN easy_install pip
RUN pip install robotframework robotframework-ride

RUN yum install -y make gcc zlib.x86_64 zlib-devel.x86_64 python-devel.x86_64
RUN pip install psutil==2.1

RUN sed -i 's/UsePAM yes/UsePAM no/g' /etc/ssh/sshd_config
RUN sed -i 's/UseDNS yes/UseDNS no/g' /etc/ssh/sshd_config
RUN echo 'root:Letmein' | chpasswd
RUN useradd -u 1000 jhadmin
RUN echo "jhadmin:jhadmin" | chpasswd
RUN echo "jhadmin   ALL=(ALL)       NOPASSWD: ALL" >> /etc/sudoers

RUN useradd user1 \
    && useradd user2 \
    && useradd user3 \
    && useradd user4 \
    && useradd user5 \
    && useradd user6 \
    && useradd user7 \
    && useradd user8 \
    && useradd user9 \
    && useradd user10

RUN echo "user1:user1" | chpasswd \
    && echo "user2:user2" | chpasswd \
    && echo "user3:user3" | chpasswd \
    && echo "user4:user4" | chpasswd \
    && echo "user5:user5" | chpasswd \
    && echo "user6:user6" | chpasswd \
    && echo "user7:user7" | chpasswd \
    && echo "user8:user8" | chpasswd \
    && echo "user9:user9" | chpasswd \
    && echo "user10:user10" | chpasswd

RUN ssh-keygen -t dsa -f /etc/ssh/ssh_host_dsa_key
RUN ssh-keygen -t rsa -f /etc/ssh/ssh_host_rsa_key
RUN mkdir /var/run/sshd

# RUN mkdir /home/jhadmin/.ssh
# RUN chown jhadmin:jhadmin  /home/jhadmin/.ssh
# RUN chmod -R 700 /home/jhadmin/.ssh

# ADD id_rsa.pub /home/jhadmin/.ssh/authorized_keys
# RUN chown jhadmin:jhadmin  /home/jhadmin/.ssh/authorized_keys
# RUN chmod 600 /home/jhadmin/.ssh/authorized_keys

# ADD id_rsa /home/jhadmin/.ssh/
# RUN chown jhadmin:jhadmin /home/jhadmin/.ssh/id_rsa

RUN yum install -y bc

EXPOSE 22
CMD ["/usr/sbin/sshd", "-D"]
