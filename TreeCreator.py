# How tall is the tree: 5

# |       #       4 - 1
# |      ###      3 - 3
# |     #####     2 - 5
# |    #######    1 - 7
# |   #########   0 - 9
# |       #       4 - 1

tree_height = int(input("How tall is the tree: "))
hashes = 1
stump = (" " * (tree_height-1) + "#")

while tree_height != 0:
    print(" " * (tree_height-1) + ("#" * hashes))
    tree_height -= 1
    hashes += 2
print(stump)
