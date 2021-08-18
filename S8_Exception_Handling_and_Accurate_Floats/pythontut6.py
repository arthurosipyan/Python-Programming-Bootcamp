# Exception Handling & Accurate Floats

# By giving the while a value of True it will cycle until a break is reached
while True:
    # If we expect an error can occur surround potential error with try
    try:
        number = int(input("Please enter a number : "))
        break

    # The code in the except block provides an error message to set things right
    # We can either target a specific error like ValueError
    except ValueError:
        print("You didn't enter a number")

    # We can target all other errors with a default
    except:
        print("An unknown error occurred")
print("Thank you for entering a number")

# Python Problem for you to Solve

# I want you to implement a Do While loop in Python
# The rules for a Do While loop is that they always execute all of the code at least once
# After that 1st loop if the condition is true they will run that code again.
'''
I want you to create a guessing game in which the user must chose a number between 1 and 10 with the following format. 

Guess a number between 1 and 10 : 1
Guess a number between 1 and 10 : 3
Guess a number between 1 and 10 : 5
Guess a number between 1 and 10 : 7
You guessed it
'''

secret_number = 7
while True:
    guess = int(input("Guess a number between 1 and 10 : "))

    if guess == secret_number:
        print("You guessed it")
        break

# More Accurate Floats

# The decimal module provides for more accurate floating point calculations
# With from you can reference methods without the need to reference the module like we had to do with math in a previous video
# 28 points of precision by default.
# We can also create an alias being D here to avoid conflicts with methods with the same name

from decimal import Decimal as D

sum = D(0)
sum += D("0.0111111111111111")
sum += D("0.0111111111111111")
sum += D("0.0111111111111111")
print("Sum = ", sum)
sum -= D("0.0333333333333333")
print("Sum = ", sum)






