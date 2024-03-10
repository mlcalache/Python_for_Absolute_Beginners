example_list_1 = [5, 4, 3, 2, 1]
example_list_2 = [True, False, True, False]
example_list_3 = [1.0, 2.0, 3.0]
example_list_4 = ["Matheus", "de Lara", "Calache"]
example_list_5 = [["a", "b", "c"], ["d", "e", "f"], ["g", "h"]]
example_list_6 = [True, 1, "a", [2, False], "b", 2.0]

print(example_list_1)
print(example_list_2)
print(example_list_3)
print(example_list_4)
print(example_list_5)
print(example_list_6)

print(list("blah"))

print(1 in example_list_1)  # True
print(6 in example_list_1)  # False
print(1 not in example_list_1)  # False
print(6 not in example_list_1)  # True

# Exercise #
print("\n---")
print("Exercise")
var_1 = [1, 1.0, True, "a", [2, 3, 4]]
var_2 = list("Matheus")
e_in = "e" in var_2
print("Char 'e' in: " + str(e_in))
a_not_in = "a" not in var_2
print("Char 'a' not in: " + str(a_not_in))

# Access by index #
print("\n---")
print("Access by index")
index_list_1 = [["a", "b", "c"], ["d", "e", "f"], ["g", "h", "i"]]
print(index_list_1[2][0])  # g
index_list_2 = ["Matheus", "de Lara", "Calache"]
print(index_list_2[-1][0])  # C
print(index_list_1[-1][-1])  # i
print(index_list_1[-1][-2])  # h
print(index_list_1[-1][-3])  # g
print(index_list_1[-2][-1])  # f

# Slicing Lists #
print("\n---")
print("Slicing lists")
list_slice = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list_slice[:4])
print(list_slice[3:8])
print(list_slice[6:])

# Reassigning values in lists #
print("\n---")
print("Reassigning values in lists")
reassign_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(reassign_list)
reassign_list[0] = 0
print(reassign_list)
reassign_list[4:7] = [10, 11, 12]
print(reassign_list)

index = 0
for n in reassign_list:
    # print(n)
    reassign_list[index] = index
    index += 1
print(reassign_list)
