#!/usr/bin/env python3
import os
import operator
import json

log_files = [ '/var/log/messages', '/var/log/syslog' ]


for log_file in log_files:
	
	if os.path.exists( log_file ):
		with open( log_file, "r") as log:
			LogRow={}
			for i in log.readlines():
				l=i.split(' ')
				d=i.split(l[4])
				date=d[0].split(":")
				time=date[0]+":"+date[1]
				if time not in dict.keys(LogRow):
					LogRow[time]=1
				else:
					LogRow[time]+=1

		for key, value in reversed(sorted(LogRow.items(), key=lambda e: e[1], )):
			print('{}:{}'.format(key, str(value)))
	else:
		print ('unable to find log file: {}'.format(log_file))
