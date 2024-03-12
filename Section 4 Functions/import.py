# generic import
import random

var_1 = random.randint(1, 10)  # between (including) 1 and 10
print(var_1)
print(random.randint(1, 10))
print(random.randint(1, 10))
print(random.randint(1, 10))


# import a function from a module
from random import randint

print(randint(1, 10))


# universal import
from random import *

print(random())
print(randint(1,10))
