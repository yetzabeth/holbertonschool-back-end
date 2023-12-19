#!/usr/bin/python3
import json
import requests
from sys import argv


if __name__ == '__main__':
    todo = requests.get('https://jsonplaceholder.typicode.com/todos').json()
    user = requests.get('https://jsonplaceholder.typicode.com/users').json()

    name = ""
    for elements in user:
        if elements.get('id') == int(argv[1]):
            name = elements.get('name')
            break
    else:
        print("Error: User with ID {} not found.".format(argv[1]))
        exit(1)

    task_list = [task for task in todo if task.get('userId') == int(argv[1])]
    completed_tasks_count = len([task for task in task_list if task.get('completed')])

    print('Employee {} is done with tasks({}/{}):'.
          format(name, completed_tasks_count, len(task_list)))

    for task in task_list:
        if task.get('completed'):
            print('\t{}'.format(task.get('title')))
