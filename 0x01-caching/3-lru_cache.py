#!/usr/bin/env python3
"""LRUCache Module"""
BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """LRUCache class that inherits from BaseCaching"""

    def __init__(self):
        """Initialize the cache"""
        super().__init__()
        self.last_key = None
        self.cache_keys = []

    def put(self, key, item):
        """Put item into cache with LRU behavior"""
        if key is not None and item is not None:
            if key in self.cache_data:
                self.cache_keys.remove(key)
            elif len(self.cache_data) == BaseCaching.MAX_ITEMS:
                lru = self.cache_keys.pop()
                del self.cache_data[lru]
                print(f"DISCARD: {lru}")

            self.cache_keys.insert(0, key)
            self.cache_data.update({key: item})

    def get(self, key):
        """Get an item by key"""
        if key is not None:
            return (self.cache_data.get(key))
        else:
            return (None)
