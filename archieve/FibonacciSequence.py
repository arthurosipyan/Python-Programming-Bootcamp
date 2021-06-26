# 1, 1, 2, 3, 5, 8...

# The Fibonacci sequence is defined by:
# Fn = Fn-1 + Fn-2
# Where F0 = 0 and F1 = 1

def fibonacci(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    return fibonacci(num-1) + fibonacci(num-2)

# How many Fibonacci values should be found? 30
# 1
# 1
# 2
# 3
# 5


fib_amount = int(input("How many Fibonacci values should be found? "))
i = 1
while i <= fib_amount:
    print(fibonacci(i))
    i += 1
