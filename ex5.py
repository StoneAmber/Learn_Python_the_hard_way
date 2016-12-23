# -*- coding: utf-8 -*-

name = 'Zen A. Shaw'
age = 35
height = 74
weight = 180
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %s" %  name
print "He is %f  cms tall." %  (2.54 * height)
print "He's %f kgs heavy." %  (0.45 * weight)
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % ( eyes,  hair)
print "His teeth are usually %s depending on the coffee." %  teeth
print "If I add %d , %d ,and  %d I get %d." % (
        age,  height,  weight, age +  height +  weight)
print round(1/3),round(9/10),round(10/9),round(1.9)
'''
#1
print "If I add %d , %d ,and  %d I get %d." %
      ( age,  height,  weight, age +  height +  weight)
outcome:
PS C:\Users\windman> python e:wind\python\ex5.py
  File "e:wind\python\ex5.py", line 17
    print "If I add %d , %d ,and  %d I get %d." %
                                                ^
SyntaxError: invalid syntax
#2
variables ident & function must begin in the first place of each line.
If u have space(s)before it,It will be unexpected indent error,like these:
PS C:\Users\windman> python e:wind\python\ex5.py
  File "e:wind\python\ex5.py", line 12
    print "He is %d  inches tall." %  height
    ^
IndentationError: unexpected indent

PS C:\Users\windman> python e:wind\python\ex5.py
  File "e:wind\python\ex5.py", line 4
    age = 35
    ^
IndentationError: unexpected indent
'''
