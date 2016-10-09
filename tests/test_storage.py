#!/usr/bin/env python
# -*- coding: utf-8  -*-

"""
execute the unittest file in project root directory.
"""
import os
import sys
sys.path.append(r"../xtx/")
#sys.path.append(r"..\xtx")

import unittest

from xtx.storage.storage import Storage
from xtx.storage.file_storage import FileStorage
from xtx.storage.text_file_storage import TextFileStorage
from xtx.storage.bin_file_storage import BinFileStorage
from xtx.storage.csv_storage import CsvStorage
from xtx.storage.excel_storage import ExcelStorage
from xtx.storage.exceptions import *

def get_func_name():
	import inspect
	#print(inspect.stack()[1])
	return inspect.stack()[1][3]



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
            
            
class TextFileStorageTest(unittest.TestCase):
    
    def setUp(self):
        pass
        
    def tearDown(self):
        pass
        
    def test_instance(self):
		with self.assertRaises(TypeError):
			s = TextFileStorage() # can not instance
        
        
class BinFileStorageTest(unittest.TestCase):
    
    def setUp(self):
        pass
        
    def tearDown(self):
        pass
        
    def test_instance(self):
		with self.assertRaises(TypeError):
			s = BinFileStorage() # can not instance
        
        



class CsvStorageTest(unittest.TestCase):

	def setUp(self):
		self.tmpdir = r"tests/data/tmp/"
		self.classname = self.__class__.__name__
		self.separator = "$"
		self.ext = ".csv"

	def tearDown(self):
		pass

	def test_create_file_not_exists(self):
		testfile = self.classname + self.separator + get_func_name() + self.ext
		s = CsvStorage(self.tmpdir + testfile)
		s.remove(force = True)
		s.create()
		s.remove(force = True)

	def test_create_file_exists(self):
		testfile = self.classname + self.separator + get_func_name() + self.ext
		s = CsvStorage(self.tmpdir + testfile)
		s.remove(force = True)
		s.create()
		with self.assertRaises(StorageExistsError): 
			s.create()
		s.remove(force = True)
		

	def test_create_file_exists_force(self):
		testfile = self.classname + self.separator + get_func_name() + self.ext
		s = CsvStorage(self.tmpdir + testfile)
		s.remove(force = True)
		s.create()
		s.create(force = True)
		s.remove(force = True)

	def test_read(self):
		s = CsvStorage(r"tests/data/test.csv")
		dat = s.read()
		self.assertTrue(len(dat) > 0)

	def test_read_limit(self):
		s = CsvStorage(r"tests/data/test.csv")
		dat = s.read(limit = 5)
		self.assertTrue(len(dat) == 5)

	def test_write_append(self):
		testfile = self.classname + self.separator + get_func_name() + self.ext
		s = CsvStorage(self.tmpdir + testfile)
		if not s.exists():
			s.create()
		dat = [["a", "b", "c"],[1, 2, 3]]
		s.write(data = dat)


	def test_write_overwrite(self):
		testfile = self.classname + self.separator + get_func_name() + self.ext
		s = CsvStorage(self.tmpdir + testfile)
		s.remove(force = True)
		s.create()
		dat = [["a", "b", "c"],[1, 2, 3]]
		s.write(data = dat, overwrite = True)

	def test_copy(self):
		testfile = self.classname + self.separator + get_func_name() + self.ext
		s = CsvStorage(self.tmpdir + testfile)
		s.remove(force = True)
		s.create()
		dat = [["a1", "b1", "c1"],[1, 2, 3]]
		s.write(data = dat, overwrite = True)
		s.copy()
		newfilename = self.classname + self.separator + get_func_name() + FileStorage.POSTFIX + self.ext
		self.assertTrue(os.path.exists(self.tmpdir + newfilename))
		s.remove()

	def test_copy_path(self):
		testfile = self.classname + self.separator + get_func_name() + self.ext
		s = CsvStorage(self.tmpdir + testfile)
		s.remove(force = True)
		s.create()
		dat = [["a11", "b11", "c11"],[1, 2, 3]]
		s.write(data = dat, overwrite = True)
		newpath = self.tmpdir + os.path.sep + "test_copy2.csv"
		s.copy(path = newpath)
		self.assertTrue(os.path.exists(newpath))
		s.remove()
		CsvStorage(newpath).remove()

	def test_remove(self):
		with self.assertRaises(StorageNotFoundError):
			s = CsvStorage(r"tests/data/test_notexists.csv")
			s.remove()
		s = CsvStorage(r"tests/data/test_todel.csv")
		s.create()
		s.remove()

	def test_clear(self):
		pass

	

	

class ExcelStorageTest(unittest.TestCase):
	
	def setUp(self):
		self.tmpdir = r"tests/data/tmp/"
		self.classname = self.__class__.__name__
		self.separator = "$"
		self.ext = ".csv"
		
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
	suite.addTest(CsvStorageTest("test_create_file_not_exists"))
	suite.addTest(CsvStorageTest("test_create_file_exists"))
	suite.addTest(CsvStorageTest("test_create_file_exists_force"))
	suite.addTest(CsvStorageTest("test_read"))
	suite.addTest(CsvStorageTest("test_read_limit"))
	suite.addTest(CsvStorageTest("test_write_append"))
	suite.addTest(CsvStorageTest("test_write_overwrite"))
	suite.addTest(CsvStorageTest("test_copy"))
	suite.addTest(CsvStorageTest("test_copy_path"))
	#suite.addTest(CsvStorageTest("test_read"))
	#suite.addTest(ExcelStorageTest("test_read"))
	return suite

if __name__ == "__main__":
	unittest.main(defaultTest = "suite")