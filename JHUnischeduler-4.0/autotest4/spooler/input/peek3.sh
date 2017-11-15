#!/bin/sh
echo "begin"
sleep 10
for (( i=0; i<3; i++ ))
do
echo $JH_JOBID
sleep 1
done
echo "end"
