#!/usr/bin/python3
"""
Python script that, using a REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""

import requests
from sys import argv


if __name__ == "__main__":
    if len(argv) > 1:
        emp_id = argv[1]
        base_url = "https://jsonplaceholder.typicode.com"
        user_url = f"{base_url}/users/{emp_id}"
        todos_url = f"{base_url}/todos?userId={emp_id}"

        user_res = requests.get(user_url).json()
        todos_res = requests.get(todos_url).json()

        employee_name = user_res.get("name")
        total_tasks = len(todos_res)
        done_tasks = [t for t in todos_res if t.get("completed") is True]
        number_of_done_tasks = len(done_tasks)

        print(
            f"Employee {employee_name} is done with "
            f"tasks({number_of_done_tasks}/{total_tasks}):"
        )
        for task in done_tasks:
            print(f"\t {task.get('title')}")