#!/usr/bin/python3
"""
 extend your Python script to export data in the CSV format.
"""

import csv
import requests
import sys

if __name__ == "__main__":
    user_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/users"
    user = requests.get(url + "/{}".format(sys.argv[1])).json()
    todos = requests.get(url + "/{}/todos".format(sys.argv[1])).json()
    username = user.get("username")

    with open("{}.csv".format(user_id), "w", newline="") as csfile:
        writer = csv.writer(csfile, quoting=csv.QUOTE_ALL)
        for task in todos:
            writer.writerow(
                [
                    sys.argv[1],
                    username,
                    task.get("completed"),
                    task.get("title"),
                ]
            )
