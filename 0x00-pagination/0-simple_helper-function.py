#!/usr/bin/env python3
""" A task on pagination"""


def index_range(page: int, page_size: int,) -> tuple:
    """returns a tuple with the range of pages"""
    start = (page - 1) * page_size
    end = start + page_size
    return start, end
