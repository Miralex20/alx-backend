#!/usr/bin/env python3
"""A module on caching task"""
BaseCaching = __import__("base_caching").BaseCaching


class BasicCache(BaseCaching):
    """ A caching system that inherits from base-caching"""
    def put(self, key, item):
        """ Assign item to a key in a dictionary"""
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """ return the value linked to a key"""
        return self.cache_data.get(key, None)