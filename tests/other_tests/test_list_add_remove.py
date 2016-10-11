#!/usr/bin/env python
# -*- coding: utf-8  -*-

l = ["a", "b", "c", "d"]
todel = []
for i in range(0,len(l)):
	e = l[i]
	if e == "b" or e == "c":
		todel.append(e)

for i in todel:
	l.remove(i)

print("deleted:")
print(l)

l.extend(["e", "f"])
print("extended:")
print(l)


al = [["a", "b", "c"], ["d", "e", "f", "g"], ["w", "x", "y", "z"]]
for i in al:
	if len(i) != 3:
		al.remove(i)

print("deleted:")
print(al)

al.extend([["o", "p", "q"]])
print(al)