#!/usr/bin/python3
""" A function that queries the Reddit API and returns the number of
    subscribers (not active users, total subscribers) for a given subreddit.
    If an invalid subreddit is given, the function should return 0. """

import requests


def number_of_subscribers(subreddit):
    """ A function that queries the Reddit APIand returns
        the number of subscribers """
    try:
        url = "https://api.reddit.com/r/{}/about".format(subreddit)
        headers = {
            "User-Agent": "linux:0x16.api.advanced:v1.0.0"
            }
        request = requests.get(url, headers=headers, allow_redirects=False)
        '''if request.status_code == 404:
            return (0)'''
        subscribers = request.json().get('data').get('subscribers')
        return subscribers
    except Exception:
        return (0)
