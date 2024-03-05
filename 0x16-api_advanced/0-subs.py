#!/usr/bin/python3
""" Req reddit api """


def number_of_subscribers(subreddit):
    """ Queries the reddit api """
    import requests

    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'My-User-Agent'}
    response = requests.get(url, headers=headers, allow_redirections=False)
    data = response.json()

    if response.status_code >= 300:
        return 0
    else:
        return data['data']['subscribers']
