from fixed_file.layout import Layout
import os
from typing import List


class FixedFile:
    data: list
    columns: list

    def __init__(self, data: list, columns: list) -> None:
        self.data = data
        self.columns = columns

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

            data = ([cls.__parse_line(line, layout) for line in lines])
            columns = [h.name if h.name else 'Unamed:%d' %
                       i for i, h in enumerate(layout)]

            return FixedFile(data, columns)

    def to_csv(self, path: str, sep=',', columns_name=True):
        with open(path, 'w') as file:
            if columns_name:
                data = [[str(col) for col in row] for row in self.data]
                csv = [sep.join(row) for row in data]

                if columns_name:
                    csv.insert(0, sep.join(self.columns))

                file.write('\n'.join(csv))
