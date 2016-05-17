#! /usr/bin/python
#!-*- coding:utf-8 -*-

import time
import json
import socket
import os

i = 0
data = []
ts = int(time.time())
host = os.uname()[1]
Core = os.popen("ls /sys/devices/platform/coretemp.0/temp*_input")

def get_temperature(value):
	s = {}
	s['endpoint'] = host
	s['metric'] = "cpu.temperature.Core." + str (i)
	s['timestamp'] = ts
	s['step']= 300
	s['value'] = value
	s['counterType'] = 'GAUGE'
	s['tags'] =  ''
	data.append(s)
for c in Core:
	file = open(c.strip('\n'))
	te = float(file.read()) / 1000
	file.close()
	get_temperature(te)
	i += 1
print (json.dumps(data))
