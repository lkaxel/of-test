#! /usr/bin/python
#!-*- coding:utf-8 -*-
from __future__ import division
import time
import json
import socket
import os
#import re
import commands
i = 0
data = []
ts = int(time.time())
host = os.uname()[1]
#with open("/proc/meminfo") as A:
#	memtotal = memfree = ''
#	for eachline in A:
#		memtotal = re.match("MemTotal(.*?)\s",eachline)
#		memfree = re.match("MemFree(.*?)\s",eachline)
#		print memfree
(a,memtotal) = commands.getstatusoutput("cat /proc/meminfo |grep MemTotal|awk '{print $2}'")
(b,memfree) = commands.getstatusoutput("cat /proc/meminfo |grep MemFree|awk '{print $2}'")
def get_memfree(value):
        s = {}
        s['endpoint'] = host
        s['metric'] = "memfree.custom"
        s['timestamp'] = ts
        s['step']= 300
        s['value'] = value
        s['counterType'] = 'GAUGE'
        s['tags'] =  ''
        data.append(s)

get_memfree(float(int(memfree)/1024))

def get_memused(value):
        s = {}
        s['endpoint'] = host
        s['metric'] = "memused.custom"
        s['timestamp'] = ts
        s['step']= 300
        s['value'] = value
        s['counterType'] = 'GAUGE'
        s['tags'] =  ''
        data.append(s)

get_memused(float(int(memtotal) - int(memfree))/1024)


def get_free_percent(value):
        s = {}
        s['endpoint'] = host
        s['metric'] = "memfree.percent.custom"
        s['timestamp'] = ts
        s['step']= 300
        s['value'] = value
        s['counterType'] = 'GAUGE'
        s['tags'] =  ''
        data.append(s)

get_free_percent(float(int(memfree)/int(memtotal)*100))
print (json.dumps(data))


