#!/usr/bin/python3
""" Python script to export data in the CSV format. """

import csv
import requests
import sys


if __name__ == "__main__":
    id = sys.argv[1]
    url = 'https://jsonplaceholder.typicode.com'
    user = requests.get(url + "/users/{}".format(id)).json()
    todos = requests.get(url + "/todos", params={'userId': id}).json()

    username = user.get('username')

    with open('{}.csv'.format(str(id)), 'w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)

        for task in todos:
            writer.writerow(["{}".format(id), "{}".format(username),
                             "{}".format(task.get("completed")),
                             "{}".format(task.get("title"))])
    file.close()
