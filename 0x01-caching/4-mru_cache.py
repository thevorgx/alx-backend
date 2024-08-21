#!/usr/bin/env python3
"""LRUCache Module"""
BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """MRUCache class that inherits from BaseCaching"""

    def __init__(self):
        """Initialize the cache"""
        super().__init__()
        self.cache_keys = []

    def put(self, key, item):
        """Put item into cache with MRU behavior"""
        if key is not None and item is not None:
            if key in self.cache_data:
                self.cache_keys.remove(key)
            elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                mru = self.cache_keys.pop()
                del self.cache_data[mru]
                print(f"DISCARD: {mru}")

            self.cache_keys.append(key)
            self.cache_data.update({key: item})

    def get(self, key):
        """Get an item by key"""
        if key is not None and key in self.cache_data:
            self.cache_keys.remove(key)
            self.cache_keys.append(key)
            return (self.cache_data[key])
        else:
            return (None)
