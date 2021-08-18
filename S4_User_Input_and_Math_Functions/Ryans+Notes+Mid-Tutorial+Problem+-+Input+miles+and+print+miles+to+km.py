# Asks the user to input the number of miles
miles = input("Number of miles: ")
# You'll convert miles to kilometers (kilometers = miles * 1.60935)
miles = float(miles)
kilometers = miles * 1.60935
# Then print this example 5 miles equals 8.0467 kilometers
print("{} miles equals {} kilometers".format(miles,kilometers))