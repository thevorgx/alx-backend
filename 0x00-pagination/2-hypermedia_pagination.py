#!/usr/bin/env python3
"""Simple helper function"""
import csv
import math
from typing import List


def index_range(page: int, page_size: int) -> tuple:
    """function helper that return a tuple that contain
    start idx and end idx"""
    start_idx = (page-1) * page_size
    end_idx = start_idx + page_size
    idx_range = (start_idx, end_idx)
    return (idx_range)


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
        """return a list of data from database
        step1:
        get star and end idx using index_range function
        step2:
        use this information to get the data using dataset method if
        start idx < len of data_list"""
        assert isinstance(page, int) and isinstance(page_size, int)
        assert page > 0 and page_size > 0

        data_range = index_range(page, page_size)
        start_idx = data_range[0]
        end_idx = data_range[1]

        data_set = self.dataset()

        if start_idx < len(data_set):
            return (data_set[start_idx:end_idx])
        else:
            return([])

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """same stuff as get_page but more data"""
        data_set = self.dataset()
        data = self.get_page(page, page_size)
        total_pages = math.ceil(len(data_set) / page_size)
        next_page = page + 1 if page < total_pages else None
        prev_page = page - 1 if page > 1 else None

        hyper_dict = {'page_size': page_size,
                      'page': page,
                      'data': data,
                      'next_page': next_page,
                      'prev_page': prev_page,
                      'total_pages': total_pages}
        return (hyper_dict)
