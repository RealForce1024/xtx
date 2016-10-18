import sys
sys.path.append(r"../xtx/")

import os
import unittest

from xtx.data import *
from tests.testing import Testing

class DataRowTest(Testing):

	def setUp(self):
		pass

	def tearDown(self):
		pass

	def test_index_getter(self):
		pass

def suite():
	suite = unittest.TestSuite()
	#suite.addTest(EmlStorageTest("test_create_file_not_exists"))
	#suite.addTest(EmlStorageTest("test_create_file_exists"))
	#suite.addTest(EmlStorageTest("test_create_file_exists_force"))
	suite.addTest(DataRowTest("test_index_getter"))
	#suite.addTest(EmlStorageTest("test_read_limit"))
	#suite.addTest(EmlStorageTest("test_write_append"))
	#suite.addTest(EmlStorageTest("test_write_overwrite"))
	#suite.addTest(EmlStorageTest("test_copy"))
	#suite.addTest(EmlStorageTest("test_copy_path"))
	return suite

if __name__ == "__main__":
	unittest.main(defaultTest = "suite")