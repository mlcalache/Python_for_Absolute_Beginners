def calculate_factorial(number):
    if number == 0:
        factorial = 1
    else:
        counter = number
        factorial = 1

        while counter > 0:
            factorial *= counter
            counter -= 1

    print("factorial of " + str(number) + " is " + str(factorial))

    return factorial


user_input = int(input("enter a positive integer"))
calculate_factorial(user_input)

calculate_factorial(0)
calculate_factorial(1)
calculate_factorial(3)
calculate_factorial(4)
calculate_factorial(5)
