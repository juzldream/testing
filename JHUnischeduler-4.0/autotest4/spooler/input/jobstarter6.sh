#!/bin/sh
echo "begin">>$AUTOTEST_TOP/spooler/output/jobstarter-out-6.txt
whoami >> $AUTOTEST_TOP/spooler/output/jobstarter-out-6.txt
for (( i=0;i<15;i++))
do
    echo $i >>$AUTOTEST_TOP/spooler/output/jobstarter-out-6.txt
    sleep 1
done
echo "end">>$AUTOTEST_TOP/spooler/output/jobstarter-out-6.txt
$*
