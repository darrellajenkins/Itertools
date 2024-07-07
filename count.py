from itertools import count


for yes in count(-5, .5):
    print(yes)
    if yes >= 2:
        break
print()

mountain = map(lambda x: x ** 2, count())
for num in mountain:
    if num > 30:
        break
    print(num)
