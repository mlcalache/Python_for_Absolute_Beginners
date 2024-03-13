ex_1 = {}.fromkeys(["address"], "Piet Heinkade 167")  # one key+value is created: key address
print(ex_1)
ex_2 = {}.fromkeys("ad", "Piet Heinkade 167")  # two key+value are created: keys a and d
print(ex_2)
ex_3 = {}.fromkeys("addr",
                   "Piet Heinkade 167")  # d is only used once, thus three key+value are created: keys a, d, and r
print(ex_3)
ex_4 = {}.fromkeys(["address"])  # creates one key "address" with no value
print(ex_4)
