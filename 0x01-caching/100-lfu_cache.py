#!/usr/bin/env python3
""" class LFUCache that inherits from BaseCaching and is a caching system
"""
from collections import deque
BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """ LFU Cache Class """
    def __init__(self):
        super().__init__()
        self.max_items = BaseCaching.MAX_ITEMS
        self.repeated_items = {}
        self.size = 0

    def put(self, key, item):
        """  Assign to the dictionary self.cache_data
             the item value for the key key
        """
        if key and item:
            self.size += 1

            if key in self.cache_data:
                self.cache_data[key] = item
                self.repeated_items[key] += 1
                return

            if self.size > self.max_items:
                r = self.repeated_items
                min_repeate = min(r, key=lambda k: r[k])
                self.cache_data.pop(min_repeate)
                r.pop(min_repeate)
                print(f"DISCARD: {min_repeate}")

            self.cache_data[key] = item
            self.repeated_items[key] = 0

    def get(self, key):
        """ Return the value in self.cache_data linked to key """
        if key and key in self.cache_data:
            self.repeated_items[key] += 1
            return (self.cache_data[key])

        return (None)
