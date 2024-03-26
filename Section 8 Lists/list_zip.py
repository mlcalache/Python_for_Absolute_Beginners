list_1 = [1, 2, 3, 4, 5]
list_2 = ["apple", "orange", "pear", "tomato", "grape"]
list_3 = [1.5, 1.75, 1.99, 0.89, 3.5]

for number, fruit in zip(list_1, list_2):
    print(number, fruit)

for number, fruit, price in zip(list_1, list_2, list_3):
    print(number, fruit, price)
