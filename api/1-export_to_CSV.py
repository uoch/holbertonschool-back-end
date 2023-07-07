#!/usr/bin/python3
"""
Using what you did in the task #0,
extend your Python script
to export data in the CSV format.
"""
from funct import getdata2,printf

if __name__ == '__main__':
    import requests
    import sys
    import csv
    import importlib
    module = importlib.import_module('funct')
    getdata = module.getdata2

    employee_id = int(sys.argv[1])
    employe_name, tasks_completed, total, todos_data = getdata(employee_id)

    with open(f'{employee_id}.csv', 'w') as f:
        csv_writer = csv.writer(f,
                                delimiter=',')
        for todo in todos_data:
            csv_writer.writerow(printf([employee_id, employe_name,
                                        todo['completed'], todo['title']]))
