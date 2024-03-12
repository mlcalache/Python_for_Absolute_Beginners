arctic_animals = ["penguin", "elephant", "polar bear", "walrus", "tiger", "reindeer"]
print(arctic_animals)

# remove the tiger with del
del arctic_animals[arctic_animals.index("tiger")]
print(arctic_animals)

# remove the elephant with remove
arctic_animals.remove("elephant")
print(arctic_animals)

# add arctic fox with append
arctic_animals.append("arctic fox")
print(arctic_animals)

# add snowy owl in between the polar bear and the walrus
arctic_animals.insert(arctic_animals.index("polar bear") + 1, "snowy owl")
print(arctic_animals)

# sort alphabetically
arctic_animals.sort()
print(arctic_animals)
reindeer_index = arctic_animals.index("reindeer")
print(reindeer_index)

popped_animal = arctic_animals.pop()
print(arctic_animals)
print(popped_animal)
