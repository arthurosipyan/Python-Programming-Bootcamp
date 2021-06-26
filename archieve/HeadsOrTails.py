import random
import time
# Example Output
# Heads: 46
# Tails: 54


def main():
    start = time.time()
    ht_list = [random.choice(list(['h', 't'])) for i in range(100)]
    print("Heads: {} ({}%)".format(ht_list.count("h"), str(int(((ht_list.count("h")/len(ht_list)) * 100)))))
    print("Tails: {} ({}%)".format(ht_list.count("t"), str(int(((ht_list.count("t")/len(ht_list)) * 100)))))
    end = time.time()
    print("Runtime: ", "{:.2f}".format(end - start))


main()
