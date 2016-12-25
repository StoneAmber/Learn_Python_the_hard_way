# -*- coding: utf-8 -*

from sys import argv

script, user_name, user_type,= argv
prompt = '-->'
public = "pass4"

password = raw_input("password: ")

if  password == public :
    print "Welcome %s,this is PUB" % user_name
else :
    print "password ERROR!"

'''
SyntaxError:invaild syntax. ^ points end of public.
What wrong ?
OH! I don't knew the if rules.Block controled by if
must be end with : 
'''
