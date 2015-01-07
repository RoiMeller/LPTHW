# LPTHW Exercise 15 - Reading files 

# load the argument parser module from sys
from sys import argv

# use argv (argument value) to get the filename we wann'a open() later
script, filename = argv

# open the file name
txt = open(filename)
# print a little opening message
print "Here's your file %r: " % filename
# call the  read function on txt by using '.' without any parameters..
print txt.read()

# close and free up any system resources taken up by the open file.
txt.close()

# ask the user to give us the filename again by printing 
# print "Type the filename again: "
# use raw_input() to assign the user input into file_again
# file_again = raw_input("~]$ ")

# open the specific file
# txt_again = open(file_again)
# and print it out :)
# print txt_again.read()
