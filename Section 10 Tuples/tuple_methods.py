print("Access properties within the tuple by their indexes:")
nested = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
print(nested)
print(nested[1])  # (4,5,6)
print(nested[1][2])  # 6

nested = (1, 2, 3, (4, 5, 6), (7, 8, 9))
print(nested)
print(nested[1])  # 2
# print(nested[1][2])  # error

print("\nUsing the count to check how many times an item repeats within the tuple:")
repeat = (1, 2, 3, 3, 3, 2, 1, 2, 3, 2, 1)
print("Number 1 appears " + str(repeat.count(1)) + " times")
print("Number 2 appears " + str(repeat.count(2)) + " times")
print("Number 3 appears " + str(repeat.count(3)) + " times")
print("Number 0 appears " + str(repeat.count(0)) + " times")

print("\nUsing the index method to get the position of an item within the tuple:")
ints = (1, 1, 1, 2, 3, 4, 5, 6, 7, (8, 9, 10))
print("Index of item 7 is " + str(ints.index(7)))  # 8
print("Index of item 2 is " + str(ints.index(2)))  # 3
print("Index of item 1 is " + str(ints.index(1)))  # 0
# print("Index of item 9 is " + str(ints.index(9)))  # error, item 9 does not exist
print("Index of item (8, 9, 10) is " + str(ints.index((8, 9, 10))))  # 9
