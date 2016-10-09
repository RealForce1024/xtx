#!/usr/bin/env python
# -*- coding: utf-8  -*-

from xtx.storage.storage import Storage
import xtx.storage.storage_utils
from xtx.storage.exceptions import *

"""
usage:
	with Temporarize("filepath") as temp:
		....
"""
class Temporarize(object):

	def __init__(self, storage = None, filepath = None):
		if storage is not None :
			if isinstance(storage, Storage):
				self.storage = storage
			else:
				raise TypeError(storage)
		else:
			if filepath is not None:
				self.storage = storage_utils.create_file(filepath, force = False)
			else:
				raise ArgumentsAbsenceError("storage and filepath must be specified one.")

	def __enter__(self):
		return self.storage

	def __exit__(self, e_t, e_v, t_b):
		self.storage.remove(force = True)
