#!/usr/bin/python3
""" Req reddit api function that queries the Reddit API and returns
the number of subscribers"""


def number_of_subscribers(subreddit):
    """
    Queries the reddit api for a given subreddit. If an invalid subreddit
    is given, the function should return 0.
    """
    import requests

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'User-Agent': 'python:myredditapp:v1.0.0 (by /u/zakaria_H/)'}
    response = requests.get(url, headers=headers, allow_redirections=False)
    data = response.json()

    if response.status_code >= 300:
        return 0
    else:
        return data['data']['subscribers']
