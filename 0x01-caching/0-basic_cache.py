#!/usr/bin/env python3
"""BasicCache Module"""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """BasicCache class inherit from BaseCaching"""
    def put(self, key, item):
        """put item on cache_data dict"""
        if key is not None and item is not None:
            self.cache_data.update({key: item})

    def get(self, key):
        """get key from cache_data dict"""
        if key is None or key not in self.cache_data:
            return (None)
        the_key = self.cache_data.get(key)
        return (the_key)
