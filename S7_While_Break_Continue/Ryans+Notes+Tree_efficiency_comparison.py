'''
Comments on a slightly different solution Christmas tree problem
Zhimin · Lecture 11
I'm not sure if my question is important but I just want to get more insight. My code is below, how would you comment on the execute efficiency and memory usage? which one will be more effective when it comes to more complicated problems?

tree_level = input("How tall is the tree :")
tree_level = int(tree_level)
n = 1  # n is the current tree level being printed
while n <= tree_level:
    for i in range(1, tree_level - n + 1):
        print(" ", end="")
    for i in range(1, 2 * n):
        print("#", end="")
    n += 1
    print()
for i in range(1, tree_level):
    print(" ", end="")
print("#")

Derek Banas
Derek — Instructor
I provide all the code here for you to be able to compare the efficiency of the 2 functions. I didn't aim to maximize efficiency, but it turned out pretty good as you'll see.

import time
def make_tree():
    tree_level = 5
    n = 1  # n is the current tree level being printed
    while n <= tree_level:
        for i in range(1, tree_level - n + 1):
            print(" ", end="")
        for i in range(1, 2 * n):
            print("#", end="")
        n += 1
        print()
    for i in range(1, tree_level):
        print(" ", end="")
    print("#")
def make_tree_2():
    tree_height = 5
    spaces = tree_height - 1
    hashes = 1
    stump_spaces = tree_height - 1
    while tree_height != 0:
        for i in range(spaces):
            print(' ', end="")
        for i in range(hashes):
            print('#', end="")
        print()
        spaces -= 1
        hashes += 2
        tree_height -= 1
    for i in range(stump_spaces):
        print(' ', end="")
    print("#")
start_time = time.time()
make_tree()
print(f"{time.time() - start_time} seconds")
start_time = time.time()
make_tree_2()
print(f"{time.time() - start_time} seconds")
'''
import time
def make_tree():
    tree_level = 5
    n = 1  # n is the current tree level being printed
    while n <= tree_level:
        for i in range(1, tree_level - n + 1):
            print(" ", end="")
        for i in range(1, 2 * n):
            print("#", end="")
        n += 1
        print()
    for i in range(1, tree_level):
        print(" ", end="")
    print("#")
def make_tree_2():
    tree_height = 5
    spaces = tree_height - 1
    hashes = 1
    stump_spaces = tree_height - 1
    while tree_height != 0:
        for i in range(spaces):
            print(' ', end="")
        for i in range(hashes):
            print('#', end="")
        print()
        spaces -= 1
        hashes += 2
        tree_height -= 1
    for i in range(stump_spaces):
        print(' ', end="")
    print("#")
# made a float
start_time = float(time.time())
make_tree()
# I added more decimals to the output.
print(f"{float(time.time()) - start_time:.15f} seconds")
# added a pause
time.sleep(1)
# made a float
start_time = float(time.time())
make_tree_2()
# I added more decimals to the output.
print(f"{float(time.time()) - start_time:.15f} seconds")