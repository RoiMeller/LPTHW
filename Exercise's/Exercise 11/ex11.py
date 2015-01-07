# LPTHW Exercise 11

# We put a ',' (comma) at the end of each print line. 
# That way print doesn't end the line with a newline character and go to the next line.

print "How old are you ?",
age = raw_input()

print "How tall are you ?",
height = raw_input()

print "How much do you weight ?",
weight = raw_input()

print "So, your'e %r old, %r tall and %r heavy..." % (
	age, height, weight)

