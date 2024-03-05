#!/usr/bin/python3
"""
queries the Reddit API and returns the number of subscribers(not active
users, total subscribers) for a given subreddit. if an invalid subreddit
is given, the function should return 0.
"""
import requests


def get_subreddit_data(subreddit):
    """function that queries the Reddit API"""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {
        "User-Agent": "Custom User Agent"
    }  # Reddit API requires a User-Agent header
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        return None


def number_of_subscribers(subreddit):
    """function that queries the Reddit API"""
    data = get_subreddit_data(subreddit)
    if data and "data" in data and "subscribers" in data["data"]:
        return data["data"]["subscribers"]
    else:
        return 0
