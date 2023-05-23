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

    with open('{}.json'.format(str(id)), 'w') as jsonfile:
        json.dump({id: [{
                "task": "{}".format(task.get("title")),
                "completed": "{}".format(task.get("completed")),
                "username": username} for task in todos]
            }, jsonfile)

    jsonfile.close()
