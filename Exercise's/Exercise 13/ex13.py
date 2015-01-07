# LPTHW Exercise 13 - Parameters, Unpacking, Variables

# import - add module ("libraries\features") from the python modules set by asking you which one you want 
# (argv - argument variable - hold the argument that you pass to your python script )
from sys import argv

# this line "unpacks" argv so that, rather than holding all the arguments
# it's get assigned to four variables...
script, first = argv

# Print the first unpacked variable from argv
print "The script is called: ", script

# variables passing by the user :)
first = raw_input("Your first variable is: ")
second = raw_input("Your second variable is: ")
three = raw_input("Your third variable is: ")
print "Your variables are... %r %r %r " % (
	first, second, three)
