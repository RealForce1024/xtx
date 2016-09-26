#!/usr/bin/env python
# -*- coding: utf-8  -*-

import unittest


class SimpleFlowTest(unittest.TestCase):
	def setUp(self):
		pass
		
	def tearDown(self):
		pass
		
	def test_from_excel_to_postgres(self):
		file_path = ""
		db_url = ""
		db_username = ""
		db_userpwd = ""
		
		# self.assertEqual(1, 2)
		

def suite():
	suite = unittest.TestSuite()
	suite.addTest(SimpleFlowTest("test_from_excel_to_postgres"))
	return suite
	
if __name__ == "__main__":
	unittest.main(defaultTest = "suite")