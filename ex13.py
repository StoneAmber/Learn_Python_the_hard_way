# -*- coding: utf-8 -*-


from sys import argv

script, first, second, third = argv

print "The script is called:", script
print "Your first variable is:", first
print "Yout second variable is:", second
print "Your third variable is:", third


pyname, other, c, d= argv
double_argv = argv * 2

#p1, p2 = raw_input("ARG1&ARG2:")
#p3 = raw_input("ARG3:")

print "pyname:", pyname
print "other:", other
print "c:", c
print "d:", d
print "double_argv:%r" % double_argv
#print "ARG1:%r ARG2:%r" % (p1, p2)
#print "ARG3:%r" % p3
