#!/usr/bin/env python
# -*- coding: utf-8  -*-

l = ["a", "b", "c", "d"]
for i in l:
	if i == "b" or i == "c":
		l.remove(i)

print("deleted:")
print(l)

l.extend(["e"])
print(l)


al = [["a", "b", "c"], ["d", "e", "f", "g"], ["w", "x", "y", "z"]]
for i in al:
	if len(i) != 3:
		al.remove(i)

print("deleted:")
print(al)

al.extend([["o", "p", "q"]])
print(al)