print("How to create sets:")
set_1 = {9, 8, 7, 6}
set_2 = set({9, 8, 7, 6})

print(set_1)
print(set_2)

print("\nDuplicated values are automatically ignored:")
set_3 = {1, 1, 2, 2, 3, 3, 4, 4}
set_4 = set({1, 1, 2, 2, 3, 3, 4, 4})

print(set_3)
print(set_4)

print(
    "\nOrder of the items displayed in the output may differ from the order of the editor, because sets are unordered.")

print("\nOnly the odd numbers from 1 to 12:")
set_range = set(range(1, 12, 2))  # only the odd numbers from 1 to 12
print(set_range)

print("\nSet with mixed item types:")
set_mixed = {"a", 3.14, 18, True}
print(set_mixed)

print("\nUsing a loop over a set, returns an ordered list:")
set_loop = {3, 5, 7, 8, 2, 6, 9}
for num in set_loop:
    print(num)

print("\nCheck if an item is within a set:")
print(3 in set_loop)
print(10 in set_loop)

print("\nUsing a set created from a list, with duplicated values, that are automatically removed for the set:")
list_cities = ["Ribeirão Preto", "São Paulo", "Rio de Janeiro", "São Paulo", "Campinas", "São José dos Campos",
               "Ribeirão Preto", "São Carlos", "Ribeirão Preto"]
set_cities = set(list_cities)
print("List: " + str(list_cities))
print("Length of the list: " + str(len(list_cities)))
print("Set: " + str(set_cities))
print("Length of the set: " + str(len(set_cities)))
list_cities = list(set_cities)
print("List: " + str(list_cities))
print("Length of the list: " + str(len(list_cities)))
