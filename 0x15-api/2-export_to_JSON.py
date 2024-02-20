#!/usr/bin/python3
"""
Python script that, using this REST API,
for a given employee ID, returns information
about his/her TODO list progress.
"""
import json
import requests
import sys

if __name__ == "__main__":
    user_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/users"
    user = requests.get(url + "/{}".format(sys.argv[1])).json()
    todos = requests.get(url + "/{}/todos".format(sys.argv[1])).json()

    with open("{}.json".format(user_id), "w") as jsonfile:
        json.dump(
            {
                user_id: [
                    {
                        "task": todo.get("title"),
                        "completed": todo.get("completed"),
                        "username": user.get("username"),
                    }
                    for todo in todos
                ]
            },
            jsonfile,
        )
