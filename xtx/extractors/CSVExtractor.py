#!/usr/bin/env python
# -*- coding: utf-8  -*-

import os.path
import pandas as pd

class CsvExtractor(object):

	def __init__(self):
		pass

	def extract(self, filepath, headerRows = 1):
		"""
		Extract data from the excel file.

		Args:
			filepath: the path of target file.
			headerRows: default 1. the rows count of header.

		Returns:
			return the pandas.DataFrame of rows.

		Raises:
			None
		"""

		if not os.path.exists(filepath):
			raise FileNotFoundError(filepath)

		dataTable = []
		for line in open(filepath, 'r'):
			rowdata = line.split(",")
			rowdata = map(str.strip, rowdata)
			dataTable.append(list(rowdata))

		return pd.DataFrame(data = dataTable[headerRows:], columns = dataTable[:headerRows][0])

if __name__ == "__main__":
	filepath = os.path.abspath(r"../../test/read_test/data/test.csv")
	reader = CsvExtractor()
	print(reader.extract.__doc__)
	dt = reader.extract(filepath)
	print(dt)
