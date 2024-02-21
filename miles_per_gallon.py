import random
from math import floor

tank_gallons = random.randint(10, 25)
car_miles = random.randint(200, 400)


#  the formula miles per gallon (MPG) = miles driven/gallons used

def miles_per_gallon(g, m):
    return floor(m / g)


print("Car tank holds " + str(tank_gallons) + " gallons.")
print("Car travels " + str(car_miles) + " miles with a full tank.")
print("Car can travel " + str(miles_per_gallon(tank_gallons, car_miles)) + " miles per gallon.")
