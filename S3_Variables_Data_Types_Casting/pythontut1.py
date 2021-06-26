# Assigns the string of characters Derek to the variable named my_name
my_name = "Derek"

# Outputs Hello Derek to the screen
print("Hello", my_name)

# You can use \" when you want to use double quotes between double quotes
# \" is known as an escape sequence
print("\"We never really grow up, we only learn how to act in public\" - Bryan White")

'''
Other Escape Sequences

Newline : \n
Backslash : \\
Single Quote : \’
Backspace : \b
Tab : \t

There is no maximum value for an integer, as long as you have enough memory. You can however get a practical maximum size with this : 
'''

import sys
print(sys.maxsize)

# You can get the maximum size for a float like this

import sys
print(sys.float_info.max)

# Floats have 15 digits of precession
f1 = 1.1111111111111111
f2 = 1.1111111111111111
f3 = f1 + f2
print(f3)

# This is a complex number
Cn1 = 5 + 6j

# A boolean data type can have either a value of True or False
can_vote = True

# Python is dynamically typed. What that means is a variables data type is determined by the value you assign to it
my_age = 43
my_age = "Dog"

# Casting allows you to convert from one type to another
# float to int
print("Cast ", type(int(5.4)))
# float to string
print("Cast 2 ", type(str(5.4)))
# unicode character to string
print("Cast 3 ", type(chr(97)))
# character to unicode
print("Cast 4 ", type(ord('a')))
# integer to float
print("Cast 5 ", type(float(2)))

# This is a comment. Anything after # is ignored
# Write notes about how your code works here

'''
I’m a multi-line comment
'''

# Variable names are case sensitive. For example Age is not the same as age.
Age = 2
Age = 3

# Make sure you are casting to the correct data type when working with variables
# Make sure that you surround calculations with parentheses when they produce a single value
num_1 = "1"
num_2 = "2"
print("1 + 2 =", (int(num_1) + int(num_2)))