arctic_animals = ["penguin", "polar bear", "walrus", "reindeer"]
print(arctic_animals)

# By reference
print("\n---")
print("Change by reference")
aux = arctic_animals
aux[2] = "polar bear with lasers"
print(arctic_animals)
print(aux)

# By value
print("\n---")
print("Change by value")
aux = arctic_animals.copy()
aux[1] = "penguin with lasers"
print(arctic_animals)
print(aux)

# copy.deepcopy
print("\n---")
print("copy.deepcopy")
import copy

arctic_animals = ["penguin", "polar bear", "walrus", "reindeer"]
aux = copy.deepcopy(arctic_animals)
aux[1] = "polar bear with lasers"
print(arctic_animals)
print(aux)
