#!/usr/bin/env python
# -*- coding: utf-8  -*-

import unittest

class SimpleFlowTest(unittest.TestCase):
	def setUp(self):
		pass
		
	def tearDown(self):
		pass
		
	def from_eml_to_excel(self):
		self.assertEqual(1, 2)
		

def suite():
	suite = unittest.TestSuite()
	suite.addTest(SimpleFlowTest("from_eml_to_excel"))
	return suite
	
if __name__ == "__main__":
	unittest.main(defaultTest = "suite")