# LPTHW Exercise 19 - Function and Variables

# Function decloration 
def cheese_and_crackers(cheese_count, boxes_of_crackers):
	print "You haave %d cheeses!" % cheese_count
	print "You haave %d boxes of crackers!" % boxes_of_crackers
	print "Man that's enough for a party!" 
	print "Get a blanket.\n"

print "We can just give the function number directly:"
# pass throw the function the vriables values
cheese_and_crackers(20, 30)

print "Or, we can use variables from our functioln:"
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)

print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

# my own function
arg1 = int(raw_input("Enter the first num: "))
arg2 = int(raw_input("Enter the second num: "))

# Function definition is here
def sum( arg1, arg2 ):
   # Add both the parameters and return them."
   total = arg1 + arg2
   print "print from Inside - The sum of arg1 + arg2 : ", total
   return total

# Call sum() function and print it outside
total = sum(arg1, arg2 )
print "Outside the function : ", total 
