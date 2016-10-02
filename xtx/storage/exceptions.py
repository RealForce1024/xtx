#!/usr/bin/env python
# -*- coding: utf-8  -*-

class StorageExistsError(Exception):

	def __init__(self, location):
		self.location = location

	
