# Enter Calculation : 5 * 6
# 5 * 6 = 30

num1, operator, num2 = input("Enter Calculation: ").split()

if operator == '+':
    print("{} {} {} = {}".format(num1, operator, num2, str(int(num1) + int(num2))))
elif operator == '-':
    print("{} {} {} = {}".format(num1, operator, num2, str(int(num1) - int(num2))))
elif operator == '/':
    print("{} {} {} = {}".format(num1, operator, num2, str(int(num1) / int(num2))))
elif operator == '%':
    print("{} {} {} = {}".format(num1, operator, num2, str(int(num1) % int(num2))))
elif operator == '*':
    print("{} {} {} = {}".format(num1, operator, num2, str(int(num1) * int(num2))))
else:
    print("Invalid input")
