#!/usr/bin/python3
""" Req reddit api """
import requests


def number_of_subscribers(subreddit):
    """ Queries the reddit api """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'My-User-Agent'}
    response = requests.get(url, headers=headers, allow_redirections=False)
    data = response.json()
    if 'data' in data and 'subscribers' in data['data']:
        return data['data']['subscribers']
    else:
        return 0
