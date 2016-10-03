#!/usr/bin/env python
# -*- coding: utf-8  -*-

class Student(object):
	
	# public class fields
	name = "zhangsan"
	
	# private class fields
	__sex = "boy"
	
	def __init__(self):
		# public instance fields
		self.age = 99
		# private instance fields
		self.__addr = "BEIJING"
	
	# private instance method
	def __setAge(self, age):
		self.age = age
	
	# public instance method
	def getName(self):
		return Student.name
		
	def getSex(self):
		return Student.__sex
	
	def getAge(self):
		return self.age
		
	def getAddr(self):
		return self.__addr;
	
	# property getter
	@property
	def addr(self):
		return self.__addr
	
	# property setter
	@addr.setter
	def addr(self, address):
		self.__addr = address
		
	@staticmethod
	def sayHi():
		# a = self.age
		print("hi!")
	
	@classmethod
	def sayGood(cls):
		# a = self.age
		print(cls.name)
		print("Good!")
		
if __name__ == "__main__":
	print(dir(Student))
	s = Student()
	
	# access public class field by class name
	print(Student.name)
	# access public class field by instance
	print(s.name)
	
	print(s.getName())
	
	# print(Student.__sex)
	print(s.getSex())
	
	
	print(s.age)
	print(s.getAge())
	# print(s.__setAge(33))
	
	#print(s.__addr)
	print(s._Student__addr)
	print(s.getAddr())
	s.addr = "SHANGHAI"
	print(s.addr)
	
	s.sayHi()
	Student.sayHi()
	s.sayGood()
	Student.sayGood()