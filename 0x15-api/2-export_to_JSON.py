#!/usr/bin/python3
""" Python script to export data in the CSV format. """

import json
import requests
import sys


if __name__ == "__main__":
    id = sys.argv[1]
    url = 'https://jsonplaceholder.typicode.com'
    user = requests.get(url + "/users/{}".format(id)).json()
    todos = requests.get(url + "/todos", params={'userId': id}).json()
    username = user.get('username')

    e_dict = {
            "{}".format(id): [{
                "task": "{}".format(task.get("title")),
                "completed": "{}".format(task.get("completed")),
                "username": "{}".format(username)} for task in todos]
    }

    with open('{}.json'.format(str(id)), 'w', newline='') as jsonfile:
        json.dump(e_dict, jsonf)

    jsonfile.close()
