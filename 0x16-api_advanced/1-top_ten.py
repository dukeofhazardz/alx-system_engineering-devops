#!/usr/bin/python3
""" A function that queries the Reddit API and prints the titles
    of the first 10 hot posts listed for a given subreddit. """

import requests


def top_ten(subreddit):
    """ A function that queries the Reddit API and returns
        prints the titles of the first 10 hot posts """
    try:
        url = "https://api.reddit.com/r/{}/hot".format(subreddit)
        headers = {
            "User-Agent": "linux:0x16.api.advanced:v1.0.0"
            }
        params = {
            "limit": 10
            }
        request = requests.get(url, headers=headers,
                               params=params, allow_redirects=False)
        hot = request.json().get('data')
        [print(h.get('data').get('title')) for h in hot.get('children')]
    except Exception:
        print(None)
