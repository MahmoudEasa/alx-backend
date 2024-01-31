#!/usr/bin/env python3
""" Class LRUCache that inherits from BaseCaching and is a caching system
"""
from collections import deque
BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """ LRU Cache Class """
    def __init__(self):
        super().__init__()
        self.max_items = BaseCaching.MAX_ITEMS
        self.queue = deque()
        self.size = 0

    def put(self, key, item):
        """  Assign to the dictionary self.cache_data
             the item value for the key key
        """
        if key and item:
            self.size += 1

            if key in self.cache_data:
                self.cache_data[key] = item
                self.queue.remove(key)
                self.queue.append(key)
                return

            if self.size > self.max_items:
                old = self.queue.popleft()
                self.cache_data.pop(old)
                print(f"DISCARD: {old}")

            self.cache_data[key] = item
            self.queue.append(key)

    def get(self, key):
        """ Return the value in self.cache_data linked to key """
        if key and key in self.cache_data:
            self.queue.remove(key)
            self.queue.append(key)
            return (self.cache_data[key])

        return (None)
