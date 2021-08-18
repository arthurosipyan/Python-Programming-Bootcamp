# Conditional Operators
# > : Greater than
# < : Less than
# >= : Greater than or equal to
# <= : Less than or equal to
# == : Equal to
# != : Not equal to

# Drink Question Code
# if, elif, and else are followed by a condition and then a colon
# The code that follows is indented to show what code should be executed depending on the condition
# It is important that the lines be indented exactly the same amount on each line
# I added a default condition with else, so that if the user wanted neither they would get water
drink = input("Pick One (Coke, or Pepsi) : ")
if drink == "Coke":
    print("Here is your Coke")
elif drink == "Pepsi":
    print("Here is your Pepsi")
else:
    print("Here is your water")

# Python Problem for you to Solve

# Taking what you have learned about conditional operators and previous videos, I want you to make a calculator
# You’ll accept 2 numbers separated by an operator
# You’ll then use conditional operators to determine what calculation to make
# Sample output to model :
# Enter Calculation : 5 * 6
# 5 * 6 = 30

# Store the user input of 2 numbers and an operator
num1, operator, num2 = input('Enter Calculation: ').split()

# Convert strings into integers
num1 = int(num1)
num2 = int(num2)

# If, else if (elif) and else execute different code depending on a condition
if operator == "+":
    print("{} + {} = {}".format(num1, num2, num1+num2))

# If the 1st condition wasn't true check if this one is
elif operator == "-":
    print("{} - {} = {}".format(num1, num2, num1 - num2))
elif operator == "*":
    print("{} * {} = {}".format(num1, num2, num1 * num2))
elif operator == "/":
    print("{} / {} = {}".format(num1, num2, num1 / num2))

# If none of the above conditions were true then execute this by default
else:
    print("Use either + - * or / next time")

# Logical Operators
# and : If both are true it returns true
# or : If either are true it returns true
# not : Converts true into false and vice versa

# Write a program that will determine whether a birthday is important or not
# I’ll use the following criteria to determine that.

# 1 - 18 -> Important
# 21, 50, > 65 -> Important
# All others -> Not Important

# Ask for the users age and cast to an integer
age = int(input("Enter Age : "))
# If age is both greater than or equal to 1 and less than or equal to 18 it is true
if (age >= 1) and (age <= 18):
    print("Important Birthday")
# If age is either 21 or 50 then it is true
elif (age == 21) or (age == 50):
    print("Important Birthday")
# We check if age is less than 65 and then convert true to false or vice versa
# This is the same as if we put age > 65
elif not(age < 65):
    print("Important Birthday")
else:
    print("Sorry Not Important")

# 2nd Python Problem for you to Solve

# We’ll determine what grade someone should go to depending on their age. Here is my criteria for determining grade :
# 1. If age 5 “Go to Kindergarten”
# 2. Ages 6 through 17 goes to grades 1 through 12 “Go to Grade 6”
# 3. If age is greater then 17 then say “Go to College”

# Here is sample output :
# Enter age : 6
# Go to Grade 6

# Ask for the age
age = int(input("Enter age: "))

# Handle if age < 5
if age < 5:
    print("Too Young for School")

# Special output just for age 5
elif age == 5:
    print("Go to Kindergarten")

# Since a number is the result for ages 6 - 17 we can check them all
# with 1 condition
# Use calculation to limit the conditions checked
elif (age > 5) and (age <= 17):
    grade = age - 5
    print("Go to Grade {}".format(grade))

# Handle everyone else
else:
    print("Go to College")

# Ternary Operator
# The ternary operator is used to assign one value or another based on a condition
# It follows this format condition_true if condition else condition_false

age = int(input("What is your age? "))
can_vote = True if age >= 18 else False
print("You can vote :", can_vote)
