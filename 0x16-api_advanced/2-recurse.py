#!/usr/bin/python3
import requests
""" Req reddit api """


def recurse(subreddit, hot_list=None, after=None):
    """ Queries the reddit api the top 10"""

    if hot_list is None:
        hot_list = []

    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=100"
    headers = {'User-Agent': 'My-User-Agent'}
    params = {'after': after} if after else {}

    try:
        response = requests.get(url, headers=headers, params=params)
        data = response.json()
        if 'data' in data and 'children' in data['data']:
            for post in data['data']['children']:
                hot_list.append(post['data']['title'])

            if data['data']['after'] is not None:
                return recurse(subreddit, hot_list, data['data']['after'])
            else:
                return hot_list
        else:
            return None
    except Exception as e:
        print("Error:", e)
        return None
