#!/usr/bin/python3
""" Req reddit api function that queries the Reddit API and returns
the number of subscribers"""


def number_of_subscribers(subreddit):
    """
    Queries the reddit api for a given subreddit. If an invalid subreddit
    is given, the function should return 0.
    """
    import requests
    res = requests.get("https://www.reddit.com/r/{}/about.json"
                       .format(subreddit),
                       headers={"User-Agent": "My-User-Agent"},
                       allow_redirects=False)
    if res.status_code >= 300:
        return 0
    return res.json().get("data").get("subscribers")
