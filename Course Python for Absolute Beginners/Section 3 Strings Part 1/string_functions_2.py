print("#-#-#-#-#")
x1 = "hello world"
x2 = x1.rjust(15)
x3 = x1.ljust(15)

print(x1)
print(x2)
print(x3)
print(x3 + "four spaces later.")

print("#-#-#-#-#")
x4 = x1.rjust(15, "-")
x5 = x1.ljust(14, "-")

print(x4)
print(x5)

print("#-#-#-#-#")
x6 = x1.center(15)

print(x6)

print("#-#-#-#-#")
x7 = x1.center(15, "-")

print(x7)

print("#-#-#-#-#")
y1 = "  hello world  "
y2 = y1.strip()
y3 = y1.rstrip()
y4 = y1.lstrip()

print(y1)
print(y2)
print(y3)
print(y4)

print("#-#-#-#-#")
z1 = "--hello world--"
z2 = z1.strip("-")
z3 = z1.rstrip("-")
z4 = z1.lstrip("-")

print(z1)
print(z2)
print(z3)
print(z4)

print("#-#-#-#-#")
w1 = "hello world! world"
w2 = w1.rstrip("world").strip()
w3 = w1.rstrip(" rldow")

print(w1)
print(w2)
print(w3)

print("#-#-#-#-#")
t1 = "juice, bread, cheese, beef, bread, bread"
t2 = t1.rstrip(", edarb")

print(t1)
print(t2)

print("#-#-#-#-#")
r1 = "blueblueyellowblue"
r2 = r1.strip("eubl")

print(r1)
print(r2)

print("#-#-#-#-#")
s1 = "matheus de lara calache"
s2 = s1.replace(" de lara", "")

print(s1)
print(s2)
