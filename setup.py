#!/usr/bin/env python
# -*- coding: utf-8  -*-

from setuptools import setup, find_packages

from xtx import __version__

def readme():
    with open('readme') as f:
        return f.read()

setup(
	name = "xtx", 
	version = __version__, 
	packages = find_packages(),
	keywords = [],
	author = "LIPEI",
	author_email = "pei@ilanever.com",
	description = "",
	long_description=readme(),
	url = "https://github.com/lipei86/xtx"
	)