#!/bin/sh
N=$1
if [ "x$N" = "x" ]; then
    N=100000
fi
echo "scale=$N; a(1)*1" |bc -l
