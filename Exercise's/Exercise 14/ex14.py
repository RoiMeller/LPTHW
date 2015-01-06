# LPTHW Exercise 14 - Prompting an Passing

from sys import argv

script, your_name, your_age = argv
prompt = '~]$ '

print "Hi %s, I'm the %s script..." % (your_name, script)
print "I'd like to ask you a few question."
print "Do you like me %s?" % your_name
likes = raw_input(prompt)

print "Where do you live %s ?" % your_name
lives = raw_input(prompt)

print "What kind of a comuter do you have?"
computer = raw_input(prompt)



print "Alright, so you said %r about liking me." % likes 
print "Your'e %r yers old..." % your_age

print """
You live in %r. 
And you have a %r computer. nice!
""" % (lives, computer)

