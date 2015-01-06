# LPTHW Exercise 30 - Else and If

pepole = 50
cars = 25
trucks = 10
vehicles = cars + trucks

if cars > pepole:
	print "We should take the cars."
elif cars < pepole:
	print "We should not take the cars."
else:
	print "We can't decide."

if trucks > cars:
	print "That's too many trucks."
elif trucks < cars:
	print "Maybe we could take the trucks."
else:
	print "We still can't decide."

pepole /= 5

if pepole > trucks:
	print "Alright, let's just take the trucks."
elif cars != trucks and vehicles > pepole:
	print "We have enough vehicles."
else:
	print "Fine, let's stay home then."

