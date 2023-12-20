#!/usr/bin/python3
"""
Script that, using a REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""

import requests
from sys import argv


if __name__ == '__main__':
    """Script for task0"""
    user_request = requests.get(
        'http://jsonplaceholder.typicode.com/users/{}'.format(argv[1])).json()
    todos_req = requests.get(
        'http://jsonplaceholder.typicode.com/todos').json()
    csvs = ""
    name = str(user_request.get('username'))
    uid = argv[1]
    for task in todos_req:
        if task.get('userId') == int(argv[1]):
            csvs += ("\"{}\",\"{}\",\"{}\",\"{}\"\n"
                     .format(uid,
                             name,
                             task.get('completed'),
                             task.get('title')))
    with open(("{}.csv").format(uid), "w", encoding="utf-8") as f:
        f.write(csvs)
