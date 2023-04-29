#!/usr/bin/python3
"""
Write a Python script that, using this REST API, for a
given employee ID, returns information about his/her TODO
list progress.
"""
import requests
import sys


def getdata(employee_id):
    data = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}".format(employee_id)).json()
    employee_name = data["name"]

    todos_data = requests.get(
        f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}").json()

    total = len(todos_data)
    tasks_completed = len([task for task in todos_data if task["completed"]])

    return employee_name, tasks_completed, total, todos_data


if __name__ == "__main__":
    employee_id = int(sys.argv[1])
    employee_name, tasks_completed, total, todos_data = getdata(employee_id)

    progress = "{}/{}".format(tasks_completed,total)

    print("Employee {} is done with tasks({}):".format(employee_name, progress))
    for task in todos_data:
        if task["completed"]:
            print(f"\t{task['title']}")
