# LPTHW Exercise 5 - strings include the drill section

name = 'Roi Meller'
age = 29
height = 72.5 # inches
weight = 163 # lbs
eyes = 'Brown'
teeth = 'White'
hair = 'Brown'
inches_to_centimeter = height * 2.54 
pounds_to_kilograms = weight * 0.45359237

print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "He's %d pounds heavy." % weight
print "He's %d centemiters tall." % inches_to_centimeter
print "He's %d kg heavy." % pounds_to_kilograms

print "Actually that's not too heavy."

print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffe." % teeth

# this lline is tricky 
# its print the 3 variables age, height and weight.. 
# then sum them up and print the result 
print "If I add %d, %d, and %d I get %d." % (
	age, height, weight, age + height + weight)

