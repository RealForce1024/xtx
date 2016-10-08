#!/usr/bin/env python
# -*- coding: utf-8  -*-

import os
import os.path

from xtx.storage.file_storage import FileStorage
from xtx.storage.exceptions import (StorageExistsError
    , StorageNotFoundError)

class CsvStorage(FileStorage):

    def __init__(self, filepath):
        super().__init__(filepath)

    def write(self, data, overwrite = True):
        if not os.path.exists(self.filepath):
            raise StorageNotFoundError(self.filepath)
        with open(self.filepath, "w", encoding="utf-8") as file:
            for row in data:
                file.write(','.join(row))
                file.write('\n')


    def read(self, line_limit = -1):
        if not os.path.exists(self.filepath):
            raise StorageNotFoundError(self.filepath)
        data = []
        with open(self.filepath, "r", encoding="utf-8") as file:
            line_index = 0
            for line in file.readlines():
                if line_limit != -1 and line_index >= line_limit:
                    break
                data.append(line.split(','))
                line_index += 1
        return data

if __name__ == "__main__":
    filepath = os.path.abspath(r"../tests/data/test_create.csv")
    cs = CsvStorage(filepath = filepath)
    cs.create(force = True)
