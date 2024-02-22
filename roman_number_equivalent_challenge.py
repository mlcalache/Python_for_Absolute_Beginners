# For this exercise, start by creating a variable and
# assigning it a randomly generated integer between and inclusive of both 1 and 10.
#
# Then, using your knowledge of if, elif, and else statements,
# create a program which prints the roman numeral equivalent of the randomly generated number.
#
# For example, if the randomly generated integer was 9,
# then the program would say that the roman numeral equivalent of 9 is IX in the output.
from random import randint

random_int = randint(1, 10)
print(random_int)

if random_int == 1:
    print("I")
elif random_int == 2:
    print("II")
elif random_int == 3:
    print("III")
elif random_int == 4:
    print("IV")
elif random_int == 5:
    print("V")
elif random_int == 6:
    print("VI")
elif random_int == 7:
    print("VII")
elif random_int == 8:
    print("VIII")
elif random_int == 9:
    print("IX")
else:
    print("X")
