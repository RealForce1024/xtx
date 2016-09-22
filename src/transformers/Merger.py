#!/usr/bin/env python
# -*- coding: utf-8  -*-

import os

from ExcelReader import ExcelReader
from ExcelWriter import ExcelWriter
from CSVReader import CSVReader

class Merger(object):
	
	def __init__(self, srcDir, targetFile, headerRows = 1):
		self.srcDir = srcDir
		self.targetFile = targetFile
		self.headerRows = headerRows
		
	def merge(self):
		if not os.path.exists(self.srcDir):
			raise FileNotFoundError(self.srcDir)
		
		dataTable_merged = [];
		fileIndex = 0;
		for parent, dirnames, filenames in os.walk(self.srcDir):
			for filename in filenames:
				fullname = os.path.join(parent, filename)
				extName = fullname.split(".")[-1]
				reader = None
				if extName == "csv":
					reader = CSVReader(fullname)
				elif extName == "xls" or extName == "xlsx":
					reader = ExcelReader(fullname, targetSheet = 0)
				else:
					raise ValueError("Unsupported arg type: %s" % fullname)
				datatable = reader.read()
				dataToMerge = datatable if fileIndex == 0 else datatable[self.headerRows:]
				dataTable_merged.extend(dataToMerge)
				fileIndex += 1
		print(dataTable_merged[0:5])
		writer = ExcelWriter(dataTable_merged, targetPath = self.targetFile, targetSheet = 0, recreateFile = True)
		writer.write()
		
		
if __name__ == "__main__":
	srcDir = r"D:\svnserver\业务数据\网银快捷复够率数据\tmp_1-5"
	targetFile = r"D:\svnserver\业务数据\网银快捷复够率数据\1-5.xlsx"
	merger = Merger(srcDir, targetFile)
	merger.merge()
	print("OK")