# key: value
consoles = {"nintendo": "wii",
            "microsot": "xbox",
            "sony": "playstation"}

print("\n---\nPrint consoles dictionary:\n")
print(consoles)

print("\n---\nPrint the value:\n")
print(consoles["nintendo"])

print("\n---\nPrint all keys with a loop:\n")
for x in consoles:
    print(x)

print("\n---\nPrint all values with a loop:\n")
for x in consoles:
    print(consoles[x])

# -----------------------

mohs_hardness = {9: "corundum", 10: "diamond"}
floats = {1.23: 1000, 3.14159: 10000, 2.718: 100000}
mixed = {"string": 1, 10210: 2, 4.977: 3, False: 4}

print("\n---\nPrint mohs_hardness with a loop:\n")
for x in mohs_hardness:
    print(x)
    print(mohs_hardness[x])

print("\n---\nPrint floats with a loop:\n")
for x in floats:
    print(x)
    print(floats[x])

print("\n---\nPrint mixed with a loop:\n")
for x in mixed:
    print(x)
    print(mixed[x])

# Dictionaries are unordered

print("\n---\nLists are ordered:\n")
print([1, 2, 3] == [1, 2, 3])
print([1, 2, 3] == [3, 2, 1])

print("\n---\nDictionaries are unordered:\n")
print({1: True, 2: True, 3: False} == {1: True, 2: True, 3: False})
print({1: True, 2: True, 3: False} == {3: False, 2: True, 1: True})

print("\n---\nCheck if exists with in or not in:\n")
first = {1: True, 2: True, 3: False}
# print(first[4])  # This given an error as the key '4' does not exist
print(0 in first)
print(1 in first)
print(4 not in first)
print(2 not in first)
