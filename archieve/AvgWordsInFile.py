# Line 1
# Number of Words: 3
# Avg Word Length: 4.7
# Line 2
# Number of Words: 3
# Avg Word Length: 4.7

with open("myFile.txt", mode="w", encoding="utf-8") as my_file:
    my_file.write("Hello world\n"
                  "Godzilla is cool\n"
                  "Today is April 6th\n"
                  "This is a test for the python course on Udemy by Derak Banas")

with open("myFile.txt", encoding="utf-8") as my_file:
    line_num = 1
    while True:
        line = my_file.readline()
        if not line:
            break

        char_count = 0
        for word in line.split():
            char_count += len(word)

        print("Line {}: {}"
              "Number of Words: {}\n"
              "Avg Word Length: {}\n\n".format(line_num, line,
                                               len(line.split()),
                                               "{:.1f}".format(char_count / len(line.split()))))
        line_num += 1
