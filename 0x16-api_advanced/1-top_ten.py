#!/usr/bin/python3
"""function that queries the Reddit API and prints the titles
of the first 10 hot posts listed for a given subreddit."""
import requests


def top_ten(subreddit):
    """prints the titles of the 10 hottest posts"""
    URL = "https://www.reddit.com/r/{}/hot.json?limit=10".format(
        subreddit
    )
    headers = {"User-Agent": "Reddit-Agent"}
    response = requests.get(
        URL, headers=headers, allow_redirects=False
    )
    if response.status_code >= 300:
        print("None")
    Js = response.json()
    [print(post["data"]["title"]) for post in Js["data"]["children"]]
