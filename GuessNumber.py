# Guess a number between 1 and 10: 1
# Guess a number between 1 and 10: 3
# Guess a number between 1 and 10: 5
# Guess a number between 1 and 10: 7
# You guessed it

secret_number = 5

while True:
    guess = int(input("Guess a number between 1 and 10: "))
    if guess == secret_number:
        print("You guessed it")
        break
