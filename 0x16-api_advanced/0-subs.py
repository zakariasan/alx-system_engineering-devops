#!/usr/bin/python3
""" Req reddit api """


def number_of_subscribers(subreddit):
    """ Queries the reddit api """
    import requests

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'User-Agent': 'CustomClient/1.0'}
    response = requests.get(url, headers=headers, allow_redirections=False)
    data = response.json()

    if response.status_code >= 300:
        return 0
    else:
        return data['data']['subscribers']
