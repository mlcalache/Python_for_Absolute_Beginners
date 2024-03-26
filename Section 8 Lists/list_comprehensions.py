list_1 = [1, 2, 3, 4, 5]
list_2 = [i * 2 for i in list_1]  # double the values of the list

print(list_1)
print(list_2)

list_3 = [i * 2 for i in list_1 if i % 2 == 0]  # double the values of the list but only for the even ones

print(list_3)
