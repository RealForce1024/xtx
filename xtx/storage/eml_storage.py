#!/usr/bin/env python
# -*- coding: utf-8  -*-

import os.path
import pandas as pd

from file_storage import FileStorage

class EmlStorage(FileStorage):

	def __init__(self, filepath = None):
		super().__init__(filepath)

	def write(self, data, overwrite = True):
		raise NotImplementedError

	def read(self, line_limit = -1):
		raise NotImplementedError
