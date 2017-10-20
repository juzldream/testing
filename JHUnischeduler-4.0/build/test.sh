#!/bin/sh

host1=rhela
host2=rhelb

module_name=$1
priority_tag=$2
if [ "x$priority_tag" == "xall" ]; then
	priority_tag=''
else
	priority_tag=" --include $priority_tag"
fi

cd /apps/
svn --username=fkong --password=letmein --no-auth-cache checkout svn://192.168.0.30/tools/trunk/TestAutomation/JHUnischeduler-4.0/autotest4
chmod -Rf 777 autotest4
cd /apps/autotest4/

echo "module name: $module_name"
echo "priority tag: $priority_tag"

ls -al testcase

sed -i "s/MASTER_HOST=\"rhela1\"/MASTER_HOST=\"$host1\"/g" /apps/autotest4/autotest_prepare
sed -i "s/SLAVE_LINUX=\"rhelb\"/SLAVE_LINUX=\"$host2\"/g" /apps/autotest4/autotest_prepare

# sudo su root -c ". /apps/unischeduler/conf/profile.unischeduler && export ROBOT_SYSLOG_FILE=/tmp/syslog.txt && pybot -t case1.addqueue autotestfile.txt" 2>&1 >> /apps/autotest4.0/log.txt << AAA
# sudo su root -c ". /apps/unischeduler/conf/profile.unischeduler && export ROBOT_SYSLOG_FILE=/tmp/syslog.txt && export AUTOTEST_ENV=/apps/autotest4 && pybot /apps/autotest4" 2>&1 >> /apps/autotest4/log.txt << AAA
if [ "x$module_name" == "xall" ]; then
	. /apps/unischeduler/conf/profile.unischeduler && . /apps/autotest4/autotest_prepare && export ROBOT_SYSLOG_FILE=/tmp/syslog.txt && export AUTOTEST_ENV=/apps/autotest4 && pybot $priority_tag --exclude docker-not-run /apps/autotest4/testcase/
else
	. /apps/unischeduler/conf/profile.unischeduler && . /apps/autotest4/autotest_prepare && export ROBOT_SYSLOG_FILE=/tmp/syslog.txt && export AUTOTEST_ENV=/apps/autotest4 && pybot $priority_tag --exclude docker-not-run /apps/autotest4/testcase/$module_name
fi

cd /apps/autotest4
mkdir -p reports_${module_name}
mv log.html reports_${module_name}/
mv report.html reports_${module_name}/
mv output.xml reports_${module_name}/

exit 0
