#!/usr/bin/env python
# -*- coding: utf-8  -*-

import os.path

from xtx.storage.text_file_storage import TextFileStorage

class EmlStorage(TextFileStorage):

	def __init__(self, filepath = None):
		super().__init__(filepath)

	def write(self, data, overwrite = True):
		raise NotImplementedError

	def read(self, limit = -1):
		raise NotImplementedError
