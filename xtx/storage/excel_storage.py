#!/usr/bin/env python
# -*- coding: utf-8  -*-

import os.path

from xtx.storage.bin_file_storage import BinFileStorage
from xtx.storage.exceptions import (StorageExistsError
	, StorageNotFoundError
	, UnmatchExtensionError
	, ArgumentsAbsenceError)

class ExcelStorage(BinFileStorage):

	def __init__(self, filepath = None, sheetIndex = -1, sheetName = None):
		super().__init__(filepath)
		self.sheetIndex = sheetIndex
		self.sheetName = sheetName

	def getExtension(self):
		return self.filepath.split(".")[-1]
		
	def __read_excel2003(self, limit = -1):
		import xlrd

		tabledata = []
		wb = xlrd.open_workbook(self.filepath)

		# get worksheet
		ws = None
		if not sheetName is None:
			ws = wb.sheet_by_name(self.sheetName)
		else:
			if not sheetIndex is None:
				ws = wb.sheet_by_index(self.sheetIndex)
			else:
				raise ArgumentsAbsenceError("The targetSheet arguments must be specified one:  sheetIndex=%s, sheetName=%s" % \
					(self.sheetIndex, self.sheetName))

		# get cell data
		for rowIndex in range(0, ws.nrows):
			if (rowIndex + 1) > limit:
				break

			row = ws.row(rowIndex)
			rowdata = []
			for colIndex in range(0, ws.ncols):
				cell = row[colIndex]
				cellval = cell.value
				rowdata.append(cellval)
			tabledata.append(rowdata)

		return tabledata

	def __read_excel2007(self, limit = -1):
		from openpyxl.workbook import Workbook
		from openpyxl import load_workbook
		
		tabledata = []
		wb = load_workbook(filename = self.filepath)
		
		# get worksheet
		ws = None
		if not sheetName is None:
			ws = wb.get_sheet_by_name(self.sheetName)
		else:
			if not sheetIndex is None:
				ws = wb.get_sheet_by_name(wb.get_sheet_names()[self.sheetIndex])
			else:
				raise ArgumentsAbsenceError("The targetSheet arguments must be specified one:  sheetIndex=%s, sheetName=%s" % \
					(self.sheetIndex, self.sheetName))
		
		# get cell data
		for rowNum in range(1, ws.max_row + 1):
			if rowNum > limit:
				break

			rowdata = []
			for colNum in range(1, ws.max_column + 1):
				cellval = ws.cell(row = rowNum, column= colNum).value
				rowdata.append(cellval)
			tabledata.append(rowdata)
		
		return tabledata

	def __write_excel2003(self, data, overwrite = False):
		raise NotImplementedError(self.filepath)

	def __write_excel2007(self, data, overwrite = False):
		raise NotImplementedError(self.filepath)
		
	def write(self, data, overwrite = False):
		if not self.exists(self.filepath):
			raise StorageNotFoundError(self.filepath)

		ext = self.getExtension()
		if ext == "xls":
			self.__write_excel2003(data = data, overwrite = overwrite)
		elif ext == "xlsx":
			self.__write_excel2007(data = data, overwrite = overwrite)
		else:
			raise UnmatchExtensionError(self.filepath)

	def read(self, limit = -1):
		if not self.exists(self.filepath):
			raise StorageNotFoundError(self.filepath)
		
		data = None
		ext = self.getExtension()
		if ext == "xls":
			data = self.__read_excel2003(limit = limit)
		elif ext == "xlsx":
			data = self.__read_excel2007(limit = limit)
		else:
			raise UnmatchExtensionError(self.filepath)
		return data
	