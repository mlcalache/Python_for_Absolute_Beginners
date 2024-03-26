from functools import reduce


def make_sum(x, y):
    return x + y


list_1 = [1, 2, 3, 4, 5]

result_sum = reduce(make_sum, list_1)

print(result_sum)
