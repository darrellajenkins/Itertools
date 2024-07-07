from itertools import product as prod


animals = ['camels', 'dogs', 'pigeons']
locations = ["Brookfield", "Woodland Park"]

print(list(prod(animals, locations)))
print()


animales = ['camels', 'dogs', 'pigeons']
print(list(prod(animales, repeat=2)))
