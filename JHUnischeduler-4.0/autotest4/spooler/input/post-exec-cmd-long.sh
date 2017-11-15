#!/bin/sh
#AUTOTEST_TOP="/apps/autotest4/"
echo "begin" >> $AUTOTEST_TOP/spooler/output/post-exec-long.txt
whoami >> $AUTOTEST_TOP/spooler/output/post-exec-long.txt
for (( i=0;i<12;i++))
do
    echo $i>> $AUTOTEST_TOP/spooler/output/post-exec-long.txt
    sleep 1
done
echo "end">> $AUTOTEST_TOP/spooler/output/post-exec-long.txt
