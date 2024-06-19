#!/usr/bin/env python3
"""Module 1"""

import redis
import uuid
from typing import Union


class Cache:
    """Create a Cache class. In the __init__ method, store an
       instance of the Redis client as a private variable named _redis
       (using redis.Redis()) and flush the instance using flushdb.
    """
    def __init__(self):
        """Initializing cache instance"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """create  store method that take a data argunment and return a string
            the moment you generate random key using uuid, store the input data
            in Redis using the random key and return a key type-annotate store
            correctly; Remember that data can be str, byte, int, of flot
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
