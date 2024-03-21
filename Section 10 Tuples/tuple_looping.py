cities = ("Ribeirão Preto", "São Paulo", "Campinas", "São Carlos", "São José dos Campos", "Guarujá")

print("\nUsing a for:")
for city in cities:
    print(city)

print("\nUsing a while:")
count = 0
while count < len(cities):
    print(cities[count])
    count += 1

print("\nUsing a while backwards:")
backwards_count = len(cities) - 1
while backwards_count >= 0:
    print(cities[backwards_count])
    backwards_count -= 1
