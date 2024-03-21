print("Set add:")
scifi = {"Star Trek", "Star Wars", "Halo"}
scifi.add("Mass Effect")
print(scifi)

scifi.add("Star Wars")  # nothing happens, since Star Wars already exists
scifi.add("star wars")  # star wars is added because it is all in lower case (case sensitive)

print(scifi)

print("\nSet remove:")
scifi.remove("star wars")
# scifi.remove("test")  # error, as test does not exist in the set

print(scifi)

print("\nSet discard:")
scifi.discard("test")  # nothing happens, even though test does not exist in the set
scifi.discard("Mass Effect")

print(scifi)

scifi_copy = scifi.copy()
scifi_reference_copy = scifi

print(scifi_copy)
print(scifi_copy is scifi)  # False
print(scifi_reference_copy is scifi)  # True

scifi.clear()

print(scifi)  # Empty set because of clear()
print(scifi_reference_copy)  # This is also empty

print("\nSet union:")
set_1 = {1, 2, 3, 4, 5}
set_2 = {6, 7, 8, 9, 10}
set_3 = set_1.union(set_2)
print(set_1)
print(set_2)
print(set_3)
set_3.clear()
print(set_3)
set_3 = set_1 | set_2  #
print(set_3)

print("\nSet intersection:")
set_4 = {1, 2, 3, 6}
set_5 = {3, 4, 5, 6}
set_6 = set_4.intersection(set_5)  # 3, 6
print(set_4)
print(set_5)
print(set_6)  # 3, 6
set_6.clear()
print(set_6)
set_6 = set_4 & set_5  # also an intersection = 3, 6
print(set_6)

print("\nSet subtraction:")
set_7 = {4, 5, 6, 7, 8}
set_8 = {6, 7, 8, 9, 10}
set_9 = set_8 - set_7
print(set_7)
print(set_8)
print(set_9)

print("\nSet difference:")
set_10 = {4, 5, 6, 7, 8}
set_11 = {6, 7, 8, 9, 10}
set_12 = set_10.difference(set_11)  # 4, 5
print(set_10)
print(set_11)
print(set_12)
set_12 = set_11.difference(set_10)  # 9, 10
print(set_12)
