# -*- coding: utf-8 -*-

x = "There are %d types of people." % 10  10 replace %d
binary = "binary"
do_not = "don't"
y = "Those who knows %s and those who %s." % (binary, do_not)
                     # first %s maps binary,the other maps do_not
print x
print y

print "I said: %r" % x
print "I alsd said: '%s'." % y

hilarious = False # mabe it's a bool type,to indicate condition
joke_evaluation = "Isn't that joke so funny?! %r"
print joke_evaluation % hilarious # %r is mapping hilarious

w = "This is the left side of ..."
e = "a string with right side."
print w + e # link string w and e
