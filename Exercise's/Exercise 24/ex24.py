# LPTHW Exercise 24 - More practice

# Practice what we learn'd so far
print "Let's practice everything..."
print 'You\'d need to know \'bout escapes with \\ that do \n newline and \t tabs.'

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \nthe need of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""

print "---------------"
print poem
print "---------------"

five = 10 - 2 + 3 - 6
print "This should be five: %s" % five

def secret_formula(started):
	jelly_bean = started * 500
	jars = jelly_bean / 1000
	crates = jars / 100
	return jelly_bean, jars, crates

# init' start_point as 10000 for later use in started variable in secret_fornula() function. 
start_point = 10000

# assign the return variables values 
beans, jars, crates = secret_formula(start_point)

print "With a starting point of: %d" % start_point
print "We'd have %d beans, %d jars, and %s crates." % (
	beans, jars, crates)

start_point = start_point / 10

print "We can also do that this way:"
print "We'd have %d beans, %d jars and %d crates." % secret_formula(start_point) 
