'''
Determine School Grade
To solve this program:
Don't use th input function in this code
1. Assign an age to the variable age
2. Based on age using conditional and logical operators output one of the following:
a. "Too young for School"
b. "Go to Kindergarten"
c. "Go to Grade [Calculated Grade]"
c. "Go to College"

Going for a minimalist program, did not comment the code
'''
age = int(input("Enter Age: "))
if age < 5: print("Too Young for School")
elif age == 5: print("Go to Kindergarten")
elif (age >= 6) and (age <= 17): print("Go to Grade", age-5)
else: print("Go to College")