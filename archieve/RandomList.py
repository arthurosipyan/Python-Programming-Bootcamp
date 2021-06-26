import random

random_list = []

for i in range(5):
    random_list.append(random.randrange(1, 9))


for i in random_list:
    print(i)
