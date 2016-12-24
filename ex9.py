# -*- coding: utf-8 -*-

days = "Mon Tue Wed Thu Fri Sat Sun"
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nAug"
#            \n is able to wrap.
print "Here are the days: ", days
print "Here are the months: ",months

print """
There's somenthing going here.
With the three double-qoutes.
We'll be able to type as mush as we like.
Even 14 lines if we want, or 5, or 6.
"""
'''
Maybe print """ somenthing like ...... """
will print the strings literaly.(include wraps,spaces)
'''
''' from LPTHW
Q: Why do the \n newlines not work when I use %r?
A: That's how %r formatting works;it prints it the way
you wrote it (or close to it).It's the "raw" format
for debugging
