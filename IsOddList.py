def even_or_odd_list(func, values):
    odd_list = []
    for i in range(len(values)):
        if func(i):
            odd_list.append(i)
    return odd_list


def is_even(num):
    return num % 2 == 0


def is_odd(num):
    return num % 2 == 1


def main():
    values = [i for i in range(11)]
    print("Original list: ", values)
    print("Even list: ", even_or_odd_list(is_even, values))
    print("Odd list: ", even_or_odd_list(is_odd, values))


main()
