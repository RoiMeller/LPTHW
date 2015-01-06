# LPTHW Exercise 21 - Functions can return something

def add(a, b):
        print "ADDING %d + %d" % (a, b)
        return a + b

def subtract(a, b):
        print "SUBTRACTING %d - %d" % (a, b)
        return a - b

def multiply(a, b):
        print "MULTIPLYING %d * %d" % (a, b)
        return a * b

def divide(a, b):
        print "DIVIDING %d / %d" % (a, b)
	return a / b

print "Let's do some math with just function!Yay-not!"

age = add(25, 4)
height = subtract(190, 5)
weight = multiply(37, 2)
iq = divide(256, 2)

print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)

# Extra credit
print "Here is a puzzle."

# Taking the return value of one function and using it as the argument of another function.
what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print "That becomes:", what, "Can you do it by hand?"

# Breaking it DOWN!

div = iq / 2
mul = weight * div
sub = height - mul
add  = age + sub
sum = add

print "Here's the total again: %d" ,sum , "Is this it ???"
