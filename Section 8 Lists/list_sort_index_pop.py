num_list = [2.718, 4, -19, 10000, 0]
print(num_list)
num_list.sort()
print(num_list)

beatles = ["Ringo", "John", "Paul", "George"]
print(beatles)
beatles.sort()
print(beatles)

num_list.sort(reverse=True)
print(num_list)

beatles.sort(reverse=True)
print(beatles)

mixed = [False, 5.67, "string", -2]
# mixed.sort()  # this given an error, because of the string that cannot be converted to a number.
# False is converted to 0.
del mixed[2]
mixed.sort()
print(mixed)

ascii_order = ["Andy", "kiwi", "apple", "Karen", "Brian", "banana"]
print(ascii_order)
ascii_order.sort()
print(ascii_order)
ascii_order.sort(key=str.lower)
print(ascii_order)

ascii_order = ["Andy", "kiwi", "apple", "Karen", "Brian", "banana"]
index = ascii_order.index("kiwi")
print(index)
# index = ascii_order.index("peanut")  # this will give an error, as 'peanut' is not in the list
# print(index)

list_x = [1, 2, 3, 4, 1, 2, 3, 4]
index = list_x.index(2)  # index is 1, since the first time the number 2 appears in the list is in index == 1
print(index)

list_bands = ["Iron Maiden", "Metallica", "Dream Theater", "Symphony X"]
print(list_bands)
band = list_bands.pop()  # Pops the last index
print(list_bands)
print(band)

list_bands = ["Iron Maiden", "Metallica", "Dream Theater", "Symphony X"]
print(list_bands)
band = list_bands.pop(2)  # Pops the index 2
print(list_bands)
print(band)
