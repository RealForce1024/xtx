#!/usr/bin/env python
# -*- coding: utf-8  -*-

"""
execute the unittest file in xtx home directory.
"""

import sys
sys.path.append(r"../xtx/")

import unittest

from xtx.storage.storage import Storage
from xtx.storage.file_storage import FileStorage
from xtx.storage.csv_storage import CsvStorage


class StorageTest(unittest.TestCase):

	def setUp(self):
		pass

	def tearDown(self):
		pass

	def test_instance(self):
		s = Storage()


class FileStorageTest(unittest.TestCase):

	def setUp(self):
		pass

	def tearDown(self):
		pass

	def test_create(self):
		s = FileStorage()



class CsvStorageTest(unittest.TestCase):

	def setUp(self):
		pass

	def tearDown(self):
		pass

	def test_read(self):

		import os
		print(os.getcwd())

		s = CsvStorage(r"tests/data/test.csv")
		print(s.read())



def suite():
	suite = unittest.TestSuite()
	suite.addTest(StorageTest("test_instance"))
	suite.addTest(FileStorageTest("test_create"))
	suite.addTest(CsvStorageTest("test_read"))
	return suite

if __name__ == "__main__":
	unittest.main(defaultTest = "suite")
