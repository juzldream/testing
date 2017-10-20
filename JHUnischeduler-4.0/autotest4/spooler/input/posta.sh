#!/bin/sh
echo $JH_JOBID>$AUTOTEST_TOP/spooler/output/jobout$JH_JOBID.txt
for i in {1..10};do
   echo $i>>$AUTOTEST_TOP/spooler/output/jobout$JH_JOBID.txt
   let i=i+1
   sleep 1
done;
