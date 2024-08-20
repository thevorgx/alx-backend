#!/usr/bin/env python3
"""FIFOCache Module"""
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """FIFOCache class inherit from BaseCaching"""
    def put(self, key, item):
        """put item on cache_data dict using FIFO ALGO"""
        if key is not None and item is not None:
            self.cache_data.update({key: item})
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                my_dict = self.cache_data
                del_key = next(iter(my_dict))
                my_dict.pop(del_key)
                print(f"DISCARD: {del_key}")

    def get(self, key):
        """get key from cache_data dict"""
        if key is None or key not in self.cache_data:
            return (None)
        the_key = self.cache_data.get(key)
        return (the_key)
