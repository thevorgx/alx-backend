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

        data_list = self.dataset()

        if start_idx < len(data_list):
            return (data_list[start_idx:end_idx])
        else:
            return([])
