#!/usr/bin/env python
# -*- coding: utf-8  -*-

import os
import os.path

from file_storage import FileStorage

class CsvStorage(FileStorage):

    def __init__(self, filepath):
        super().__init__()





    def write(self, data, overwrite = True):
        if not os.path.exists(self.filepath):
            raise FileNotFoundError
        with open(self.filepath, "w", encoding="utf-8") as file:
            for row in data:
                file.write(','.join(row))
                file.write('\n')


    def read(self, line_limit = -1):
        if not os.path.exists(self.filepath):
            raise FileNotFoundError
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
	cs = CsvStorage("")
