#!/usr/bin/env python
# -*- coding: utf-8  -*-

class DataSet(object):
	
	def __init__(self, *tables):
		self.tables = tables if len(tables) > 0 else [];
	
	def append(self, table):
		self.tables.append(table)
		
	def insert(self, index, table):
		pass
		
	def remove_table_by_index(self, index):
		pass
		
	def get_table_by_index(self, index):
		pass
		
	def get_table_by_name(self, name):
		pass
		
	def get_table_names(self):
		pass
	
	def get_tables_size(self):
		return len(self.get_tables())
		
	def get_tables(self):
		return self.tables
		
	
		
		