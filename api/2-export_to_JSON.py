#!/usr/bin/python3
"""
Script that, using a REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""

import json
import requests
from sys import argv


if __name__ == '__main__':
    """Script for task0"""
    user_request = requests.get(
        'http://jsonplaceholder.typicode.com/users/{}'.format(argv[1])).json()
    todos_req = requests.get(
        'http://jsonplaceholder.typicode.com/todos').json()
    dic = {}
    name = user_request.get('username')
    uid = argv[1]
    dic[uid] = []
    for i in todos_req:
        aux = {}
        if i.get('userId') == int(uid):
            aux['task'] = i.get('title')
            aux['completed'] = i.get('completed')
            aux['username'] = name
            dic[uid].append(aux)

    with open(("{}.json").format(uid), "w", encoding='utf-8') as f:
        json.dump(dic, f)
