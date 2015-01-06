# LPTHW Exercise 6 - Srings and Text

x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)

print x
print y

# strings inside another string...
# 1
print "I said: %r." % x
# 2
print "I also said: '%s'." % y

hilarious = False
# 3
joke_evaluation = "Isn't that joke so funny?! %r"

# 4
print joke_evaluation % hilarious

w = "This is the left side of..."
e = "A string with a right side."

# add and prints the strings together
print w + e


