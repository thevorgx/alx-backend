#!/usr/bin/env python3
"""LIFOCache Module"""
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """LIFOCache class inherit from BaseCaching"""
    def put(self, key, item):
        """put item on cache_data dict using LIFO ALGO"""
        if key is not None and item is not None:
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                my_dict = self.cache_data
                del_key, del_value = my_dict.popitem()
                print(f"DISCARD: {del_key}")
            self.cache_data.update({key: item})

    def get(self, key):
        """get key from cache_data dict"""
        if key is None or key not in self.cache_data:
            return (None)
        the_key = self.cache_data.get(key)
        return (the_key)
