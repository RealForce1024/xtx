#!/usr/bin/env python
# -*- coding: utf-8  -*-

import os.path
import re
import pandas as pd
from html.parser import HTMLParser
#from HTMLParser import HTMLParser

# regular expression
REG_TABLE = re.compile(r'<table.*?>.*?</table>', re.M | re.I | re.S)
REG_TR = re.compile(r'<tr.*?>.*?</tr>', re.M | re.I | re.S)
REG_TD = re.compile(r'<td.*?>.*?</td>', re.M | re.I | re.S)
REG_TD_VAL = re.compile(r'<td.*>(.*)</td>')
REG_TH = re.compile(r'<th.*?>.*?</th>', re.M | re.I | re.S)
REG_TH_VAL = re.compile(r'<th.*>(.*)</th>')
REG_H3 = re.compile(r'<h3.*?>.*?</h3>', re.M | re.I | re.S)

class HtmlExtractor(object):

	def __init__(self):
		pass

	def __extract_by_regexp(self, htmlContent):
		tableHtmls = REG_TABLE.findall(htmlContent)
		for tableHtml in tableHtmls:
			trHtmls = REG_TR.findall(tableHtml)
			for trHtml in trHtmls:
				thHtmls = REG_TH.findall(trHtml)
				tdHtmls = REG_TD.findall(trHtml)
				for thHtml in thHtmls:
					pass

				for tdHtml in tdHtmls:
					pass

	def extract(self, filepath = None, content = None):
		htmlContent = None
		if not content is None:
			htmlContent = content
		else:
			if not filepath is None:
				 htmlContent = open(filepath, 'r')
			else:
				raise ValueError("The follow arguments must be specified one:  filepath=%s, content=%s" % \
					(filepath, content))

		htmlParser = __MyHtmlParser()
		htmlParser.feed(htmlContent)
		tablesData = htmlParser.getTables()


class __MyHtmlParser(HTMLParser):

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

	def getTables(self):
		return self.__tables

if __name__ == "__main__":
	htmlContent = "\
		<html>\
			<head><title></title></head>\
			<body>\
				<table>\
					<thead><tr><th>名称</th><th>年龄</th></tr></thead>\
					<tbody>\
						<tr><td>张三</td><td>22</td></tr>\
						<tr><td>李四</td><td>33</td></tr>\
					</tbody>\
				</table>\
				<table>\
					<tr><th><span>名称</span></th><th><span>性别</span></th></tr>\
					<tr><td>张三</td><td>男</td></tr>\
					<tr><td>李四</td><td>女</td></tr>\
				</table>\
			</body>\
		</html>"
	parser = __MyHtmlParser()
	parser.feed(htmlContent)
	data = parser.getTables()
	print(data)
