#!/usr/bin/python3

import requests
import requests

def count_words(subreddit, word_list, after=None, counts=None):
    if counts is None:
        counts = {}

    if not subreddit:
        return

    url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=100'
    if after:
        url += f'&after={after}'

    headers = {'User-Agent': 'Mozilla/5.0'}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()['data']['children']

        for post in data:
            title = post['data']['title'].lower()
            for keyword in word_list:
                keyword_count = title.count(f' {keyword.lower()} ')
                counts[keyword] = counts.get(keyword, 0) + keyword_count

        new_after = response.json()['data']['after']
        if new_after:
            count_words(subreddit, word_list, new_after, counts)
        else:
            print_results(counts)
    except requests.exceptions.RequestException as e:
        print(f'Error fetching data for subreddit {subreddit}: {e}')

def print_results(counts):
    sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
    for keyword, count in sorted_counts:
        print(f'{keyword.lower()}: {count}')

# Example usage:
count_words('python', ['python', 'java', 'javascript'])
