#!/usr/bin/env python
# -*- coding: utf-8  -*-

import email
import os.path

import HtmlExtractor.HtmlExtractor

class EmailExtractor(object):

	def __init__(self, srcPath):
		self.srcPath = srcPath

	def __get_html(self):
		html = None
		with open(self.srcPath, encoding="UTF-8") as file:
			msg = email.message_from_file(file)
			for part in msg.walk():
				if not part.is_multipart():
					r = part.get_payload(decode=True)
					html = r.decode("UTF8")
			file.close()
		return html

	def extract(self):
		html = self.__get_html()
		html_tables = REG_TABLE.findall(html)


if __name__ == "__main__":
	filepath = os.path.abspath(r"..\..\test\read_test\data\test.eml")
	ee = EmailExtractor(filepath)
	print(ee.extract())
