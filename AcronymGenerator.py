# Convert to Acronym: Random Access Memory
# RAM

sentence = input("Convert to Acronym: ")

words = sentence.split()

for word in words:
    print(word[0].upper(), end="")
