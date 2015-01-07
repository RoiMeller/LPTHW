# LPTHW Exersice 16 - Reading and writing files

from sys import argv

script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want it, hit RETURN."

raw_input("?")

print "Opening the file...."
# open the specific file in write mode
target = open(filename, 'w+')

print "Truncating the file. Goodbye!"
# erase the file content
target.truncate()

print "Now i'm going to ask you for three lines."

# getting the user input by using raw_input
line1 = raw_input("Line 1: ")
line2 = raw_input("Line 2: ")
line3 = raw_input("Line 3: ")

print "I'm going to write these to the file."

# too much repetition!
# target.write(line1)
# target.write("\n")
# target.write(line2)
# target.write("\n")
# target.write(line3)
# target.write("\n")

# write the user input to the file - The better way..
lines = (" %s \n %s \n %s \n ") % (
	line1, line2, line3 )
target.write(lines)

# close and save it :)
print "And finally, we close it..."
target.close()

# open the specific file again to print it out
target = open(filename, 'r')

# print the new file
print "Opening %r." % filename
print target.read()

# close it :)
target.close()
