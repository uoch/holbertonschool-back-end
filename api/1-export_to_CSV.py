#!/usr/bin/python3
"""
Using what you did in the task #0,
extend your Python script
to export data in the CSV format.
"""
if __name__ == '__main__':
    import csv
    import requests
    import sys

    num = sys.argv[1]
    response = requests.get(
        'https://jsonplaceholder.typicode.com/users/' + num)
    todos = requests.get(
        'https://jsonplaceholder.typicode.com/todos?userId=' + num)

    employee = response.json()
    todos = todos.json()
    id = employee['id']
    name = employee['username']

    with open(f'{num}.csv', 'w') as file:
        for i in todos:
            Task = i['completed']
            TASK_TITLE = i['title']
            TASK_COMPLETED_STATUS = i['completed']
            TASK_TITLE = i['title']
            file.write(
                f"\"{id}\",\"{name}\",\"{Task}\",\"{TASK_TITLE}\"\n")
