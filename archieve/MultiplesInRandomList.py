import random


def main():
    random_list = list(random.randint(1, 1001) for i in range(100))
    print(list(filter((lambda x: x % 9 == 0), random_list)))


main()
