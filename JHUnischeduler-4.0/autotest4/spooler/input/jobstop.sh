#!/bin/sh
echo "stop $JH_JOBID" > $AUTOTEST_TOP/spooler/output/jobstop.txt
kill -19 $JH_JOBPIDS
