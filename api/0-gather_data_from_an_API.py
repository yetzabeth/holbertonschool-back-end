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
    usr_todos_list = [x for x in todos_req if x.get(
        'userId') == int(argv[1])]
    # (x) Elemento dentro de los elementos de todos_request solamente si
    user_completed_list = [
        x for x in usr_todos_list if x.get('completed') is True]
    # Recorremos la lista de todos nuevamente para filtrar tareas completadas

    print("Employee {} is done with tasks({}/{}):"
          .format(
              user_request.get('name'),
              len(user_completed_list),
              len(usr_todos_list)))
    for task in user_completed_list:
        print("\t " + task.get('title'))
