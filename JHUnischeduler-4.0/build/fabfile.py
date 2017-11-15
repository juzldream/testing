import os
import time
from fabric.api import *
from fabric.operations import *

host1 = 'root@172.17.1.201:22'
host2 = 'root@172.17.1.202:22'

host1_name='rhela'
host2_name='rhelb'
host1_ip='172.17.1.201'
host2_ip='172.17.1.202'

master = (host1)

env.warn_only = True
env.hosts = [host1, host2]
env.password = 'Letmein'
env.command_timeout = None
env.connection_attempts = 10

unischeduler_top = '/apps/unischeduler'
unischeduler_profile = unischeduler_top + '/conf/profile.unischeduler'

module_name = os.environ.get('MODULE_NAME', 'all')
priority_tag = os.environ.get('PRIORITY_TAG', 'all')

@runs_once
def start():
    execute(start_docker, hosts='localhost')
    time.sleep(10)
    execute(prepare_hosts)
    execute(install, hosts=master)
    # execute(start_redis, hosts=master)
    execute(start_jhds)
    time.sleep(10)
    execute(run_test, hosts=master)

@runs_once
def stop():
    # execute(stop_service, hosts=master)
    # execute(stop_jhds)
    # execute(stop_redis, hosts=master)
    execute(stop_docker, hosts='localhost')

def prepare_hosts():
    run('echo "%s %s" >> /etc/hosts' % (host1_ip, host1_name), timeout=60)
    run('echo "%s %s" >> /etc/hosts' % (host2_ip, host2_name), timeout=60)
    run('cat /etc/hosts')

@hosts(master)
def install():
    run('cd /apps; svn --username=wren --password=letmein --no-auth-cache checkout svn://192.168.0.30/tools/trunk/TestAutomation/JHUnischeduler-4.0/build')
    run('/apps/build/myinstall.sh')

@hosts(master)
def clean():
    run('rm -rf %s /apps/unischeduler-4.0.tar.gz' % unischeduler_top)

@hosts(master)
def start_redis():
    run('. %s; %s/etc/redis-jhds start' % (unischeduler_profile, unischeduler_top))

@hosts(master)
def stop_redis():
    run('. %s; %s/etc/redis-jhds stop' % (unischeduler_profile, unischeduler_top))

def start_jhds():
    run('. %s && %s/etc/jhds start && sleep 60' % (unischeduler_profile, unischeduler_top))

def stop_jhds():
    run('. %s && %s/etc/jhds stop && sleep 60' % (unischeduler_profile, unischeduler_top))

def start_service():
    run('. %s; jservice start sched all' % (unischeduler_profile))
    run('. %s; jservice start jobagent all' % (unischeduler_profile))

def stop_service():
    run('. %s; jservice stop sched all' % (unischeduler_profile))
    run('. %s; jservice stop jobagent all' % (unischeduler_profile))

@hosts('localhost')
def start_docker():
    local('sudo rm -rf /tmp/apps')
    local('mkdir -p /tmp/apps')
    # local('sudo rm -rf /tmp/apps/4.0')
    # local('sudo rm -rf /tmp/apps/autotest4')
    # local('sudo rm -rf /tmp/apps/unischeduler')
    # local('sudo rm -rf /tmp/apps/*.tar.gz')
    # local('mkdir -p /tmp/apps')

    local('sudo docker run --privileged --name=%s -h %s --net=\'none\' -d -P -v /tmp/apps:/apps -v /etc/localtime:/etc/localtime unischeduler-test:v1' % (host1_name, host1_name))
    local('sudo ./bind_addr.sh %s %s' % (host1_name, host1_ip))

    local('sudo docker run --privileged --name=%s -h %s --net=\'none\' -d -P -v /tmp/apps:/apps -v /etc/localtime:/etc/localtime unischeduler-test:v1' % (host2_name, host2_name))
    local('sudo ./bind_addr.sh %s %s' % (host2_name, host2_ip))

    # local('sudo cp -rf /home/jhadmin/workspace/tools/trunk/TestAutomation/JHUnischeduler-4.0/build /tmp/apps/')

@hosts('localhost')
def stop_docker():
    local('sudo docker stop %s %s' % (host1_name, host2_name))
    local('sudo docker rm %s %s' % (host1_name, host2_name))

@hosts(master)
def run_test():
    # env.abort_on_prompts = True
    # env.combine_stderr = True
    # env.keepalive = 5
    # env.use_shell = True
    run('/apps/build/test.sh %s %s' % (module_name, priority_tag))

# @hosts(master)
# def test():
#     from fabric.state import output
#     output.output = False
#     env.abort_on_prompts = True
#     env.combine_stderr = False
#     env.keepalive = 5
#     env.use_shell = False
#     run('cd /tmp; time sudo su root -c ". %s && export ROBOT_SYSLOG_FILE=/tmp/syslog.txt && pybot -t case1.addqueue autotest4.0/autotestfile.txt" 2>&1 >> /tmp/my.log' % (unischeduler_profile))
#     # run('cd /tmp; ./test.sh')
