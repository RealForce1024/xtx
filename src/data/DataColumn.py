#!/usr/bin/env python
# -*- coding: utf-8  -*-

class DataColumn(object):
	
	def __init__(self, name, caption, dataType = type(str), nullable = True, defaultValue = None, parentTable = None):
		self.name = name
		self.caption = caption
		self.dataType = dataType
		self.nullable = nullable
		self.defaultValue = defaultValue
		self.parentTable = parentTable
		
	
		
		