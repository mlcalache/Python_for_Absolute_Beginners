print("Example")

counter = 0

while counter < 3:
    print(counter)
    counter += 1

print("Exercise")

exercise = 10

while exercise > 0:
    print(exercise)
    exercise -= 1

print("Challenge")

user_input = int(input("Enter a positive integer"))
counter = user_input
sum = 0
while counter > 0:
    sum += counter
    counter -= 1

print("User input was " + str(user_input))
print("Sum found by the while loop is " + str(sum))
