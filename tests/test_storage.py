#!/usr/bin/env python
# -*- coding: utf-8  -*-

"""
execute the unittest file in xtx home directory.
"""

import sys
sys.path.append(r"../xtx/")
#sys.path.append(r"..\xtx")

import unittest

from xtx.storage.storage import Storage
from xtx.storage.file_storage import FileStorage
from xtx.storage.csv_storage import CsvStorage
from xtx.storage.excel_storage import ExcelStorage


class StorageTest(unittest.TestCase):

	def setUp(self):
		pass

	def tearDown(self):
		pass

	def test_instance(self):
		with self.assertRaises(TypeError):
			s = Storage() # can not instance


class FileStorageTest(unittest.TestCase):

	def setUp(self):
		pass

	def tearDown(self):
		pass

	def test_instance(self):
		with self.assertRaises(TypeError):
			s = FileStorage() # can not instance



class CsvStorageTest(unittest.TestCase):

	def setUp(self):
		pass

	def tearDown(self):
		pass

	def test_create(self):
		pass

	def test_read(self):
		s = CsvStorage(r"tests/data/test.csv")
		dat = s.read()
		self.assertTrue(len(dat) > 0)

class ExcelStorageTest(unittest.TestCase):
	
	def setUp(self):
		pass
		
	def tearDown(self):
		pass
		
	def test_read(self):
		e = ExcelStorage(r"tests/data/test.xlsx")
		dat = e.read()
		self.assertTrue(len(dat) > 0)




def suite():
	suite = unittest.TestSuite()
	suite.addTest(StorageTest("test_instance"))
	suite.addTest(FileStorageTest("test_instance"))
	suite.addTest(CsvStorageTest("test_read"))
	suite.addTest(ExcelStorageTest("test_read"))
	return suite

if __name__ == "__main__":
	unittest.main(defaultTest = "suite")