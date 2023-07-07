#!/usr/bin/python3
"""
Write a Python script that, using this REST API, for a
given employee ID, returns information about his/her TODO
list progress.
"""
import requests
import sys
from funct import getdata

if __name__ == "__main__":
    employee_id = int(sys.argv[1])
    employe_name, tasks_completed, total, todos_data = getdata(employee_id)

    progress = "{}/{}".format(tasks_completed, total)

    print("Employee {} is done with tasks({}):".format(employe_name, progress))
    for task in todos_data:
        if task["completed"]:
            print(f"\t{task['title']}")