# -*- coding: utf-8 -*-

formatter = "%r %r %r %r"

print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False ,False ,True)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
     "I had this thing.",
     "That you type up right",
     "But it didn't sing.",
     "So I said goodnight."
)

'''
double-qoutes and single-qoutes are both for string,and they're
almostly same to Python.
%r will print raw representation of variables,it's useful when debugging.
'''
''' From LPTHW sistes
Q:Why does %r sometimes print things with single-quotes
  when I wrote them with double-quotes?
A:Python is going to print the strings in the most efficient way it can,
  not replicate exactly the way you wrote them.This is perfectly fine
  since %r is used for debugging and inspection,so it's not necessary
  that it be pretty.
'''
