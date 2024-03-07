print("one argument")
one_argument = range(5)

for num in one_argument:
    print(num)

print(type(one_argument))

print("two arguments")
two_arguments = range(5,10)

for num in two_arguments:
    print(num)

print(type(two_arguments))

print("three arguments")
three_arguments = range(1, 20, 3)

for num in three_arguments:
    print(num)

print(type(three_arguments))

print("three arguments decrease")
three_arguments_decrease = range(20, 1, -3)

for num in three_arguments_decrease:
    print(num)

print(type(three_arguments_decrease))