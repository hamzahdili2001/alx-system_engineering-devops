#!/usr/bin/python3
"""
Python script that, using this REST API,
for a given employee ID, returns information
about his/her TODO list progress.
"""
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/users"
    user = requests.get(url + "/{}".format(sys.argv[1])).json()
    todos = requests.get(url + "/{}/todos".format(sys.argv[1])).json()
    completed = [
        t.get("title") for t in todos if t.get("completed") is True
    ]
    print(
        "Employee {} is done with tasks({}/{}):".format(
            user.get("name"), len(completed), len(todos)
        )
    )
    [print("\t " + t) for t in completed]
