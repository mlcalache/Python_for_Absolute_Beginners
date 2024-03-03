the_string = "North Dakota"
aux1 = the_string.rjust(17)

print(aux1)

aux2 = the_string.ljust(17, "*")

print(aux2)

center_plus = the_string.center(16, "+")

print(center_plus)

aux3 = the_string.lstrip("North")

print(aux3)

aux4 = center_plus.rstrip("+")

print(aux4)

aux5 = center_plus.strip("+")

print(aux5)

aux6 = the_string.replace("North", "South")

print(aux6)
