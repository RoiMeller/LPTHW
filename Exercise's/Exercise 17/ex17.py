# LPTHW Exercise 17 - More files

# import the argv function
from sys import argv
# import exists function
from os.path import exists

script, from_file, to_file = argv

print "Copying from %s to %s" % (
	from_file, to_file)

# We could do these two on one line, how ?
in_file = open(from_file)
in_data = in_file.read()

# len () function gets the length of the string that you pass to it then returns that as a number.
print "The input file is %d bytes long" % len(in_data)

# exist() function return True if a file exists, 
# based on its name in a string as an argument. 
# It returns False if not
print "Does the output file exist? %r" % exists(to_file)
print "Ready, hit RETURN to continune, CTRL-C (^C) to abort."
raw_input("~]$ ")

out_file = open(to_file, 'w')
out_file.write(in_data)

print "Alright, all done... "

# save the output close and free up any system resources taken up by the open file.
out_file.close()
in_file.close()


