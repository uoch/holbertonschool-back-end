#!/usr/bin/python3
"""
Write a Python script that, using this REST API, for a
given employee ID, returns information about his/her TODO
list progress.
"""
import requests
import sys


EMPLOYEE_API_URL = "https://jsonplaceholder.typicode.com/users"
TODO_API_URL = "https://jsonplaceholder.typicode.com/todos"


def getdata(employee_id):
    data = requests.get(f"{EMPLOYEE_API_URL}/{employee_id}").json()
    employe_name = data["name"]

    todos_data = requests.get(f"{TODO_API_URL}?userId={employee_id}").json()

    total = len(todos_data)
    tasks_completed = len([task for task in todos_data if task["completed"]])

    return employe_name, tasks_completed, total, todos_data


if __name__ == "__main__":
    employee_id = int(sys.argv[1])
    employe_name, tasks_completed, total, todos_data = getdata(employee_id)

    progress = "{}/{}".format(tasks_completed, total)

    print("Employee {} is done with tasks({}):".format(employe_name, progress))
    for task in todos_data:
        if task["completed"]:
            print(f"\t{task['title']}")
