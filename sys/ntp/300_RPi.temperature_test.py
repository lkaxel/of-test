#! /usr/bin/python
#!-*- coding:utf-8 -*-

from subprocess import Popen, PIPE
from tempfile import TemporaryFile
import time
import json
import socket
import os

i = 0
data = []
ts = int(time.time())
host = os.uname()[1]
file = open("/sys/class/thermal/thermal_zone0/temp")
te = float(file.read()) / 1000
file.close() 
def get_temperature(value):
	s = {}
	s['endpoint'] = host
	s['metric'] = "RPi.cpu.temperature"
	s['timestamp'] = ts
	s['step']= 300
	s['value'] = value
	s['counterType'] = 'GAUGE'
	s['tags'] =  ''
	data.append(s)
#for te in Core:
get_temperature(te)
#	i += 1
#print te
print (json.dumps(data))
