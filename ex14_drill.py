# -*- coding: utf-8 -*

from sys import argv
script, user_name, user_type,= argv

prompt = '-->'

password = raw_input(prompt)

print "Welcome %s,this is PUB!Type:%s" % ( user_name,
        user_type)
