#!/usr/bin/python3
"""
exports information about an employees TODO list progress
given an employee id to a CSV file named `USER_ID.csv`.
"""
import json
import requests


if __name__ == "__main__":
    """Main function to retrieve and
    export all employees' tasks from
    JSONPlaceholder API.
    This function retrieves data from
    the JSONPlaceholder API for all users' tasks.
    For each user, creates a dictionary where the
    keys correspond to the user ID and the values
    correspond to a list of dictionaries,
    where each dictionary corresponds to
    a task and contains information such as
    the task title, completion status,
    and username. Finally, it writes
    the dictionary to a JSON file
    named 'todo_all_employees.json'.
    """

    url = 'https://jsonplaceholder.typicode.com/users/'
    user_response = requests.get(url)
    user_info = json.loads(user_response.text)

    # create dictionary containing users and their associated tasks
    tasks = {}

    for user in user_info:
        user_id = user['id']

        # create Response object for specific user and that user's tasks
        url = 'https://jsonplaceholder.typicode.com/todos/?userId={}'\
            .format(user_id)
        todo_response = requests.get(url)

        # create Dictionary objects from response objects
        todo_info = json.loads(todo_response.text)

        tasks_list = []

        # create a dictionary for each task and add it to the list of tasks
        for task in todo_info:
            task_dict = {}
            task_dict['username'] = user['username']
            task_dict['task'] = task['title']
            task_dict['completed'] = task['completed']
            tasks_list.append(task_dict)

        # add list of tasks to dictionary for that specific user
        tasks[user_id] = tasks_list

    # write dictionary to a JSON file named 'todo_all_employees.json'
    with open('todo_all_employees.json', 'w', encoding='UTF8',
              newline='') as f:
        f.write(json.dumps(tasks))
