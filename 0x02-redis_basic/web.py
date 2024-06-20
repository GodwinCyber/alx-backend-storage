#!/usr/bin/env python3
"""Module 5"""

import requests
import redis
import time

redis_client = redis.Redis(host='localhost', port=6379, db=0)

def get_get(url: str) -> str:
    """Fetch HTML content of a URL and cache the result with expiration"""
    cache_key = "count{}".format(url)
    cached_html = redis_client.get(cache_key)
    if cached_html:
        print("Returning cached content for {}".format(url))
        redis_client.incr("{}:count".format(cache_key))
        return cached_html.decode('utf-8')

    response = requests.get(url)
    html = response.text
    redis_client.setex(cache_key, 10, html_content)
    redis_client.set("{}:count".format(cache_key), 1, ex=10)
    return html_content


if __name__ =='___main__':
    url = "http://slowwly.robertomurray.co.uk"
    print("Fetching content for {}".format(url))
    print(get_page(url))
    time.sleep(5)
    print("Fetching content again for {}".format(url))
    print(get_page(url))
