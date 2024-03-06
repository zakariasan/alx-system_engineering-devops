#!/usr/bin/python3
"""
playing with queering Queries the Reddit API and returns the count of words in
"""
import requests


def count_words(subreddit, word_list, word_count={}, after=None):
    """
    Queries the Reddit API and returns the count of words in
    word_list in the titles of all the hot posts of the subreddit.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    params = {'after': after}
    headers = {'User-Agent': 'My-User-Agent'}

    try:
        response = requests.get(url, params=params, headers=headers,
                                allow_redirects=False)
        response.raise_for_status()
        data = response.json().get('data', {})
        children = data.get('children', [])
        if not children:
            return None
        if not word_count:
            word_count = {word.lower(): 0 for word in set(word_list)}
        for post in children:
            title = post['data']['title']
            words = title.lower().split()
            for word in word_count:
                word_count[word] += words.count(word)
        after = data.get('after')
        if after:
            return count_words(subreddit, word_list, word_count, after)
        else:
            sorted_counts = sorted(word_count.items(),
                                   key=lambda kv: (-kv[1], kv[0]))
            for word, count in sorted_counts:
                if count != 0:
                    print(f"{word}: {count}")
            return None

    except requests.RequestException as e:
        print("Error:", e)
        return None
