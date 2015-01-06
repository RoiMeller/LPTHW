# LPTHW Exercise 33 - While loops

# To avoid endless loop, there are some rule to folow:

# 1. Make sure that you use while-loops sparingly. Usually a for-loop is better.
# 2. Review your while statements and make sure that the boolean test will become False at some point.
# 3. When in doubt, print out your test variable at the top and bottom of the while-loop to see what it's doing.
 
min = raw_input("Enter the start num ~]$ ")
max = raw_input("Enter the max (End-of-loop) num ~]& ")

min = int(min)
max = int(max)

num = []

def count_numbers(min, max):
	while min < max: 
		print "At the top min is %s" % min	
		num.append(min)
		
		min += 1
		
		print "Numbers now: ", num
        	print "At the bottom min is %s" % min
		

count_numbers(min, max)

print "The numbers: "

for numbers in num:
    print numbers

