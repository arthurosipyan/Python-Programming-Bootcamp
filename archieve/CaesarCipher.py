# 1. Receive a message and then encrypt it by shifting the
# characters by a requested amount to the right.

# A becomes D, B becomes E, for example. Also, decrypt the message back.

# HINTS

# 1. A-Z have the numbers 65-90 in unicode
# 2. a-z have the numbers 97-122
# 3. You get the unicode of a character with ord(yourLetter)
# 4. You covert from unicode to character with chr(yourNumber)
# 5. Use isupper() to decide which unicode to work with
# 6. Add the key (number of characters to shift)... if bigger or smaller then
# the unicode for A, Z, a, or z increase or decrease by 26

message = input("Enter your message: ")
key = int(input("How many characters should we shift (1-26): "))
secret_message = ""

for char in message:
    if char.isalpha():
        char_code = ord(char) + key

        if char.isupper():
            if char_code > ord("Z"):
                char_code -= 26
            elif char_code < ord("A"):
                char_code += 26
        else:
            if char_code > ord("z"):
                char_code -= 26
            elif char_code < ord("a"):
                char_code += 26
        secret_message += chr(char_code)
    else:
        secret_message += char
print("Encrypted:", secret_message)

original_message = ""
key = -key

for char in secret_message:
    if char.isalpha():
        char_code = ord(char) + key

        if char.isupper():
            if char_code > ord("Z"):
                char_code -= 26
            elif char_code < ord("A"):
                char_code += 26
        else:
            if char_code > ord("z"):
                char_code -= 26
            elif char_code < ord("a"):
                char_code += 26
        original_message += chr(char_code)
    else:
        original_message += char

print("Decrypted: ", original_message)
