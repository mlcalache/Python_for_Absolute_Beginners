# F = 1.8 * C + 32

user_celsius = int(input("What is the temperature in Celsius?"))


def celsius_to_farenheit(c):
    return round(1.8 * c + 32, 1)


farenheit = celsius_to_farenheit(user_celsius)
print("The Fahrenheit equivalent of " + str(user_celsius) + " degrees Celsius is " + str(farenheit) + ".")
