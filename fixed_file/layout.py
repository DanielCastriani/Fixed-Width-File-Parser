from typing import Union


class Layout:
    start: int
    end: int
    name: Union[str, None]
    dtype: Union[str, None]
    index_offset: int

    def __init__(self, start: int, end: int, name: str = None, dtype: str = None, index_offset: int = 1):
        self.start = start - index_offset
        self.end = end - index_offset
        self.name = name
        self.dtype = dtype
        self.index_offset = index_offset
