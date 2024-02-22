# Comparison operators
# >
# <
# >=
# <=
# !=
# ==

print(4 > 2)  # True
print(1 > 3)  # False
print(9 >= 9)  # True
print(1 <= 2)  # True
print(2 <= 2)  # True
print(10 != 100)  # True
print(10 != 10)  # False
print(10 == 100)  # False
print(10 == 10)  # True
print("hello" == "hello")  # True
print("hello" != "world")  # True
print(4.0 == 4)  # True
print(type(4.0) == type(4))  # False

# Boolean operators: and, or, not
print("Boolean operators: and, or, not")

print(not (1 == 1))
print(1 == 1 and 2 == 2)
print(1 == 1 and 2 == 1)
print(1 == 1 or 2 == 1)
print(not (1 == 1 and 2 == 1))
print(True)
print(not True)