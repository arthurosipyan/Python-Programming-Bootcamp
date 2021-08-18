# Your program will:

# 1. Have the user enter their investment amount and expected interest
investment, interest = input("Enter investment and interest: ").split()
investment = float(investment)
interest = float(interest)/100
# 2. Each year their investment will increase by their investment + their investment * interest rate
total = investment
total = float(total)
for i in range(10):
    total = total + (investment * interest)
# 3. Print out their earnings after a 10 year period
print("Your earnings after 10 years is ${:.2f} from an initial investment of ${:.2f}".format(total - investment, investment))
print("Your total amount of money is now ${:.2f}".format(total))
