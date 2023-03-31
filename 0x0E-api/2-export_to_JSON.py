#!/usr/bin/python3
"""doc"""
import json
import requests
import sys
import urllib


def get_employee_data(employee_id):
    base_url = "https://jsonplaceholder.typicode.com"

    user_response = requests.get("{}/users/{}".format(base_url, employee_id))
    user_data = user_response.json()

    if 'name' not in user_data:
        print("Invalid employee ID")
        return None, None

    todos_response = requests.get("{}/users/{}/todos"
                                  .format(base_url, employee_id))
    todos_data = todos_response.json()

    return user_data, todos_data


def export_to_json(employee_id, user_data, todos_data):
    file_name = "{}.json".format(employee_id)

    task_data = []
    for task in todos_data:
        task_data.append({
            "task": task["title"],
            "completed": task["completed"],
            "username": user_data["username"]
        })

    json_data = {employee_id: task_data}

    with open(file_name, "w") as jsonfile:
        json.dump(json_data, jsonfile)

    print("Data exported to {}".format(file_name))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 2-export_to_JSON.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer")
        sys.exit(1)

    user_data, todos_data = get_employee_data(employee_id)

    if user_data and todos_data:
        export_to_json(employee_id, user_data, todos_data)
