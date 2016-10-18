#!/usr/bin/env python
# -*- coding: utf-8  -*-

import os
import os.path
import re
from html.parser import HTMLParser

from xtx.storage.text_file_storage import TextFileStorage
from xtx.storage.exceptions import ArgumentsAbsenceError

class HtmlStorage(TextFileStorage):

	def __init__(self, filepath = None, content = None):
		super().__init__(filepath)
		self.content = content

	def write(self, data, overwrite = True):
		raise NotImplementedError

	def read(self, limit = -1, encoding = "utf-8"):
		htmlContent = None
		if self.content is not None:
			htmlContent = self.content
		else:
			if self.filepath is not None:
				 with open(self.filepath, "r", encoding = encoding) as file:
					htmlContent = file.read()
			else:
				raise ArgumentsAbsenceError("The follow arguments must be specified one:  filepath=%s, content=%s" % \
					(self.filepath, self.content))

		htmlParser = SimpleHtmlParser()
		htmlParser.feed(htmlContent)
		tablesData = htmlParser.get_tables()
		return tablesData
	

class RegExpHtmlParser(object):

	# regular expression
	REG_TABLE = re.compile(r'<table.*?>.*?</table>', re.M | re.I | re.S)
	REG_TR = re.compile(r'<tr.*?>.*?</tr>', re.M | re.I | re.S)
	REG_TD = re.compile(r'<td.*?>.*?</td>', re.M | re.I | re.S)
	REG_TD_VAL = re.compile(r'<td.*>(.*)</td>')
	REG_TH = re.compile(r'<th.*?>.*?</th>', re.M | re.I | re.S)
	REG_TH_VAL = re.compile(r'<th.*>(.*)</th>')
	REG_H3 = re.compile(r'<h3.*?>.*?</h3>', re.M | re.I | re.S)

	def __init__(self):
		pass

	def parse(self, htmlContent):
		tableHtmls = RegExpHtmlParser.REG_TABLE.findall(htmlContent)
		for tableHtml in tableHtmls:
			trHtmls = RegExpHtmlParser.REG_TR.findall(tableHtml)
			for trHtml in trHtmls:
				thHtmls = RegExpHtmlParser.REG_TH.findall(trHtml)
				tdHtmls = RegExpHtmlParser.REG_TD.findall(trHtml)
				for thHtml in thHtmls:
					pass

				for tdHtml in tdHtmls:
					pass


class SimpleHtmlParser(HTMLParser):

	def __init__(self):
		super().__init__()
		self.__tables = []
		self.__table = []
		self.__row = []
		self.__appendable = False

	def handle_starttag(self, tag, attrs):
		if tag == "table":
			self.__table = []
		elif tag == "tr":
			self.__row = []
		elif tag == "th" or tag == "td":
			self.__appendable = True
		else:
			pass

	def handle_endtag(self, tag):
		if tag == "table":
			self.__tables.append(self.__table)
		elif tag == "tr":
			self.__table.append(self.__row)
		elif tag == "th" or tag == "td":
			self.__appendable = False
		else:
			pass

	def handle_data(self, data):
		if self.__appendable == True:
			self.__row.append(data.strip())

	def get_tables(self):
		return self.__tables

