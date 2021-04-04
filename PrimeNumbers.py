def is_prime(num):
    for i in range(2, num):
        if num % 2 == 0:
            return False
    return True


def get_primes(max_number):
    list_of_primes = []
    for num in range(2, max_number):
        if is_prime(num):
            list_of_primes.append(num)
    return list_of_primes


def main():
    max_number_to_check = int(input("Search for primes up to: "))
    list_of_primes = get_primes(max_number_to_check)
    for prime in list_of_primes:
        print(prime)


main()
