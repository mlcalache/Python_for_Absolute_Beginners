ex_1 = 'This is a string.'
ex_2 = "This is also a string."

# string index

ex_3 = "0123456"
character = ex_3[2]
print(character)  # 2

print("apple"[3])  # l

# string slicing

ex_4 = "apricots"

# [start at index : less than index]

print(ex_4[:3])  # apr
print(ex_4[2:5])  # ric
print(ex_4[4:])  # cots

print(ex_3[:3])  # 012
print(ex_3[2:5])  # 234
print(ex_3[4:])  # 456

# string concatenation

print("pecan" + " " + "pie")

concatenated = "R2" + "-" + "D2"
print(concatenated)  # R2-D2
print(concatenated[3])  # D
print(concatenated[1:4])  # 2-D

just = "Just do it!"
print(len(just))  # 11
print(just[len(just) - 1])  # !
print(just[5:7])  # do
slice_1 = just[8:]
print(slice_1)  # it!
slice_2 = just[:4]
print(slice_2)  # Just
slice_3 = just[5:]  # do it
print("Don't " + slice_3)  # Don't do it
