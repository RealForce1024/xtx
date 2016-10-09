#!/usr/bin/env python
# -*- coding: utf-8  -*-

import os.path
from xtx.storage.storage import Storage

class DbTableStorage(Storage):

	def __init__(self, dbconnection, schema, tablename):
		
		location = {"dbconnection": dbconnection, "schema": schema, "tablename": tablename}
		super().__init__(location)
		self.dbconnection = dbconnection
		self.schema = schema
		self.tablename = tablename

	def create(self, force = False):
		return super().create(force)

	def exists(self):
		return super().exists()

	def clear(self, force = False):
		return super().clear(force)

	def remove(self, force = False):
		return super().remove(force)

	def copy(self, path = None):
		return super().copy(path)

	def read(self, limit =  -1):
		return super().read(limit)

	def write(self, data, overwrite = False):
		return super().write(data, overwrite)
