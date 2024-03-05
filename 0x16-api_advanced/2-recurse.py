#!/usr/bin/python3
""" recursive function that queries the Reddit API
and returns a list containing the titles of all hot articles"""
import requests


def recurse(subreddit, hot_list=None, after=None):
    """Recursively fetches hot articles from a subreddit."""

    if hot_list is None:
        hot_list = []

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0"}

    params = (
        {"limit": 100, "after": after} if after else {"limit": 100}
    )

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()
        if (
            "data" in data
            and "children" in data["data"]
            and len(data["data"]["children"]) > 0
        ):
            for child in data["data"]["children"]:
                hot_list.append(child["data"]["title"])
            if data["data"]["after"]:
                return recurse(
                    subreddit, hot_list, data["data"]["after"]
                )
            else:
                return hot_list
        else:
            return None
    elif response.status_code == 404:
        raise Expception
    else:
        return Expception
