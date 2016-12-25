# -*- coding: utf-8 -*

# call argv from sys module
from sys import argv
#arfv will assign paramater to script and then filename
script, filename = argv
# fuction open() open file with default read mode
txt = open(filename)
print "Here's your file %r:" % filename
print txt.read() # call read() method of object txt
                 # to read whole contents of the file
txt.close()

print "Type the filename again:"
file_again = raw_input('>')
txt_again = open(file_again)
print txt_again.read()
txt_again.close()

''' drill 6 from Python shell(Python.exe)
Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:42:59) [MSC v.1500 32 bit (
Intel)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> t = open ("e:/wind/python/ex15_sample.txt")
>>> print t.read()
This is stuff I typed into a file.
It is really cool stuff.
Lots and lots of fun to have in here.
>>>
'''
