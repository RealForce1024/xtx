#!/usr/bin/env python
# -*- coding: utf-8  -*-

import os
import os.path
from abc import ABCMeta,abstractmethod

from storage import Storage
from exceptions import StorageExistsError

class FileStorage(Storage, metaclass = ABCMeta):

    def __init__(self, filepath = None):
        super().__init__()
        self.filepath = filepath

    def create(self, force = False):
		# if file existed
        if os.path.exists(self.filepath):
            if force == False:
                raise StorageExistsError(self.filepath)
            else:
                os.remove(self.filepath)
		# if dir not existed
		(head, tail) = os.path.split(self.filepath)
		if not os.path.exists(head):
			os.makedirs(head)

        with open(self.filepath, "w") as file:
            pass


    def clear(self, force = False):
        if not os.path.exists(self.filepath):
            raise FileExistsError
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
