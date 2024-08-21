#!/usr/bin/env python3
"""FIFOCache Module"""
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """FIFOCache class inherit from BaseCaching"""

    def __init__(self):
        """Initialize the cache"""
        super().__init__()

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
        """Get an item by key"""
        if key is not None:
            return (self.cache_data.get(key))
        else:
            return (None)
