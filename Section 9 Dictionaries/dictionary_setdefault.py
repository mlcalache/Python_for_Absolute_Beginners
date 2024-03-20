var_1 = {"a": 1, "b": 2, "c": 3}

if "d" not in var_1:
    var_1["d"] = 4

print(var_1)

var_1 = {"a": 1, "b": 2, "c": 3}

var_1.setdefault("d", 4)  # if it does not exist, it adds

print(var_1)

var_1.setdefault("d", 5)  # key d already exists, and it does NOT change from 4 to 5

print(var_1)

var_1.setdefault("a", 1)  # the key a already exists, therefore the value is unchanged (still 1)

print(var_1)
