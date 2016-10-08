#!/usr/bin/env python
# -*- coding: utf-8  -*-

import os
import os.path

from file_storage import FileStorage

class HtmlStorage(FileStorage):

	def __init__(self, filepath = None):
		super().__init__(filepath)

	def write(self, data, overwrite = True):
		raise NotImplementedError

	def read(self, limit = -1):
		raise NotImplementedError
