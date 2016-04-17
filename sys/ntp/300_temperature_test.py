#! /usr/bin/env python
#!-*- coding:utf-8 -*-


#import requests
import time
import json
import socket
import os

i = 0
data = []
ts = int(time.time())
host = os.uname()[1]
Core = os.popen("sensors | grep Core | awk -F '[+°]' '{print $2}'")

def get_temperature(value):
	s = {}
	s['endpoint'] = host
	s['metric'] = "cpu.temperature.Core."+ str(i)
	s['timestamp'] = ts
	s['step']= 60
	s['value'] = value
	s['counterType'] = 'GAUGE'
	s['tags'] =  ''
	data.append(s)
for te in Core:
	get_temperature(float(te.strip('\n')))
	i += 1
#print Core
print json.dumps(data)
