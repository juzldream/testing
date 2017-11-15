#!/bin/sh

host1=rhela
host2=rhelb

cd /apps/
wget -c http://192.168.0.43/build/jhinno_ext/jh_unischeduler_ext/trunk/`date +%Y-%m-%d`/unischeduler-4.0.0-linux-`date +%Y%m%d`.tar.gz
tar zxvf unischeduler-4.0.0-linux-`date +%Y%m%d`.tar.gz

cd /apps/unischeduler/install/; rm -f install.conf

cd /apps/unischeduler/install/; ./install.sh << AAA
$host1,$host2
$host1
jcluster
jhadmin
AAA

sed -i "17 d" /apps/unischeduler/conf/hosts.conf
sed -i "16 a$host1    1     ()" /apps/unischeduler/conf/hosts.conf
sed -i "17 a$host2    1     ()" /apps/unischeduler/conf/hosts.conf
sed -i 's/CLI_COMPATIBLE = y/#CLI_COMPATIBLE = y/g' /apps/unischeduler/conf/scheduler.conf

mkdir /apps/4.0; cd /apps/4.0; ln -s /apps/unischeduler
