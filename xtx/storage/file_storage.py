#!/usr/bin/env python
# -*- coding: utf-8  -*-

import os
import os.path
from abc import ABCMeta,abstractmethod

from xtx.storage.storage import Storage
from xtx.storage.exceptions import *

class FileStorage(Storage, metaclass = ABCMeta):

    POSTFIX = "$COPY"

    def __init__(self, filepath = None):
        super().__init__(filepath)
        self.filepath = self.location

    def exists(self):
        return os.path.exists(self.filepath)

    def create(self, force = False):
		# if the file existed
        if self.exists():
            if force == False:
                raise StorageExistsError(self.filepath)
            else:
                self.remove(self.filepath)

        (head, tail) = os.path.split(self.filepath)
        if not os.path.exists(head):
            os.makedirs(head)
        with open(self.filepath, "w") as file:
            pass


    def clear(self, force = False):
        if not self.exists():
            if force == False:
                raise StorageNotFoundError(self.filepath)
        with open(self.filepath, "w", encoding="utf-8") as file:
            file.truncate()


    def remove(self, force = False):
        if not self.exists():
            if force == False:
                raise StorageNotFoundError(self.filepath)
        else:
            os.remove(self.filepath)


    def copy(self, path = None):
        if not self.exists():
            raise StorageNotFoundError(self.filepath)
        import shutil
        if path is not None:
            shutil.copyfile(self.filepath, path)
        else:
            newname = None
            dirname = os.path.dirname(self.filepath)
            filename = os.path.basename(self.filepath)
            sections = filename.split(".")
            newname = sections[0] + FileStorage.POSTFIX + "." + sections[1] if len(sections) == 2 else sections[0] + FileStorage.POSTFIX
            shutil.copyfile(self.filepath, dirname + os.path.sep + newname)


    @abstractmethod
    def write(self, data, overwrite = False):
        pass

    @abstractmethod
    def read(self, limit = -1):
        pass
