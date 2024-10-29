import csv
import math
from typing import List


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

    def index_range(self, page: int, page_size: int,) -> tuple:
        """returns a tuple with the range of pages"""
        start = (page - 1) * page_size
        end = start + page_size
        return start, end

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """ Returns pages from a data"""
        assert type(page) is int and page > 0
        assert type(page_size) is int and page_size > 0

        start, end = self.index_range(page, page_size)
        data = self.dataset()
        if start > len(data):
            return []
        return data[start: end]
