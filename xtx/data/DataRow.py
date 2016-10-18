#!/usr/bin/env python
# -*- coding: utf-8  -*-

class DataRow(object):
	
	def __init__(self, rowdata):
		self.rowdata = rowdata if len(rowdata) > 0 else []
		
	def append(itemdata):
		self.rowdata.append(itemdata)
		
	def get_data():
		return self.rowdata
		
	def get_data_by_index(index):
		return self.rowdata[index]
		
	def remove_by_index(index):
		del self.rowdata[index]
		