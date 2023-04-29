#!/usr/bin/python3
"""
Using what you did in the task #0,
extend your Python script
to export data in the CSV format.
"""


if __name__ == '__main__':
	import requests
	import sys
	import csv
	import importlib


	module = importlib.import_module('0-gather_data_from_an_API')
	getdata = module.getdata

	employee_id = int(sys.argv[1])
	employe_name, tasks_completed, total, todos_data = getdata(employee_id)

	with open(f'{employee_id}.csv', 'w') as f:
		csv_writer = csv.writer(f, quoting=csv.QUOTE_MINIMAL,
								quotechar='"', delimiter=',')

		# Write header row
		csv_writer.writerow(['id', 'name', 'completed', 'title'])
		for todo in todos_data:
			csv_writer.writerow([str(employee_id), employe_name,
								str(todo['completed']), todo['title']])
