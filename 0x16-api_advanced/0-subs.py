#!/usr/bin/python3
"""
queries the Reddit API and returns the number of subscribers(not active
users, total subscribers) for a given subreddit. if an invalid subreddit
is given, the function should return 0.
"""

import requests
import sys


def number_of_subscribers(subreddit):
    """Queries to Reddit API"""
    u_agent = "MyRedditBot/1.0 (Hamza)"

    headers = {"User-Agent": u_agent}

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    res = requests.get(url, headers=headers, allow_redirects=False)
    if res.status_code != 200:
        return 0
    dic = res.json()
    if "data" not in dic:
        return 0
    if "subscribers" not in dic.get("data"):
        return 0
    return res.json()["data"]["subscribers"]
