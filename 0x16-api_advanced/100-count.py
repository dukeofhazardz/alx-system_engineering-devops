#!/usr/bin/python3
""" A recursive function that queries the Reddit API, parses the title of all
    hot articles, and prints a sorted count of given keywords
    (case-insensitive, delimited by spaces. Javascript should count as
    javascript, but java should not). """

import requests


def count_words(subreddit, word_list, instances={}, after=None, times=0):
    """ A recursive function that queries the Reddit API and prints
        a sorted count of given keywords """
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
            title = h.get('data').get('title').lower().split()
            for word in word_list:
                if word.lower() in title:
                    times = len([t for t in title if t == word.lower()])
                    if instances.get(word) is None:
                        instances[word] = times
                    else:
                        instances[word] += times

        if after is not None:
            if len(instances) == 0:
                print("")
                return
            instances = sorted(instances.items(), key=lambda kv: (-kv[1], kv[0]))
            [print("{}: {}".format(k, v)) for k, v in instances]
        else:
            count_words(subreddit, word_list, instances, after, times)
    except Exception:
        print("")
        return
