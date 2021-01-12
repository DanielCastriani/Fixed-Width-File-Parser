from fixed_file.layout import Layout
import os
from typing import List


class FixedFile:

    @classmethod
    def __parse_line(cls, line: str, layout: List[Layout]):
        cols = []
        for l in layout:
            value = line[l.start: l.end + 1]
            if l.dtype == 'int':
                cols.append(int(value))
            elif l.dtype == 'money':
                cols.append(int(value) / 100)
            else:
                cols.append(value.strip(' '))
        return cols

    @ classmethod
    def read_text(cls, path: str, layout: List[Layout], ignore_index: List[int] = None):

        if not os.path.exists(path):
            raise IOError('File not exists!')

        with open(path, 'r') as file:
            lines = file.readlines()

            if ignore_index:
                for index in ignore_index:
                    lines.pop(index)

            return [cls.__parse_line(line, layout) for line in lines]
