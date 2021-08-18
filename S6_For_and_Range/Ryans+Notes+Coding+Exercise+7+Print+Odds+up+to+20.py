'''
Print Odds up to 20
To solve this problem print out all off values from 1 up to 20 on separate lines
'''

for i in range(1,21):
    # odd is when the modulus of 2 is equal to 1
    # even is when the modulus of 2 is equal to 0
    if i % 2 == 1:
        print(i)
