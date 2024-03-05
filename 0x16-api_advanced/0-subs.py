#!/usr/bin/python3
"""
queries the Reddit API and returns the number of subscribers(not active
users, total subscribers) for a given subreddit. if an invalid subreddit
is given, the function should return 0.
"""
import requests


def number_of_subscribers(subreddit):
    """function that queries the Reddit API"""

    URL = "https://www.reddit.com/r/{}/about.json".format(subreddit)

    headers = {"User-Agent": "0x16.api.advanced"}
    response = requests.get(
        URL, headers=headers, allow_redirects=False
    )

    if response.status_code == 200:
        RES = response.json()
        return RES["data"]["subscribers"]
    else:
        return 0
