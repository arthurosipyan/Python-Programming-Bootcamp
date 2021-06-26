# Your program will:
# 1. Have the user enter their investment amount and expected interest
# 2. Each year, their investment will increase by their investment + their investment * the interest rate
# 3. Print out their earnings after a 10 year period

investment = float(input("Enter investment: "))
interest = float(input("Enter interest: "))/100

for i in range(1, 11):
    investment += investment * interest
    print("{} year return: ${:.2f}".format(i, investment))
