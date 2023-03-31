#!/usr/bin/python3
"""
This script uses a REST API to get information about an employee's
TODO list progress given an employee ID.
"""
import requests
import sys


def main(employee_id):
    url = "https://jsonplaceholder.typicode.com/"
    user_url = f"{url}users/{employee_id}"
    todo_url = f"{url}users/{employee_id}/todos"

    user_response = requests.get(user_url)
    todo_response = requests.get(todo_url)

    if user_response.status_code != 200 or todo_response.status_code != 200:
        print("Error: Unable to fetch data from the API")
        return

    user_data = user_response.json()
    todo_data = todo_response.json()

    total_tasks = len(todo_data)
    done_tasks = [task for task in todo_data if task["completed"]]
    done_task_count = len(done_tasks)

    print(f'Employee {user_data["name"]} is done with tasks({done_task_count}/{total_tasks}):')
    for task in done_tasks:
        print(f'\t {task["title"]}')


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: ./0-gather_data_from_an_API.py <employee_id>")
    else:
        try:
            employee_id = int(sys.argv[1])
            main(employee_id)
        except ValueError:
            print("Error: Employee ID must be an integer")

