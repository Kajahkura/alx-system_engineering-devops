#!/usr/bin/python3

import requests

def count_words(subreddit, word_list, after=None, counts=None):
    if not subreddit:
        return

    if counts is None:
        counts = {}

    url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=100'
    if after:
        url += f'&after={after}'

    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)

    try:
        response.raise_for_status()
        data = response.json()['data']['children']

        for post in data:
            title = post['data']['title'].lower()
            for keyword in word_list:
                matches = title.count(keyword.lower())
                counts[keyword] = counts.get(keyword, 0) + matches

        new_after = response.json()['data']['after']
        if new_after:
            # Recursive call to fetch the next set of posts
            count_words(subreddit, word_list, new_after, counts)
        else:
            # No more posts, print the results
            sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
            for keyword, count in sorted_counts:
                print(f'{keyword}: {count}')
    except requests.exceptions.RequestException as e:
        print(f'Error fetching data for subreddit {subreddit}: {e}')

# Example usage:
count_words('python', ['python', 'java', 'javascript'])
