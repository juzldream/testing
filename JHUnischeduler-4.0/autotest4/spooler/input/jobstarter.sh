#!/bin/sh
sleep 5
whoami > $AUTOTEST_TOP/spooler/output/jobstarter-out.txt
$*
