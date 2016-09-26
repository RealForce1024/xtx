#!/usr/bin/env python
# -*- coding: utf-8  -*-

import unittest


class SimpleFlowTest(unittest.TestCase):
	def setUp(self):
		pass
		
	def tearDown(self):
		pass
		
	def test_from_excel_to_postgres(self):
		file_path = "data/test.xlsx"
		sheetIndex = 0
		db_url = ""
		db_username = ""
		db_userpwd = ""
		rules = [
			Rule(column = "日期", type = Types.Date, targetField = "date", emptyHandler, unmatchHandler)
			, Rule(column = "类型", type = Types.Enum, targetField = "type", emptyHandler, unmatchHandler, saveRawField = "type_raw")
			, Rule(column = "银行", type = Types.String, targetField = "bank", emptyHandler, unmatchHandler, saveRawField = "bank_raw")
			, Rule(column = "卡类型", type = Types.Enum, targetField = "cardtype", emptyHandler, unmatchHandler, saveRawField = "cardtype_raw")
			, Rule(column = "用户数", type = Types.Integer, targetField = "usersCount", emptyHandler, unmatchHandler)
			, Rule(column = "卡数", type = Types.Integer, targetField = "cardsCount", emptyHandler, unmatchHandler)
		]
		loader = Loader(data = dat ,rules = rules)
		# self.assertEqual(1, 2)
		

def suite():
	suite = unittest.TestSuite()
	suite.addTest(SimpleFlowTest("test_from_excel_to_postgres"))
	return suite
	
if __name__ == "__main__":
	unittest.main(defaultTest = "suite")