# -*- coding: utf-8 -*-

from sys import argv
script, filename = argv

f = open(filename)
print "%s :" % filename
print f.read()
f.close()
