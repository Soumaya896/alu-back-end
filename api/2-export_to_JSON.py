#!/usr/bin/python3
"""
Python script that extends Task 0 to export employee TODO data in JSON format.
"""

import json
from sys import argv
import requests


if __name__ == "__main__":
    if len(argv) > 1:
        emp_id = argv[1]
        user_url = f"https://jsonplaceholder.typicode.com/users/{emp_id}"
        todos_url = f"https://jsonplaceholder.typicode.com/todos?userId={emp_id}"

        user_res = requests.get(user_url).json()
        todos_res = requests.get(todos_url).json()

        username = user_res.get("username")

        tasks_list = []
        for task in todos_res:
            tasks_list.append(
                {
                    "task": task.get("title"),
                    "completed": task.get("completed"),
                    "username": username,
                }
            )

        out_data = {str(emp_id): tasks_list}
        filename = f"{emp_id}.json"
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(out_data, f)