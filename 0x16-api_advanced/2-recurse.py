#!/usr/bin/python3
""" recursive function that queries the Reddit API
and returns a list containing the titles of all hot articles"""
import requests


def recurse(subreddit, hot_list=[]):
    """Return hot articles for a given subreddit"""
    return recurse_util(
        subreddit=subreddit, hot_list=hot_list, after=None
    )


def recurse_util(subreddit, hot_list=[], after=None):
    """An util for the recurse function"""
    if not hot_list:
        hot_list = []
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    params = {"limit": 100, "after": after}
    response = requests.get(
        url,
        headers={"User-agent": "MyRedditBot/1.0 (Hamza)"},
        params=params,
    )
    if response.status_code == 200:
        data = response.json()
        posts = data.get("data").get("children")
        for post in posts:
            hot_list.append(post.get("data").get("title"))
        after = data.get("data").get("after")
        if after:
            return recurse_util(subreddit, hot_list, after)
        else:
            return hot_list
    else:
        return None
