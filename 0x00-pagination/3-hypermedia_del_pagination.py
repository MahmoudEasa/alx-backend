#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """ Get Hyper Index Function """
        dataset_dict = self.indexed_dataset()
        dataset_list = list(dataset_dict.keys())
        data_len = dataset_list[-1]

        assert isinstance(index, int) and index <= data_len and index >= 0
        assert isinstance(page_size, int) and page_size > 0

        new_index = index
        if new_index not in dataset_dict:
            for i in range(new_index, data_len + 1):
                if i in dataset_dict:
                    new_index = i
                    break

        data = [dataset_dict[i] for i in range(
                                                new_index,
                                                (new_index + page_size)
                                               )]

        result = {
                    "index": index,
                    "next_index": (new_index + page_size),
                    "page_size": page_size,
                    "data": data
                }

        return (result)
