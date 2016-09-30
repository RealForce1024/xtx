#!/usr/bin/env python
# -*- coding: utf-8  -*-

import os.path
import pandas as pd

from abc import ABCMeta,abstractmethod

from storage import Storage

class FileStorage(Storage, metaclass = ABCMeta):

    def __init__(self, filepath = None):
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

    @abstractmethod
    def write(self, data, overwrite = True):
        pass

    @abstractmethod
    def read(self, line_limit = -1):
        pass

