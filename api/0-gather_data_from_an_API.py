#!/usr/bin/python3
"""
Gather data from an API
"""

import requests
from sys import argv


def get_todo_list_progress(employee_id):
    """
    Retrieve and display TODO list progress for a given employee ID.

    Args:
        employee_id (int): The ID of the employee.

    Returns:
        None
    """
    # Make a GET request to fetch the TODO list and user data from the JSONPlaceholder API
    todo_url = f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}'
    user_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}'

    todo_response = requests.get(todo_url)
    user_response = requests.get(user_url)

    # Check if the API requests were successful
    if todo_response.status_code != 200 or user_response.status_code != 200:
        print("Error: Unable to fetch data from the API.")
        return

    todo = todo_response.json()
    user = user_response.json()

    # Extract user information
    employee_name = user.get('name')

    # Calculate TODO list progress
    total_tasks = len(todo)
    completed_tasks = sum(1 for task in todo if task.get('completed'))

    # Print the TODO list progress
    print(f'Employee {employee_name} is done with tasks({completed_tasks}/{total_tasks}):')

    # Print the titles of completed tasks with indentation
    for task in todo:
        if task.get('completed'):
            print(f'    {task.get("title")}')


if __name__ == '__main__':
    # Check if the correct number of command-line arguments is provided
    if len(argv) != 2:
        print("Usage: python3 script_name.py <employee_id>")
    else:
        # Call the function with the provided employee ID
        get_todo_list_progress(int(argv[1]))
