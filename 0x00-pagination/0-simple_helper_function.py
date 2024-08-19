#!/usr/bin/env python3
"""Simple helper function"""


def index_range(page: int, page_size: int) -> tuple:
    """function helper that return a tuple that contain
    start idx and end idx"""
    start_idx = (page-1) * page_size
    end_idx = start_idx + page_size
    idx_range = (start_idx, end_idx)
    return (idx_range)
