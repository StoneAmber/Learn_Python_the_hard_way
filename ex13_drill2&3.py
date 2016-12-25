# -*- coding: utf-8 -*-

from sys import argv

pyname, other = argv
double_argv = argv * 2

p1, p2 = raw_input("ARG1&ARG2:")
p3 = raw_input("ARG3:")

print "pyname:", pyname
print "other:", other
print "double_argv:%r" % double_argv
print "ARG1:%r ARG2:%r" % (p1, p2)
print "ARG3:%r" % p3
