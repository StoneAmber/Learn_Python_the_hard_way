# -*- coding: utf-8 -*-

from sys import argv
import codecs

script, input_file = argv

def print_all(f):

    print f.read()

def rewind(f):
    f.seek(0)

def print_a_line(line_count, f):
    print line_count, f.readline()

current_file = codecs.open(input_file, 'r', encoding='utf_16_le')

print "First let's print the whole file:\n"

print_all(current_file)

print "Now let's rewind, kind of like a tape."

rewind(current_file)

print "Let's print three lines:"

current_line = 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

current_file.close()

'''
PS E:\wind\python\learn_python_the_hard_way> py -2 ex20_1.py ex20utf16le.txt
First let's print the whole file:

Traceback (most recent call last):
  File "ex20_1.py", line 22, in <module>
    print_all(current_file)
  File "ex20_1.py", line 10, in print_all
    print f.read()
UnicodeEncodeError: 'gbk' codec can't encode character u'\ufeff' in position 0:
illegal multibyte sequence
PS E:\wind\python\learn_python_the_hard_way>
'''
''' run result from IDLE 2.7.13
>>> from sys import argv
>>> sys.argv = ['E:/wind/python/learn_python_the_hard_way/ex20_1.py','E:/wind/python/learn_python_the_hard_way/ex20utf16le.txt']
>>> execfile('E:/wind/python/learn_python_the_hard_way/ex20_1.py')
First let's print the whole file:

﻿line 1    May the code be with you.

 line2  Aha!

line 3  wrote somethings


Now let's rewind, kind of like a tape.
Let's print three lines:
1 ﻿line 1    May the code be with you.


2  line2  Aha!


3 line 3  wrote somethings

>>>
'''
