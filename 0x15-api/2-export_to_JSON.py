#!/usr/bin/python3
"""Export to JSON"""
import requests
from sys import argv
import json

if __name__ == "__main__":
    """export to JSON"""
    my_list = []
    employee = {}

    url = "https://jsonplaceholder.typicode.com/"
    tasks = requests.get(url + "todos?userId=" + argv[1])
    tasks = tasks.json()
    emp = requests.get(url + "users/" + argv[1])
    emp = emp.json()
    USER_ID = emp.get("id")
    username = emp.get("username")

    for arg in tasks:
        my_dict = {}
        my_dict["completed"] = arg["completed"]
        my_dict["task"] = arg["title"]
        my_dict["username"] = username
        my_list.append(my_dict)

    employee[argv[1]] = my_list
    file = argv[1] + ".json"
    with open(file, 'w', encoding="utf-8") as f:
        d = json.dumps(employee)
        f.write(d)
