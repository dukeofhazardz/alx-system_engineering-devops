#!/usr/bin/python3
""" A recursive function that queries the Reddit API and returns a list
    containing the titles of all hot articles for a given subreddit.
    If no results are found for the given subreddit, the
    function should return None. """

import requests


def recurse(subreddit, hot_list=[], after=None, times=0):
    """A recursive function that queries the Reddit API and returns a list"""
    try:
        url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
        headers = {
            "User-Agent": "linux:0x16.api.advanced:v1.0.0"
            }
        params = {
                "limit": 100,
                "times": times,
                "after": after
            }
        request = requests.get(url, headers=headers,
                               params=params, allow_redirects=False)
        hot = request.json().get('data')
        after = hot.get('after')
        times += hot.get('dist')
        for h in hot.get('children'):
            hot_list.append(h.get('data').get('title'))
        if after is not None:
            return recurse(subreddit, hot_list, after, times)
        else:
            return hot_list
    except Exception:
        print(None)
