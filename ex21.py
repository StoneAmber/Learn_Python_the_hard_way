# -*-coding: utf-8 -*-

def add(a, b):
	print "ADDING %d + %d" % (a, b)
	return a + b

def substract(a, b):
	print "SUBSTRACTING %d - %d" % (a, b)
	return a - b

def mulitply(a, b):
	print "MULITING %d * %d" % (a, b)
	return a * b

def divide(a, b):
	print "DVIDING %d / %d" % (a, b)
	return a / b

print "Let's do some math with just functions!"

age = add(30, 5)
height = substract(78, 4)
weight = mulitply(90, 2)
iq = divide(100, 2)

print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)

# A puzzple for the extra credit, tpye it in anyway.

print "Here is a puzzle."

what = add(age, substract(height, mulitply(weight, divide(iq, 2))))
print "That becomes: ", what, "Can you do it by hand?"