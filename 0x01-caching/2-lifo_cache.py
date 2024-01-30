#!/usr/bin/env python3
""" Class LIFOCache that inherits from BaseCaching and is a caching system
"""
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """ FIFO Cache Class """
    def __init__(self):
        super().__init__()
        self.max_items = BaseCaching.MAX_ITEMS

    def put(self, key, item):
        """  Assign to the dictionary self.cache_data
             the item value for the key key
        """
        if key and item:
            number_of_items = 0

            for i in self.cache_data:
                number_of_items += 1

            if number_of_items >= self.max_items:
                if key in self.cache_data:
                    self.cache_data[key] = item
                    return

                last_key, last_val = self.cache_data.popitem()
                print(f"DISCARD: {last_key}")

            self.cache_data[key] = item

    def get(self, key):
        """ Return the value in self.cache_data linked to key """
        if key and key in self.cache_data:
            return (self.cache_data[key])

        return (None)
