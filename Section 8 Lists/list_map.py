def make_double(x):
    return x * 2


values = [1, 2, 3, 4, 5]
doubled = map(make_double, values)

print(values)

list_doubled = list(doubled)

print(list_doubled)
