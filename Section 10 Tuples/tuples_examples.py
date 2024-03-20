tuple_1 = ("a", "b", "c", "d", "e")
tuple_2 = (2.123, False, [1, 2, 3])
tuple_3 = (1, 1, 0, 0, 0)

tuple_4 = tuple([3.14, 2.205, 10])
tuple_5 = tuple("abcde")

print(tuple_4)
print(tuple_5)

tuple_6 = tuple({"a": 1, "b": 2, "c": 3})  # only the keys will be made into a tuple
print(tuple_6)

# Slicing tuples

print("\nSlicing tuples")
tuple_7 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(tuple_7[2])
print(tuple_7[:8])
print(tuple_7[2:7])
print(tuple_7[3:])

# tuple_7[0] = 0  # error... tuples do not support item assignment. tuples are immutable


# use tuples for data that does not change, e.g., days of the week, alphabet, seasons, etc.
tuple_week_days = ("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday")
tuple_seasons = ("Winter", "Sprint", "Summer", "Fall")

# size (bytes) of lists vs tuples

tuple_size = (1, 2, 3)
list_size = [1, 2, 3]
print(tuple_size.__sizeof__())  # 48
print(list_size.__sizeof__())  # 72
