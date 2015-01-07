# LPTHW Exercise 18 - Names, Variables, Code, Function

# def (=define) will tell python we want to make a function
# print_two = the name of the function
# *args - the variables names ( its has to go inside '()' parentheses
# we end the function line with :
def print_two(*args):
# all the lines that are indented four spaces will become attached to this function
	arg1, arg2 = args
	print "arg1: %r, arg2: %r" % (arg1, arg2)

def print_two_again(arg1, arg2):
	print "arg1: %r, arg2: %r" % (arg1, arg2)

def print_one(arg1):
	print "arg1: %r" % arg1

def print_none():
	print "I got nothin'g..."

print_two("Roi", "Meller")
print_two_again("Roi", "Meller")
print_one("First!")
print_none()
