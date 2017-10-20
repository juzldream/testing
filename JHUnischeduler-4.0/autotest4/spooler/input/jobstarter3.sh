#!/bin/sh
whoami > $AUTOTEST_TOP/spooler/output/jobstarter-out-3.txt
name=`hostname`
echo $name | tr '[A-Z]' '[a-z]'
$*
