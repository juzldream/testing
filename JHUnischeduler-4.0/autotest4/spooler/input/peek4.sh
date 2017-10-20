#!/bin/sh
echo "prebegin"
for (( i=0; i<5; i++ ))
do
echo $JH_JOBID
sleep 1
done
echo "preend"

