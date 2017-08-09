#!/usr/bin/python
# -*- coding: utf-8 -*-
#
import json
import urllib
import urllib2
import tool
import os
 
import commands



cm = "cd /apps/jhappform/spoolers/jhadmin/;mkdir testplus_2017;cd testplus_2017;touch files.txt readme.md log.doc"

sh = commands.getstatusoutput(cm)
print sh

