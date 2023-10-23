#!/usr/bin/python3

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: {} <employee_id>".format(sys.argv[0]))
        sys.exit(1)

    employee_id = sys.argv[1]
    base_url = "https://jsonplaceholder.typicode.com"
    user_url = f"{base_url}/users/{employee_id}"
    todos_url = f"{base_url}/todos?userId={employee_id}"

    try:
        user_response = requests.get(user_url)
        todos_response = requests.get(todos_url)
        user_data = user_response.json()
        todos_data = todos_response.json()

        # Count the number of completed and total tasks
        total_tasks = len(todos_data)
        completed_tasks = sum(1 for todo in todos_data if todo['completed'])

        print(f"Employee {user_data['name']} is done with tasks({completed_tasks}/{total_tasks}):")

        for todo in todos_data:
            if todo['completed']:
                print("\t " + todo['title'])

    except requests.exceptions.RequestException as e:
        print("An error occurred:", e)
