# LPTHW Exercise 32 - Loops and Lists

the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# for-loop that's goes thrugh the list
for number in the_count:
	print "This is count %d" % number

# same as above
for fruit in fruits:
	print "A fruit of type: %s" % fruit

# we can go through mixed lists as well
# we have to use %r since we don't know what's in it
for i in change:
	print "I got %r" % i

# we can also build lists, first start with an empty one
elements = []

# uses the range function to count from 0 to 5 
for i in range(0, 6):
	print "Adding %d to the list." % i
	# appended (i) and updates element list
	elements.append(i)

# now we can print them out too
for i in elements:
	print "Element was: %d" % i


