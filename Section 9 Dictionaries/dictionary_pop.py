ex_1 = {"make": "Honda", "model": "Civic", "year": 2016}
print(ex_1)
popped = ex_1.pop("model")
print(ex_1)
print(popped)

# popped = ex_1.pop("type")  # gives an error, as type does not exist

ex_1 = {"make": "Honda", "model": "Civic", "year": 2016}
print(ex_1)
popped = ex_1.popitem()  # pops the last item (tuple)
print(ex_1)
print(popped)
