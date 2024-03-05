#!/usr/bin/python3
"""
function that queries the Reddit API and
returns the number of subscribers"""
import requests


def number_of_subscribers(subreddit):
    """function that queries the Reddit API"""

    URL = "https://www.reddit.com/r/{}/about.json".format(subreddit)

    headers = {"User-Agent": "Reddit-Agent"}
    response = requests.get(
        URL, headers=headers, allow_redirects=False
    )

    if response.status_code == 200:
        RES = response.json()
        return RES["data"]["subscribers"]
    else:
        return 0
