# -*- coding: utf-8 -*-

from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copying from %s to %s" % (from_file, to_file)
in_file = open(from_file)
indata = in_file.read()

print "The input file is %d bytes long" % len(indata)

print "Does the output file exist? %r" % exists(to_file)
print "Ready, hit RETURN to continue, CTRL-C to abort."
raw_input()

out_file = open(to_file, 'w')
out_file.write(indata)

print "Alright, all done."

out_file.close()
in_file.close()

''' from PowerShell
PS E:\wind\python> echo "This is a test file." >ex17.txt
PS E:\wind\python> type ex17.txt
This is a test file.
PS E:\wind\python> python ex17.py ex17.txt ex17_new.txt
Copying from ex17.txt to ex17_new.txt
The input file is 46 bytes long
Does the output file exist? False
Ready, hit RETURN to continue, CTRL-C to abort.

Alright, all done.
PS E:\wind\python> gc ex17_new.txt # get content of ex17_new.txt
This is a test file.
਍

'''
