#!/bin/sh
echo "kill $JH_JOBID">$AUTOTEST_TOP/spooler/output/jobkill.txt
kill -15 $JH_JOBPIDS
kill -9 $JH_JOBPIDS
