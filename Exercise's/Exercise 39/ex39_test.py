import hashmap

# call hashmap new() function to Initializes a Map
states = hashmap.new()
# create a mapping of state to abbreviation
hashmap.set(states, 'Oregon', 'OR')
hashmap.set(states, 'Florida', 'FL')
hashmap.set(states, 'California', 'CA')
hashmap.set(states, 'New York', 'NY')
hashmap.set(states, 'Michigan', 'MI')

# a basic set of states and some cities in them
cities = hashmap.new()
hashmap.set(cities, 'CA', 'San Francisco')
hashmap.set(cities, 'MI', 'Detroit')
hashmap.set(cities, 'FL', 'Jacksonville')
hashmap.set(cities, 'NY', 'New York')
hashmap.set(cities, 'OR', 'Portland')

# create my own basic map
enigma = hashmap.new()

hashmap.set(enigma, '1990', 'MCMXC A.D')
# confirms set will replace previous one
hashmap.set(enigma, '1990', 'MCMXC a.D')
hashmap.set(enigma, '1994', 'The Cross of Change')
hashmap.set(enigma, '1996', 'Le Roi Est Mort, Vive Le Roi!')
hashmap.set(enigma, '1999', 'The Screen Behind the Mirror')
hashmap.set(enigma, '2003', 'Voyageur')
hashmap.set(enigma, '2006', 'A Posteriori')
hashmap.set(enigma, '2008', 'Seven Lives Many Faces')

# print out some cities
print '-' * 10
print "NY State has: %s" % hashmap.get(cities, 'NY')
print "OR State has: %s" % hashmap.get(cities, 'OR')

# print some states
print '-' * 10
print "Michigan's abbreviation is: %s" % hashmap.get(states, 'Michigan')
print "Florida's abbreviation is: %s" % hashmap.get(states, 'Florida')

# do it by using the state then cities dict
print '-' * 10
print "Michigan has: %s" % hashmap.get(cities, hashmap.get(states, 'Michigan'))
print "Florida has: %s" % hashmap.get(cities, hashmap.get(states, 'Florida'))

# print all states abbreviation
print '-' * 10
hashmap.list(states)

# print every city in state
print '-' * 10
hashmap.list(cities)

# print all Enigma album's
print '-' * 10
hashmap.list(enigma)

print '-' * 10
state = hashmap.get(states, 'Texas')

if not state:
	print "Sorry, no Texas."

city = hashmap.get(cities, 'TX', 'Does Not Exist')
print "The city for the state 'TX' is: %s" % city
