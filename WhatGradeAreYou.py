#  If age 5 "Go to Kindergarten"

# Ages 6 through 17 goes to grades 1 through 12... "Go to Grade 6"

# If age is greater then 17 then say "Go to College"

age = int(input("Enter age: "))

if age == 5:
    print("Go to Kindergarten")
elif 6 <= age <= 17:
    print("Go to Grade {}".format(str(age - 5)))
elif age > 17:
    print("Go to College")
else:
    print("Too young for school")
