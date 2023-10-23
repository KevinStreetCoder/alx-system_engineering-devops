#!/usr/bin/python3

import requests
import csv
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
        user_response = requests.get(user_url)
        todos_response = requests.get(todos_url)
        user_data = user_response.json()
        todos_data = todos_response.json()

        # Count the number of completed and total tasks
        total_tasks = len(todos_data)
        completed_tasks = sum(1 for todo in todos_data if todo['completed'])

        user_id = user_data['id']
        username = user_data['username']

        # Create and write data to CSV file
        csv_filename = "{}.csv".format(user_id)
        with open(csv_filename, 'w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
            
            for todo in todos_data:
                csv_writer.writerow([user_id, username, str(todo['completed']), todo['title'])

        print("Data exported to {}.csv".format(user_id))

    except requests.exceptions.RequestException as e:
        print("An error occurred:", e)
