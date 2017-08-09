#!/usr/bin/python
# -*- coding: utf-8 -*-
# 
import urllib
import urllib2
import requests 


url = 'http://192.168.0.93:8080/appform/ws/filedownload' 
data = {'path':'/apps/jhappform/conf/appform.conf','token':'C0141A0BB2442308A1BC59162148CA2847899E89CDF7DCC887883633D8A24D8E4A7F790CD928232D3D9A4254CF60554B869F04E4D1AE626D60B41552560DF7FDE76EE8622166F3E8A765DC8E1CD585E4'}
r = requests.get(url, params=data)
print r.content






