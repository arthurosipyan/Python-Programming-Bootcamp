# a - z 97 - 122
# A - Z 65 - 90

# Enter string: DOG
# DOG = 687971
# 687971 = DOG

norm_string = input("Enter string: ")
secret_string = ""

for char in norm_string:
    secret_string += str((ord(char) - 23))

print("Secret Message:", secret_string)

norm_string = ""

for i in range(0, len(secret_string)-1, 2):
    char_code = secret_string[i] + secret_string[i+1]
    norm_string += chr(int(char_code) + 23)

print("Original Message:", norm_string)
