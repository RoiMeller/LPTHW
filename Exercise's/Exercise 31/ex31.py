# LPTHW Exercise 31 - Making decisions

choices = """
Do you go through door num' #1 or door num' #2 ?
"""

print "You enter a dark room with two doors."

while True:
	print choices

	door = raw_input("~]$ ")

	if door == "1":
		print "There's a giant bear here eatint a cheese cake. What do you do?"
		print "1. Take the cake."
		print "2. Scream at the bear."
		print "3. Run out!."

		bear = raw_input("~]$ ")

		if bear == "1":
			print "The bear eats your face off. Good job!"
			break
		
		elif bear == "2":
			print "The bear slapped you!\n"
			print """ 
			What woul'd you like to do?
			1. Get out.
			2. fight!.\n
			"""
		
			user_choice = raw_input("~]$ ")
				
			if user_choice == "1":
				print "You've got out"
			elif user_choice == "2":
				print "The bear eats your face off. Good job!"
				break
		
		elif bear == "3":
			print "You've got out"
		
		else:
			print "Well, doing %s is probably better. bear runs away." % bear
			break

	elif door == "2":
		print """
		You stare into the endless abyss at Cthulhu's retina."
		1. Blueberries."
		2. Yellow jacket clothespins."
		3. Understanding revolvers yelling melodies."
		"""
		insanity = raw_input("~]$ ")

		if insanity == "1" or insanity == "2":
			print "Your body survives powered by a mind of jello. Goodjob!"
			break
		else:
			print "The insanity rots your eyes into a pool of muck. Good job!"
			break

	else:
		print "You stumble around and fall on knife and die. Good job!"
		break

