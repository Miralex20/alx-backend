#!/usr/bin/env python3
"""A caching system task"""
BaseCaching = __import__('base_caching').BaseCaching
OrderedDict = __import__("collections").OrderedDict



class FIFOCache(BaseCaching):
    """A first in first out caching system"""
    def __init__(self):
        """ Init the cache"""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """ Assigns item to a key in the cache"""
        if key is None or item is None:
            return
        if key in self.cache_data:
            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                lastKey, _ = self.cache_data.popitem(True)
                print("DISCARD:", lastKey)
        self.cache_data[key] = item
        self.cache_data.move_to_end(key, last=True)

    def get(self, key):
        """Returns item at the given key"""
        return self.cache_data.get(key, None)