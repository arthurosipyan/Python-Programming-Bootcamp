import re

rand_str = "12345 12345-1234 1234 12346-333"
regex = re.compile(r"(\d{5}-\d{4}|\d{5}\s)")
matches = re.findall(regex, rand_str)

print(len(matches))

for i in matches:
    print(i)
