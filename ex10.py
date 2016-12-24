# -*- coding: utf-8 -*-

print "I am 6'2\" tall."
print 'I am 6\'2" tall.'

tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslah_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishes
\t* Catnip\n\t* Grass
"""

print tabby_cat
print persian_cat
print backslah_cat
print fat_cat

'''while True:
    for i in ["/","-","|","\\","|"]:
        print "%s\r" % i,
'''

print "He said\"I reply,'Who cares?'\""
print "backslah_cat %r, %s" % (
       backslah_cat, backslah_cat )
print "u'\U0001F47E'" # \u is not avialble in Python2
print "\N{u+6c34}" # \N is not declared in Python2
print r"\n",'\\n'
print "backslah_cat %r:",'%r' % backslah_cat,
print '%s:','%s' % backslah_cat
