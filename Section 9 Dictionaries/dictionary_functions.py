print("\n---\nkeys():\n")

birth_years = {1985: "matheus", 1987: ["marcela", "camila"], 2000: "whatever"}
print(birth_years[1985])
print(birth_years[1987])
print(birth_years[2000])

print()
print(birth_years.keys())

print("\n---\nPrint keys without the keys():\n")
for k in birth_years:
    print(k)

print("\n---\nPrint keys with keys():\n")
for k in birth_years.keys():
    print(k)

print("\n---\nvalues():\n")
print(birth_years.values())
for v in birth_years.values():
    print(v)

print("\n---\nitems():\n")
print(birth_years.items())  # This returns tuples
print(birth_years)

print("\n---\nfor loop using items() to get the tuples:\n")
for key, value in birth_years.items():
    print(key, value)

print("\n---\nChecking the types of keys(), values(), and items():\n")
print(type(birth_years.keys()))
print(type(birth_years.values()))
print(type(birth_years.items()))

print("\n---\nConverting keys(), values(), and items() to a list:\n")
print(list(birth_years.keys()))
print(list(birth_years.values()))
print(list(birth_years.items()))

print(type(list(birth_years.keys())))

print("\n---\nUsing in and not in with keys() and values():\n")
print("matheus" in birth_years.values())
print("joão" not in birth_years.values())
print(1985 in birth_years.keys())
print(1985 in birth_years)

print("\n---\nUsing get():\n")
if 1975 in birth_years:
    print(birth_years[1975])
else:
    print("1975 is not found")

print(birth_years.get(1975, "1975 is not found"))

print("\n---\nDictionaries are copied as references and not values:\n")

birth_years = {1985: "matheus", 1987: ["marcela", "camila"], 2000: "whatever"}

people = birth_years
people[2000] = "test"
print(people)
print(birth_years)

birth_years = {1985: "matheus", 1987: ["marcela", "camila"], 2000: "whatever"}

people = birth_years.copy()

people[2000] = "test"
print(people)
print(birth_years)

# Make it 'more' readable with breaking the lines

birth_years = {1985: "matheus",
               1987: [
                   "marcela",
                   "camila"
               ],
               2000: "whatever"}

print("\n---\nlen():\n")
print(len(birth_years))
