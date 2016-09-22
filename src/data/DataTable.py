#!/usr/bin/env python
# -*- coding: utf-8  -*-

class DataTable(object):
	
	def __init__(self, name, *rows):
		self.name = name
		self.rows = rows if len(rows) > 0 ? else []
		
	def append(row):
		self.rows.append(row)
		
	def remove_row_by_index(index):
		pass
		
	def get_row_by_index(index):
		pass
		
	def get_rows():
		return self.rows
	
		
		