# -*- coding: utf-8 -*-

print "How old are you?",
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()

print "So, you're %r old, %r tall and %r heavy," % (
       age, height, weight)


# drill 1
''' from Python Standard Libary for Python 2.7.13
raw_input([prompt])
If the prompt argument is present, it is written to standard output
without a trailing newline.The function then reads a line from
input,converts it to a string (stripping a trailing newline),
and returns that.When EOF is read, EOFError is raised.
Example:
>>>
>>> s = raw_input('--> ')
--> Monty Python's Flying Circus
>>> s
"Monty Python's Flying Circus"
If the readline module was loaded,then raw_input() will use it
to provide elaborate line editing and history features.
'''
# drill 2
print "Where are you from?"
Home_contry = raw_input('>>')
print Home_contry
# drill 3
print "Input your user name",
user_name = raw_input(":")
print user_name
