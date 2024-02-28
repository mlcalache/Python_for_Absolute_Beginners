user_input = int(input("enter a positive integer"))
counter = user_input
factorial = 1

while counter > 0:
    factorial *= counter
    counter -= 1

print("factorial of " + str(user_input) + " is " + str(factorial))
