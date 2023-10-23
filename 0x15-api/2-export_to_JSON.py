#!/usr/bin/python3

import requests
import json
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: {} <employee_id>".format(sys.argv[0]))
        sys.exit(1)

    employee_id = sys.argv[1]
    base_url = "https://jsonplaceholder.typicode.com"
    user_url = "{}/users/{}".format(base_url, employee_id)
    todos_url = "{}/todos?userId={}".format(base_url, employee_id)

    try:
        user_response = requests.get(user_url, verify=False)
        todos_response = requests.get(todos_url, verify=False)
        user_data = user_response.json()
        todos_data = todos_response.json()

        # Create a JSON file with the user's ID as the file name
        json_filename = "{}.json".format(user_data['id'])

        user_tasks = []
        for todo in todos_data:
            user_task = {
                "task": todo['title'],
                "completed": todo['completed'],
                "username": user_data['username']
            }
            user_tasks.append(user_task)

        user_json_data = {user_data['id']: user_tasks}

        with open(json_filename, 'w') as json_file:
            json.dump(user_json_data, json_file, indent=4)

        print("JSON data exported to {}".format(json_filename))

    except requests.exceptions.RequestException as e:
        print("An error occurred:", e)
