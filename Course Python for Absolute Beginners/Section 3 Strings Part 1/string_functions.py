var1 = "Matheus"
print(var1)

# Upper and Lower functions
print(var1.upper())  # true
print(var1.lower())  # true
print(var1.isupper())  # false
print(var1.islower())  # false
print(var1.upper().isupper())  # true
print(var1.lower().islower())  # true
print("".isupper())  # false
print("".islower())  # false
print("37".isupper())  # false
print("37".islower())  # false
print("37".upper().isupper())  # false
print("37 test".upper().isupper())  # true
print("%$@\"".isupper())  # false
print("%$@\"".upper().isupper())  # false
print("%$@\" test".upper().isupper())  # true

# Alpha, numeric, decimal functions
print("matheus".isalpha())  # true
print("123".isalpha())  # false
print("123".isnumeric())  # true
print("matheus".isnumeric())  # false
print("1.0".isnumeric())  # false
print("1.0".isdecimal())  # false
print("1,0".isdecimal())  # false
print("Matheus123".isalnum())  # true

print("  ".isspace())  # true
print(" a     ".isspace())  # false
print(" a     "[2].isspace())  # true
print(" a     "[2:].isspace())  # true
print("Matheus De Lara Calache".istitle())  # true
print("Matheus De Lara Calache: Software Engineer".istitle())  # true

print("matheus de lara calache".title())
print("matheus de lara calache".title().istitle())  # true

# Starts with and Ends with
print("Matheus".startswith("Ma"))  # true
print("Matheus".startswith("ma"))  # false
print("Matheus".endswith("us"))  # true
print("Matheus".endswith("uS"))  # false

# Join
print("".join(["one", "two", "three"]))
print(" ".join(["one", "two", "three"]))
print(", ".join(["one", "two", "three"]))
print(" | ".join(["one", "two", "three"]))
print("...".join(["one", "two", "three"]))

# Split
print("One, Two, Three, Four".split())  # splits on space
print("One, Two, Three, Four".split(", "))
print("One|Two|Three|Four".split("|"))

# Length
print(len(var1))

# Exercise
print("Exercise:")
mixed_case = "A Song of Fire and Ice"
print(mixed_case.isupper())
print(mixed_case.islower())
print(mixed_case.upper())
print(mixed_case.lower())
print(mixed_case.istitle())
title_case = mixed_case.title()
print(title_case)
print(title_case.startswith(mixed_case[0]))
print(title_case.endswith(mixed_case[len(mixed_case) - 1]))
print(mixed_case[len(mixed_case) - 1])
var_words = mixed_case.split()
print(var_words)
aux_join = "".join(var_words)
print(aux_join)
print(aux_join.isalpha())
