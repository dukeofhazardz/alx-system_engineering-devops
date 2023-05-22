#!/usr/bin/python3
""" Python script to export data in the CSV format. """

import json
import requests
import sys


if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com'
    users = requests.get(url + "/users").json()
    todos = requests.get(url + "/todos").json()

    e_dict = {
            "{}".format(user.get('id')): [{
                "task": "{}".format(task.get("title")),
                "completed": "{}".format(task.get("completed")),
                "username": "{}".format(user.get('username'))} for task in
                requests.get(url + "/todos", params={"userId": user.get("id")})
                .json()]
            for user in users}

    jsonf = json.dumps(e_dict)
    with open('todo_all_employees.json', 'w', newline='') as jsonfile:
        jsonfile.write(jsonf)

    jsonfile.close()
