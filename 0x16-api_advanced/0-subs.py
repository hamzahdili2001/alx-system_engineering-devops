#!/usr/bin/python3
"""
function that queries the Reddit API and
returns the number of subscribers"""
import requests


def number_of_subscribers(subreddit):
    """Return the number of subscribers"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "linux:0-subs:v1.0.0 (by /u/hamzed)"}
    response = requests.get(
        url, headers=headers, allow_redirects=False
    )
    if response.status_code == 404:
        return 0
    return response.json().get("data").get("subscribers")
