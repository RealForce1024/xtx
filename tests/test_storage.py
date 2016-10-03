#!/usr/bin/env python
# -*- coding: utf-8  -*-

import unittest

from ..xtx.storage.storage import Storage


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
		s = FileStorage()



def suite():
	suite = unittest.TestSuite()
	suite.addTest(StorageTest("test_instance"))
	return suite

if __name__ == "__main__":
	unittest.main(defaultTest = "suite")
