#!/usr/bin/env python
# -*- coding: utf-8  -*-

import os.path
import pandas as pd

from file_storage import FileStorage

class ExcelStorage(FileStorage):

    def __init__(self, filepath = None):
        super().__init__()
