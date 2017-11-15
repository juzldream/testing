#!/bin/sh
echo "kill $JH_JOBID">$AUTOTEST_TOP/spooler/output/jobkill1.txt
kill -15 -$JH_JOBPGIDS
kill -9 -$JH_JOBPGIDS
