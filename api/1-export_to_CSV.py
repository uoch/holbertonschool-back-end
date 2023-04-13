#!/usr/bin/python3
"""Using what you did in the task #0, extend your Python script to export data in the CSV format.
"""

import requests
import sys
import csv

# Retrieve employee data
employee_id = sys.argv[1]
employee_response = requests.get('https://jsonplaceholder.typicode.com/users/' + employee_id)
employee_data = employee_response.json()

todos_response = requests.get('https://jsonplaceholder.typicode.com/todos?userId=' + employee_id)
todos_data = todos_response.json()

employee_name = employee_data['username']

# Write data to CSV file
with open(f'{employee_id}.csv', 'w') as csv_file:
    csv_writer = csv.writer(csv_file, delimiter=',')

    # Write header row
    csv_writer.writerow(['id', 'name', 'completed', 'title'])

    # Write data rows
    for todo in todos_data:
        completed_status = todo['completed']
        task_title = todo['title']
        csv_writer.writerow([employee_id, employee_name, completed_status, task_title])

