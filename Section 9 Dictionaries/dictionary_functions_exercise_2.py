ex_1 = {}.fromkeys("BCDFGHJKLMNPQRSTVWXYZ", "consonant")
print(ex_1)

for key, value in ex_1.items():
    print(key, value)

fast_food_items = {"McDonald's": "Big Mac", "Burger King": "Whopper", "Chick-fil-A": "Original Chicken Sandwich"}
popped = fast_food_items.pop("McDonald's")
print(popped)
poppeditem = fast_food_items.popitem()
print(poppeditem)
print(fast_food_items)
