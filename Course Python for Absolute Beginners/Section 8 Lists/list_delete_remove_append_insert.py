planets = ["pluto", "mars", "earth", "venus"]
print(planets)
del planets[0]  # pluto is deleted
print(planets)

planets = ["pluto", "mars", "earth", "venus"]
print(planets)
planets.remove("pluto")  # pluto is removed
print(planets)
# planets.remove("saturn")  # an error message is displayed, because 'saturn' is not in the list

colors = ["blue", "red", "white", "blue", "orange", "blue"]
print(colors)
colors.remove("blue")  # only the first instance of 'blue' is removed
print(colors)

pets = ["cat", "dog", "parrot"]
print(pets)
pets.append("fish")
print(pets)

pets = ["cat", "dog", "parrot"]
pets.insert(1, "turtle")
print(pets)
