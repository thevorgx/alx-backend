#!/usr/bin/env python3
"""LIFOCache Module"""
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """LIFOCache class that inherits from BaseCaching"""
    
    def __init__(self):
        """Initialize the cache"""
        super().__init__()
        self.last_key = None

    def put(self, key, item):
        """Put item into cache with LIFO behavior"""
        if key is not None and item is not None:
            if len(self.cache_data) == BaseCaching.MAX_ITEMS:
                if self.last_key is not None:
                    print(f"DISCARD: {self.last_key}")
                    del self.cache_data[self.last_key]
            self.cache_data[key] = item
            self.last_key = key

    def get(self, key):
        """Get an item by key"""
        return self.cache_data.get(key) if key is not None else None