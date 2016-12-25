# -*- coding: utf-8 -*-

from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copying from %s to %s" % (from_file, to_file)

#print "The input file is %d bytes long" % len(indata)
#print "Does the output file exist? %r" % exists(to_file)
print "Ready, hit RETURN to continue, CTRL-C to abort."
raw_input()

open(to_file, 'w').write(open(from_file).read())

print "Alright, all done."

''' from Q&A
you probably did something like this,
indata = open(from_file).read(),
which means you don't need to then do in_file.close()
when you reach the end of the script.
It should already be closed by Python once that one line runs.
'''
