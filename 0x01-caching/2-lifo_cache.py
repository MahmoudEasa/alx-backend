#!/usr/bin/env python3
""" Class LIFOCache that inherits from BaseCaching and is a caching system
"""
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """ FIFO Cache Class """
    def __init__(self):
        super().__init__()
        self.max_items = BaseCaching.MAX_ITEMS
        self.max_items = BaseCaching.MAX_ITEMS
        self.last_put = None
        self.size = 0

    def put(self, key, item):
        """  Assign to the dictionary self.cache_data
             the item value for the key key
        """
        if key and item:
            self.size += 1

            if key in self.cache_data:
                self.cache_data[key] = item
                self.last_put = key
                return

            if self.size > self.max_items:
                self.cache_data.pop(self.last_put)
                print(f"DISCARD: {self.last_put}")

            self.cache_data[key] = item
            self.last_put = key

    def get(self, key):
        """ Return the value in self.cache_data linked to key """
        if key and key in self.cache_data:
            return (self.cache_data[key])

        return (None)
