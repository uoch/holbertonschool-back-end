#!/usr/bin/python3
"""
Write a Python script that, using this REST API, for a
given employee ID, returns information about his/her TODO
list progress.
"""
import requests
import sys


def get_todo_list_data(employee_id):
    employee_data = requests.get(
        f"https://jsonplaceholder.typicode.com/users/{employee_id}").json()
    employee_name = employee_data["name"]

    todos_data = requests.get(
        f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}").json()

    total_number_of_tasks = len(todos_data)
    number_of_done_tasks = len(
        [task for task in todos_data if task["completed"]])

    return employee_name, number_of_done_tasks, total_number_of_tasks, todos_data


if __name__ == "__main__":
    employee_id = int(sys.argv[1])
    employee_name, number_of_done_tasks, total_number_of_tasks, todos_data = get_todo_list_data(
        employee_id)

    progress = f"{number_of_done_tasks}/{total_number_of_tasks}"

    print("Employee {} is done with tasks({}):".format(employee_name, progress))
    for task in todos_data:
        if task["completed"]:
            print(f"\t{task['title']}")
