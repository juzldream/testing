#!/bin/sh
for (( i=0;i<300;i++))
do
    echo $i >> $AUTOTEST_TOP/spooler/output/pre-stop.txt
    sleep 1
done
~   
