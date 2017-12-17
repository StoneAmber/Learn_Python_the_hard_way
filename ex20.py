# -*- coding: utf-8 -*-
# from lib sys import argv to use arguemnts
from sys import argv
# two arguments wlll be assigned to script and input_file
script, input_file = argv

def print_all(f): # define print_all function
    print f.read()

def rewind(f):
    f.seek(0) # file object f point to the begin of file

def print_a_line(line_count, f):
    print line_count, f.readline() # readline() to read a line of file

current_file = open(input_file) # open file with default reading mode

print "First let's print the whole file:\n"

print_all(current_file) # call print_all function

print "Now let's rewind, kind of like a tape."

rewind(current_file)

print "Let's print three lines:"

current_line = 1
print_a_line(current_line, current_file)

current_line += 1 # After run this line,current_file is 2.
print_a_line(current_line, current_file)

current_line += 1 # After run this line,current_file is 3.
print_a_line(current_line, current_file)

'''
stonemask@PC MINGW32 /e/WIND/Python/Learn_Python_the_hard_way (master)
$ file ex2*.txt
ex20.txt:        data
ex20ansi.txt:    ASCII text, with CRLF line terminators
ex20utf16le.txt: Little-endian UTF-16 Unicode text, with CRLF, CR line terminators
ex20utf8.txt:    UTF-8 Unicode (with BOM) text, with CRLF line terminators

'''
''' run result
PS E:\wind\python\learn_python_the_hard_way> py -2 ex20.py ex20utf8.txt
First let's print the whole file:

锘縧ine 1    May the code be with you.
 line2  Aha!
line 3  wrote somethings

Now let's rewind, kind of like a tape.
Let's print three lines:
1 锘縧ine 1    May the code be with you.

2  line2  Aha!

3 line 3  wrote somethings

PS E:\wind\python\learn_python_the_hard_way> py -2 ex20.py ex20ansi.txt
First let's print the whole file:

line 1    May the code be with you.
 line2  Aha!
line 3  wrote somethings

Now let's rewind, kind of like a tape.
Let's print three lines:
1 line 1    May the code be with you.

2  line2  Aha!

3 line 3  wrote somethings

PS E:\wind\python\learn_python_the_hard_way>
'''
