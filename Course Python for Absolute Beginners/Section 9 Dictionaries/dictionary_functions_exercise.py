aux = {
    "Queen": "Bohemia Rhapsody",
    "Bee Gees": "Stayin' Alive",
    "U2": "One",
    "Michael Jackson": "Billie Jean",
    "The Beatles": "Hey Jude",
    "Bob Dylan": "Like A Rolling Stone"
}

print("\nlen()")
print(len(aux))

print("\nkeys()")
for k in aux.keys():
    print(k)

print("\nvalues()")
print(aux.values())
for v in aux.values():
    print(v)

print("\nitems()")
for k, v in aux.items():
    print(k, v)

print("\nget()")
print(aux.get("Promise of the Real", "Promise of the Real is not found"))
