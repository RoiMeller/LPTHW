# LPTHW Exercise 20 - Function and Files

# import the argv module from sys
from sys import argv

# initializing the argv into input_file variable
script, input_file = argv

# print all the .txt document function
def print_all(f):
	print f.read()

# seek(0) moves the file to the 0 byte (first byte) in the file
def rewind(f):
	f.seek(0)

def print_a_line(line_count, f):
	print line_count, f.readline()

current_file = open(input_file)

print "First let's print the whole file: \n"

print_all(current_file)

print "Now let's rewind, kind of like a tape."

rewind(current_file)

print "Let's print three lines: "

current_line = 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)
