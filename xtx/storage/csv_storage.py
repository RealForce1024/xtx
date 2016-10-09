#!/usr/bin/env python
# -*- coding: utf-8  -*-

import os
import os.path

from xtx.storage.text_file_storage import TextFileStorage
from xtx.storage.exceptions import (StorageExistsError
    , StorageNotFoundError)

class CsvStorage(TextFileStorage):

    def __init__(self, filepath):
        super().__init__(filepath)

    def write(self, data, overwrite = False):
        if not self.exists():
            raise StorageNotFoundError(self.filepath)
        openmode = "a" if overwrite == False else "w"
        with open(self.filepath, openmode, encoding="utf-8") as file:
            for row in data:
                file.write(','.join(list(map(str, row))))
                file.write('\n')


    def read(self, limit = -1):
        if not self.exists():
            raise StorageNotFoundError(self.filepath)
        data = []
        with open(self.filepath, "r", encoding="utf-8") as file:
            line_index = 0
            for line in file.readlines():
                if limit != -1 and line_index >= limit:
                    break
                data.append(line.split(','))
                line_index += 1
        return data
