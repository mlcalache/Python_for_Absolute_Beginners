penne = 16.68
pasta_sauce = 6.98
garlic_gloves = 16.78
italian_seasoning = 15.26
artisan_baguettes = 3.00
bag_of_meatballs = 4.39

sum_of_items = penne + pasta_sauce + garlic_gloves + italian_seasoning + artisan_baguettes + bag_of_meatballs

print(sum_of_items)
print(round(sum_of_items, 2))

# Variables holding the prices of the six items:

# All the variables were multiplied by 100 to make them into integers so that there would be no approximation errors
# when they were added together.

pasta = 16.68 * 100  # penne 16 oz, pack of 12
sauce = 6.98 * 100  # Arrabbiata sauce 24oz
garlic = 16.78 * 100  # 20 pack garlic clove
seasoning = 15.26 * 100  # Italian Seasoning
bread = 3.00 * 100  # Baguette twin pack
meatballs = 4.39 * 100  # 12 oz bag of meatballs
# subtotal is the sum of all prices before any sales taxes or discounts are added
subtotal = (pasta + sauce + garlic + seasoning + bread + meatballs) / 100
print(subtotal)
