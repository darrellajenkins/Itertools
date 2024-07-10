from itertools import product as prod
from itertools import product


animals = ['camels', 'dogs', 'pigeons']
locations = ["Brookfield", "Woodland Park"]

print(list(prod(animals, locations)))
print()


animales = ['camels', 'dogs', 'pigeons']
print(list(prod(animales, repeat=2)))

hours = ["12", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11"]
mins = ['00', '15', '30', '45']
times = list(product(hours, mins))

for part in ['AM', 'PM']:
    for a, b in times:
        print(f"{a}:{b}{part}")
      
