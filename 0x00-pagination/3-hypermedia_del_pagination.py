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
        """get data about a specific index with pagination details."""
        assert index is None or (isinstance(index, int) and index >= 0)
        assert isinstance(page_size, int) and page_size > 0

        dataset = self.indexed_dataset()
        max_index = len(dataset) - 1

        if index is not None:
            assert 0 <= index <= max_index

        current_index = index if index is not None else 0
        end_index = current_index + page_size

        data = []
        while len(data) < page_size and current_index <= max_index:
            if current_index in dataset:
                data.append(dataset[current_index])
            current_index += 1

        next_index = end_index if len(data) == page_size else current_index

        return {
            "index": index,
            "data": data,
            "page_size": page_size,
            "next_index": next_index
        }
