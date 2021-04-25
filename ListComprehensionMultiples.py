# random list that holds 50 values of random numbers from 1-1000
# return multiples of 9 using list comprehension

import random

print([x for x in [random.randint(1, 1001) for i in range(50)] if x % 9 == 0])
