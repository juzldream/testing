#!/bin/sh
echo "resume $JH_JOBID">$AUTOTEST_TOP/spooler/output/jobresume.txt
kill -18 $JH_JOBPIDS
