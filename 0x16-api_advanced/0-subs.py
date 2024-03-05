#!/usr/bin/python3
import requests
""" Req reddit api """


def number_of_subscribers(subreddit):
    """ Queries the reddit api """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'My-User-Agent'}

    try:
        response = requests.get(url, headers=headers)
        data = response.json()
        if 'data' in data and 'subscribers' in data['data']:
            return data['data']['subscribers']
        else:
            return 0
    except Exception as e:
        print("Error:", e)
        return 0
