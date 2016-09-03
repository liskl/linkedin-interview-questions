#!/usr/bin/env python3

import requests
import json

def printEmployeeData( EmployeeDict ):
	return '{} - {}'. format( EmployeeDict['name'], EmployeeDict['title'])

def getEmployeeDirectReports( employeeId , mock=1 ):
	baseurl = 'http://www.linkedin.corp/api/{}/{}'.format('employee', employeeId )

	
	# { "name":"", "title": "", "reports":[]}

	if ( mock == 0 ):
		api_session = requests.session()
		response = api_session.get(baseurl)
		data = json.loads(response.text)
	else:
		data = {"name":"Flynn Mackie","title":"Senior VP of Engineering","reports":[{"name":"Wesley Thomas","title":"VP of Design","reports":[{"name":"Randall Cosmo","title":"Director of Design","reports":[{"name":"Brenda Plager","title":"Senior Designer","reports":[]}]}]},{"name":"Nina Chiswick","title":"VP of Engineering","reports":[{"name":"Tommy Quinn","title":"Director of Engineering","reports":[{"name":"Jake Farmer","title":"Frontend Manager","reports":[{"name":"Liam Freeman","title":"Junior Code Monkey","reports":[]}]},{"name":"Sheila Dunbar","title":"Backend Manager","reports":[{"name":"Peter Young","title":"Senior Code Cowboy","reports":[]}]}]}]}]}
	return data

def getEmployeeId( EmployeeDict ):
	return EmployeeDict['reports']


a = 0
tabs=''

TODO: Still having issues With the Output but it is to Late to handle right now.

output = []
while a == 0:
	curr_employee = getEmployeeDirectReports( id )
	print('{}{}'.format(tabs, printEmployeeData(curr_employee)))
	if not getEmployeeId( curr_employee ):
		a == 1
	elif getEmployeeId(curr_employee):
		id = getEmployeeId( curr_employee )
		tabs = ''.format(tabs, ' ')

#for i in output:
#	print(''.format(i))
