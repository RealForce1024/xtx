#!/usr/bin/env python
# -*- coding: utf-8  -*-

import unittest

from sqlalchemy import create_engine



class SqlAlchemyTest(unittest.TestCase):

	def setUp(self):
		pass
		
	def tearDown(self):
		pass
		
	def test_pygresql(self):
		import pg
		
		conn = pg.connect(dbname = 'jingdongdw', host = '10.13.40.16', user = 'jingdongdwadmin', passwd = 'jingdongdwadmin.') 
		sql_select = "select * from jd_sys.base_users"
		users = conn.query(sql_select).dictresult()
		self.assertTrue(len(users) > 0)
		for row in users:
			print(row)
			
	def test_sqlalchemy_psycopg2(self):
		db_url = "postgresql+psycopg2://jingdongdwadmin:jingdongdwadmin.@10.13.40.16:5432/jingdongdw"

		engine = create_engine(db_url, echo=True)

		connection = engine.connect()
		
		result = connection.execute("select * from jd_sys.base_users")
		#self.assertTrue(len(result) > 0)
		for row in result:
			print(row)
		
	def test_sqlalchemy_pygresql(self):
		db_url = "postgresql+pygresql://jingdongdwadmin:jingdongdwadmin.@10.13.40.16:5432/jingdongdw"

		engine = create_engine(db_url, echo=True)

		connection = engine.connect()
		
		
def suite():
	suite = unittest.TestSuite()
	suite.addTest(SqlAlchemyTest("test_pygresql"))
	suite.addTest(SqlAlchemyTest("test_sqlalchemy_psycopg2"))
	return suite
	
if __name__ == "__main__":
	unittest.main(defaultTest = "suite")