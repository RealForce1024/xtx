#!/usr/bin/env python
# -*- coding: utf-8  -*-

def detectCharset(filepath):
	import chardet
	f = open(filepath, "rb")
	return chardet.detect(f.read())