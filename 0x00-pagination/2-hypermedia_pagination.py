#!/usr/bin/env python3
""" Implement a get_hyper method that takes the same arguments
    (and defaults) as get_page and returns a dictionary
    containing the following key-value pairs

    page_size: the length of the returned dataset page
    page: the current page number
    data: the dataset page (equivalent to return from previous task)
    next_page: number of the next page, None if no next page
    prev_page: number of the previous page, None if no previous page
    total_pages: the total number of pages in the dataset as an integer
"""
import csv
import math
from typing import List, Dict
import math


def index_range(page: int, page_size: int) -> tuple:
    """ Index Range Function """
    return (((page - 1) * page_size, page * page_size))


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """ Get Page Function """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        indexes = index_range(page, page_size)
        dataset = self.dataset()
        dataset_len = len(dataset)

        if indexes[1] > dataset_len:
            return ([])

        return (dataset[indexes[0]:indexes[1]])

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """ Get Hyper Function """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        indexes = index_range(page, page_size)
        dataset = self.dataset()
        dataset_len = len(dataset)
        data = self.get_page(page, page_size)
        next_page = None if (indexes[1] > dataset_len) else (page + 1)
        prev_page = (page - 1) if page > 1 else None

        result = {
                    'page_size': len(data),
                    'page': page,
                    'data': data,
                    'next_page': next_page,
                    'prev_page': prev_page,
                    'total_pages': math.ceil(dataset_len / page_size)
                }

        return (result)
