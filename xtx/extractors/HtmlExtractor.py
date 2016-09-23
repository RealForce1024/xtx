#!/usr/bin/env python
# -*- coding: utf-8  -*-

import os.path
import re
import pandas as pd
from HTMLParser import HTMLParser

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

class __MyHtmlParser(HTMLParser):


	tables = []
	table = []
	row = []

	def handle_starttag(self, tag, attrs):
		if tag == "table":
			pass
		elif tag == "tr":
			pass
		elif tag == "th" or tag == "td":
			pass

	def handle_endtag(self, tag):
		if tag == "table":
			pass
		elif tag == "tr":
			pass
		elif tag == "th" or tag == "td":
			pass

	def handle_data(self, data):
		pass


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
	tables = REG_TABLE.findall(htmlContent)
	for table in tables:
		print(table)
