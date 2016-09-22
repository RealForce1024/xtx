#!/usr/bin/env python
# -*- coding: utf-8  -*-

import os.path
import re
import pandas as pd

# regular expression
REG_TABLE = re.compile(r'<table.*?>.*?</table>', re.M | re.I | re.S)
REG_TR = re.compile(r'<tr.*?>.*?</tr>', re.M | re.I | re.S)
REG_TD = re.compile(r'<td.*?>.*?</td>', re.M | re.I | re.S)
REG_TD_VAL = re.compile(r'<td.*>(.*)</td>')
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


		tableContents = REG_TABLE.findall(htmlContent)
		for tableContent in tableContents:
			
