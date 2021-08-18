# While Loop

# While loops are used when you don't know how many times you will have to loop
# Here we’ll generate a random number with the random module and randrange()

# We can use the random module to generate random numbers
import random

# Generate a random integer between 1 and 50
rand_num = random.randrange(1, 51)

# The value we increment in the while loop is defined before the loop
i = 1

# Define the condition that while true we will continue looping
while i != rand_num:

    # You must increment your iterator inside the while loop
    i += 1

# Outside of the while loop when we stop adding whitespace
print("The random value is : ", rand_num)

# Break & Continue

# Continue stops executing the code that remains in the loop and jumps back to the top
# Break ends execution and jumps directly to the code that lies immediately outside of the loop

# Here we’ll cycle from 0 to 20 with a while loop
# If a number is even will use continue to skip printing it
# If it is odd we’ll print it
# We’ll then end execution with break if the value ever reaches 15

i = 1
while i <= 20:
    # If a number is even don't print it
    if (i % 2) == 0:
        i += 1
        continue

    # If i equals 15 stop looping
    if i == 15:
        break

    # Print the odds
    print("Odd : ", i)
    # Increment i
    i += 1

# Python Problem for you to Solve

# For this problem I want you to draw a pine tree after asking the user for the number of rows
# This problem is the most difficult you have had so far, but it will teach a lot

'''
Here is the sample program
 
How tall is the tree : 5
        #
       ###
      #####
     #######
    #########
        #
'''

# Tip 1 : You should use a while loop and 3 for loops
'''
Tip 2
I know that this is the number of spaces and hashes for the tree
4 - 1
3 - 3
2 - 5
1 - 7
0 - 9
Spaces before stump = Spaces before top
'''

'''
TIP 3

You will need to do the following in your program : 

1. Decrement spaces by one each time through the loop
2. Increment the hashes by 2 each time through the loop
3. Save spaces to the stump by calculating tree height - 1
4. Decrement from tree height until it equals 0
5. Print spaces and then hashes for each row
6. Print stump spaces and then 1 hash
'''

# Get the number of rows for the tree
tree_height = input("How tall is the tree : ")

# Convert into an integer
tree_height = int(tree_height)

# Get the starting spaces for the top of the tree
spaces = tree_height - 1

# There is one hash to start that will be incremented
hashes = 1

# Save stump spaces til later
stump_spaces = tree_height - 1

# Makes sure the right number of rows are printed
while tree_height != 0:
    # Print the spaces
    # end="" means a newline won't be added
    for i in range(spaces):
        print(' ', end="")

    # Print the hashes
    for i in range(hashes):
        print('#', end="")

    # Newline after each row is printed
    print()

    # I know from research that spaces is decremented by 1 each time
    spaces -= 1

    # I know from research that hashes is incremented by 2 each time
    hashes += 2

    # Decrement tree height each time to jump out of loop
    tree_height -= 1

# Print the spaces before the stump and then a hash
for i in range(stump_spaces):
    print(' ', end="")
print("#")


