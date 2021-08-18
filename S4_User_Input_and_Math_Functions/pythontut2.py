# Request user input and print a hello message
name = input('What is your name : ')
print('Hello', name)

# Assign 2 values by splitting user input at the whitespace
num_1, num_2 = input('Enter 2 Numbers : ').split()
# Convert strings into regular numbers (integers)
num_1 = int(num_1)
num_2 = int(num_2)
# Add the values entered and store in sum
sum_1 = num_1 + num_2

# Subtract the values and store in difference
difference = num_1 - num_2

# Multiply the values and store in product
product = num_1 * num_2

# Divide the values and store in quotient
quotient = num_1 / num_2

# Use modulus on the values to find the remainder
remainder = num_1 % num_2

# format() loads the variable values in order into the {} placeholders
print("{} + {} = {}".format(num_1, num_2, sum_1))
print("{} - {} = {}".format(num_1, num_2, difference))
print("{} * {} = {}".format(num_1, num_2, product))
print("{} / {} = {}".format(num_1, num_2, quotient))
print("{} % {} = {}".format(num_1, num_2, remainder))

# Python Problem
'''
I want you to write a program that:

Asks the user to input the number of miles
You’ll convert miles to kilometers (kilometers = miles * 1.60934)
Then print this for example 5 miles equals 8.0467 kilometers
'''

# Solution
# Ask the user to input miles and assign it to the miles variable
miles = input('Enter Miles ')

# Convert from string to integer
miles = int(miles)

# Perform calculation by multiplying 1.60934 times miles
kilometers = miles * 1.60934

# Print results using format()
print("{} miles equals {} kilometers".format(miles, kilometers))

# The Math Module contains many useful functions
# Import the math module
import math

# Because you used import you access methods by referencing the module
print("ceil(4.4) = ", math.ceil(4.4))
print("floor(4.4) = ", math.floor(4.4))
print("fabs(-4.4) = ", math.fabs(-4.4))

# Factorial = 1 * 2 * 3 * 4
print("factorial(4) = ", math.factorial(4))

# Return remainder of division
print("fmod(5,4) = ", math.fmod(5,4))

# Receive a float and return an int
print("trunc(4.2) = ", math.trunc(4.2))

# Return x^y
print("pow(2,2) = ", math.pow(2,2))

# Return the square root
print("sqrt(4) = ", math.sqrt(4))

# Special values
print("math.e = ", math.e)
print("math.pi = ", math.pi)

# Return e^x
print("exp(4) = ", math.factorial(4))

# Return the natural logarithm e * e * e ~= 20 so log(20) tells
# you that e^3 ~= 20
print("log(20) = ", math.log(20))

# You can define the base and 10^3 = 1000
print("log(1000,10) = ", math.log(1000,10))

# You can also use base 10 like this
print("log10(1000) = ", math.log10(1000))

# We have the following trig functions
# sin, cos, tan, asin, acos, atan, atan2, asinh, acosh,
# atanh, sinh, cosh, tanh
# They follow this format
print("sin(0) ", math.sin(0))

# Convert radians to degrees and vice versa
print("degrees(1.5708) = ", math.degrees(1.5708))
print("radians(90) = ", math.radians(90))
