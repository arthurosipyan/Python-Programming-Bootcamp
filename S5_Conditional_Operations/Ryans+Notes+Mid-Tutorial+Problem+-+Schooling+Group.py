# If age 5 "Go to Kindergarten"
# Ages 6 though 17 goes to grades 1 though 12 "Go to Grade 6"
# If age is greater than 17 then say "Go to College"
age = int(input("Age?: "))
if age == 5:
    print("Go to Kindergarten")
elif age >= 6 and age <= 17:
    print("Go to Grade", (age-5))
elif age > 17:
    print("Go to College")
else:
    print("Too young for school")