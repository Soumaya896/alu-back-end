#!/usr/bin/python3
"""
Python script to export all employees' TODO data into a single JSON file.
"""

import json
import requests


if __name__ == "__main__":
    users_url = "https://jsonplaceholder.typicode.com/users"
    todos_url = "https://jsonplaceholder.typicode.com/todos"

    users_res = requests.get(users_url).json()
    todos_res = requests.get(todos_url).json()

    all_data = {}

    for user in users_res:
        user_id = user.get("id")
        username = user.get("username")
        user_tasks = [
            {
                "username": username,
                "task": task.get("title"),
                "completed": task.get("completed"),
            }
            for task in todos_res
            if task.get("userId") == user_id
        ]
        all_data[str(user_id)] = user_tasks

    with open("todo_all_employees.json", "w", encoding="utf-8") as f:
        json.dump(all_data, f)