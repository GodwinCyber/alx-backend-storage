#!/usr/bin/env python3
"""Module 1"""

import redis
import uuid
from typing import Union, Any, Callable
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """count how many times methods of the Cache class are called.
        count_calls decorator that takes a single method Callable
        argument and returns a Callable.
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs) -> Any:
        """wrapper function that count method
            key, use the qualified name of method using
            the __qualname__ dunder method.
        """
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """Decorator to store the input and output for a method"""
    @wraps(method)
    def wrapper(self, *args, **kwargs) -> Any:
        """wrapper function that store input and output"""
        output = method(self, *args, **kwargs)
        key = method.__qualname__
        input_key = "{}:inputs".format(key)
        output_key = "{}:outputs".format(key)

        self._redis.rpush(input_key, str(args))
        self._redis.rpush(output_key, str(output))
        return output
    return wrapper


class Cache:
    """Create a Cache class. In the __init__ method, store an
       instance of the Redis client as a private variable named _redis
       (using redis.Redis()) and flush the instance using flushdb.
    """
    def __init__(self):
        """Initializing cache instance"""
        self._redis = redis.Redis()
        self._redis.flushdb(True)

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """create  store method that take a data argunment and return a string
            the moment you generate random key using uuid, store the input data
            in Redis using the random key and return a key type-annotate store
            correctly; Remember that data can be str, byte, int, of flot
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Callable = None) -> Union[
                             str, bytes, int, float, None]:
        """create get method that takes a key and an
            optional [Callable] fn argument The Callable
            will be used to convert data back to the desired format
        Arg:
            key (str): The key to retrieve data from Redis
            fn (Optional[Callable]): An optional function
            to convert data back to the desired format
        Returns:
            Union[str, bytes, int, float, None]: The retrieved
            data or None if the key does not exist in Redis
        """
        data = self._redis.get(key)
        if data is None:
            return None
        if fn is not None:
            return fn(data)
        return data

    def get_str(self, key: str) -> str:
        """Retrieve data as a stirng from Redis
        Arg:
            key: The key of the data to retrieve
        Return:
            The retrieve data as a string or None is data does not exit
        """
        return self.get(key, lambda x: x.decode('utf-8'))

    def get_int(self, key: str) -> int:
        """Retrieve data as an integer from Redis
        Args:
            key: The key of the data to retrieve
        Return:
            The retrieve data as an integer or None if it does not exist
        """
        return self.get(key, lambda x: int(x))

    def replay(method: Callable) -> None:
        """Display the history of calls of a particular function."""
        if fn is None or not hasattr(fn, '__self__'):
            return
        redis_store = getattr(fn.__self__, '_redis', None)
        if not isinstance(redis_store, redis.Redis):
            return
        fxn_name = fn.__qualname__
        in_key = '{}:inputs'.format(fxn_name)
        out_key = '{}:outputs'.format(fxn_name)
        fxn_call_count = 0

        inputs = cache._redis.lrange((in_key), 0, -1)
        outputs = cache._redis.lrange((out_key), 0, -1)

        if inputs and outputs:
            fxn_call_count = min(len(inputs), len(outputs))

        print("{} was called {} times:".format(key, len(inputs)))
        for input_data, output_data in zip(inputs, outputs):
            input_data = input_data.decode('utf-8')
            output_data = output_data.decode('utf-8')
            print("{}(*{}) -> {}".format(input_data, output_data))
