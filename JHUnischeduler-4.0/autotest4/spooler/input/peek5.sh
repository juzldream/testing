#!/bin/sh
echo "jobbegin"
for (( i=0; i<15; i++ ))
do
echo $JH_JOBID
sleep 1
done
echo "jobend"

