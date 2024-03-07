def get_number_words(arg1):
    words = arg1.split(" ")
    return len(words)


count = get_number_words("Isto é um teste")
print(count)

count = get_number_words("matheus")
print(count)

str_1 = "James Bond is 007."
str_2 = "When the moon hits your eye like a big pizza pie, that's amore!"
str_3 = "Anyway, like I was sayin', shrimp is the fruit of the sea. You can barbecue it, boil it, broil it, bake it, \
saute it. Dey's uh, shrimp-kabobs, shrimp creole, shrimp gumbo. Pan fried, deep fried, stir-fried. There's pineapple \
shrimp, lemon shrimp, coconut shrimp, pepper shrimp, shrimp soup, shrimp stew, shrimp salad, shrimp and potatoes, \
shrimp burger, shrimp sandwich. That- that's about it."

count = get_number_words(str_1)
print(count)
count = get_number_words(str_2)
print(count)
count = get_number_words(str_3)
print(count)
