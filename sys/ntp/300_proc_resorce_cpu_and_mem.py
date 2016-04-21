#! /usr/bin/env python
#!-*- coding:utf-8 -*-


#import requests
import time
import json
import socket
import os

data = []
ts = int(time.time())
host = os.uname()[1]

def get_mem(value):
	mem_cmd ="ps aux | grep " + str(value) + "|awk '{sum+=$4} END {print sum}'"
	s = {}
        s['endpoint'] = host
        s['metric'] = 'mem_' + str(value)
        s['timestamp'] = ts
        s['step']= 300
        s['value'] = float(os.popen(mem_cmd).read().strip())
        s['counterType'] = 'GAUGE'
        s['tags'] =  ''
	data.append(s)


def get_cpu(value):
	cpu_cmd ="ps aux | grep " + str(value) + "|awk '{sum+=$3} END {print sum}'"
	s = {}
        s['endpoint'] = host
        s['metric'] = 'cpu_' + str(value)
        s['timestamp'] = ts
        s['step']= 300
        s['value'] = float(os.popen(cpu_cmd).read().strip())
        s['counterType'] = 'GAUGE'
        s['tags'] =  ''
	data.append(s)
processes = ['apache2', 'mysql', 'tomcat', '/usr/bin/java']

for process in processes:
	get_mem(process)
#for process in processes:
	get_cpu(process)
print json.dumps(data)
