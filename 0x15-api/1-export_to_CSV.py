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
        user_response = requests.get(user_url, verify=False)
        todos_response = requests.get(todos_url, verify=False)
        user_data = user_response.json()
        todos_data = todos_response.json()

        # Create a CSV file with the user's ID as the file name
        csv_filename = "{}.csv".format(user_data['id'])

        with open(csv_filename, 'w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            
            # Write the header row
            csv_writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])

            for todo in todos_data:
                csv_writer.writerow([user_data['id'], user_data['username'], todo['completed'], todo['title']])

        print("CSV data exported to {}".format(csv_filename))

    except requests.exceptions.RequestException as e:
        print("An error occurred:", e)
