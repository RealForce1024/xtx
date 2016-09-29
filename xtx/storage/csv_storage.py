#!/usr/bin/env python
# -*- coding: utf-8  -*-

import os
import os.path

from .storage import Storage

class CsvStorage(Storage):

    def __init__(self, filepath):
        super().__init__()


    def create(self, force = False):
        if os.path.exists(self.filepath):
            if force == False:
                raise FileExistError
            else:
                os.remove(self.filepath)
        with open(self.filepath, "w", encoding="utf-8") as file:
            pass


    def clear(self, force = False):
        if not os.path.exists(self.filepath):
            raise FileExistError
        with open(self.filepath, "w", encoding="utf-8") as file:
            file.truncate()


    def remove(self, force = False):
        if os.path.exists(self.filepath):
            os.remove(self.filepath)
        else:
            if force == False:
                raise FileNotFoundError


    def write(self, data):
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
