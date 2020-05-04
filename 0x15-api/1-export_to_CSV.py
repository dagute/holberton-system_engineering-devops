#!/usr/bin/python3
"""Export to CSV"""
import requests
from sys import argv
import csv


def export_csv(data, path):
    """ export data in the CSV format"""
    with open(path, "w", newline="") as f:
        writer = csv.writer(f, delimiter=',', quoting=csv.QUOTE_ALL)
        for x in data:
            writer.writerow(x)

if __name__ == "__main__":
    """returns information about his/her TODO list progress"""
    url1 = requests.get("https://jsonplaceholder.typicode.com/todos")
    url2 = requests.get("https://jsonplaceholder.typicode.com/users")
    to_do = url1.json()
    users = url2.json()

    name = ""
    completed = ""
    emp_id = ""
    tasks = []

    for user in users:
        if user["id"] == int(argv[1]):
            name = user["username"]

    for arg in to_do:
        if arg["userId"] == int(argv[1]):
            if arg["completed"] is True:
                completed = 'True'
            else:
                completed = 'False'
            row = '{},{},{},{}'.format(argv[1], name,
                                       completed,
                                       arg["title"])
            tasks.append(row.split(","))

path = str(argv[1]) + ".csv"
export_csv(tasks, path)
