user_input = input("Please enter any string as input")

result = ""

three_arguments = range(len(user_input) - 1, -1, -1)

for index in three_arguments:
    result += user_input[index]

print(result)
