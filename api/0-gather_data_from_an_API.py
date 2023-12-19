#!/usr/bin/python3
"""
Gather data from an API
"""
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

    list = []
    for dict in todo:
        if dict.get('userId') == int(argv[1]):
            list.append(dict)

    true_elements = []
    for completed in list:
        if completed.get('completed'):
            true_elements.append(completed)

    print('Employee {} is done with tasks({}/{}):'.
          format(name, len(true_elements), len(list)))
    for task in true_elements:
        print('\t {}'.format(task.get('title')))
