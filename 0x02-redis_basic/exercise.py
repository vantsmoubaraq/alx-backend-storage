#!/usr/bin/env python3

"""Module implements cache class"""

import redis
import uuid
from typing import Union, Callable, Optional


class Cache:
    """connects to redis"""
    def __init__(self):
        self._redis = redis.Redis(host="localhost", port=6379)
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """stores data"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None
            ) -> Union[str, int, bytes, float]:
        """gets data"""
        value = self._redis.get(key)
        try:
            if value and fn:
                value = fn(value)
        except ValueError:
            pass
        return value

    @staticmethod
    def get_str(key: str) -> str:
        """converts into a string"""
        data = self._redis.get(key)
        return data.decode("utf-8")

    @staticmethod
    def get_int(key: str) -> int:
        """converts into an integer"""
        data = self._redis.get(key)
        try:
            data = int(data.decode("utf-8"))
        except Exception:
            data = 0
        return data
