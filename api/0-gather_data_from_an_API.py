#!/usr/bin/python3
"""
Script that, using a REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""

import requests
from sys import argv


if __name__ == "__main__":
    """Script for task0"""
    if len(argv) != 2 or not argv[1].isdigit():
        print("Usage: {} EMPLOYEE_ID".format(argv[0]))
    else:
        employee_id = int(argv[1])
        base_url = "https://jsonplaceholder.typicode.com"

        # Fetch user info
        user_info_url = "{}/users/{}".format(base_url, employee_id)
        user_info = requests.get(user_info_url).json()

        # Fetch TODO list
        todo_url = "{}/todos?userId={}".format(base_url, employee_id)
        todo_list = requests.get(todo_url).json()

        # Filter completed tasks
        completed_tasks = [task for task in todo_list if task['completed']]

        # Print results
        print("Employee {} is done with tasks({}/{}):".format(
            user_info['name'], len(completed_tasks), len(todo_list)))

        for task in completed_tasks:
            print("\t {}".format(task['title']))
