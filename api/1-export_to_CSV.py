#!/usr/bin/python3
"""
Python script that extends Task 0 to export employee TODO data in CSV format.
"""

csv_file = __import__("csv")
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

        filename = f"{emp_id}.csv"
        with open(filename, mode="w", newline="", encoding="utf-8") as f:
            writer = csv_file.writer(f, quoting=csv_file.QUOTE_ALL)
            for task in todos_res:
                writer.writerow(
                    [
                        str(emp_id),
                        str(username),
                        str(task.get("completed")),
                        str(task.get("title")),
                    ]
                )