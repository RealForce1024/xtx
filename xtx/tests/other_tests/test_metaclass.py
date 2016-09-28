#!/usr/bin/env python
# -*- coding: utf-8  -*-

class EntityMetaclass(type):
	
	def __new__(cls, name, bases, attrs):
		print("cls: ", cls)
		print("name: ", name)
		print("bases: ", bases)
		print("attrs: ", attrs)
		def get_props(cls):
			print(cls)
			print("getting props.")
			
		attrs["getProperties"] = get_props
		return type.__new__(cls, name, bases, attrs)
		
class MyEntity(object, metaclass = EntityMetaclass):
	pass
	
m = MyEntity()
m.getProperties()