ints = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

print(ints[::3])  # stride length of 3 (steps 3) = 1,4,7,10
print(ints[1::2])  # evens only (steps 2) = 2,4,6,8,10
print(ints[7::-1])  # backwards from 8 (steps -1) = 8,7,6,5,4,3,2,1
print(ints[8::-2])  # odds only backwards (steps -1) = 9,7,5,3,1
