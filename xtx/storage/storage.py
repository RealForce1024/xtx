#!/usr/bin/env python
# -*- coding: utf-8  -*-

from abc import ABCMeta,abstractmethod

class Storage(object, metaclass = ABCMeta):

	@abstractmethod
	def create(self, force = False):
		"""
		remove the existed one firstly, then create a new none when force is True.
		"""
		pass

	@abstractmethod
	def clear(self, force = False):
		"""
		clear the data whether or not existing foreign relation when force is True.
		"""
		pass

	@abstractmethod
	def remove(self, force = False):
		"""
		remove the storage whether or not existing foreign relations when force is True.
		"""
		pass

	@abstractmethod
	def write(self, data, overwrite = True):
		pass

	@abstractmethod
	def read(self, line_limit = -1):
		pass
