import itertools


a = ("Spring", [21.22, 30.66, 55.84, 447.99, 682.22])
b = ("Humble", [229.64, 330.99, 55.84])

spring = list(
    itertools.filterfalse(lambda x: x < 400, a[1]))  # filter removes everything specified, keeping the opposite
humble = list(itertools.filterfalse(lambda x: x < 400, b[1]))

spring_len = len(spring)
humble_len = len(humble)

if spring_len <= 0:
    print(f"The {a[0]} store did not sell any high-ticket items in the last quarter.")
else:
    print(f"The {a[0]} store sold {spring_len} high-ticket items in the last quarter.")

if humble_len <= 0:
    print(f"The {b[0]} store did not sell any high-ticket items in the last quarter.")
else:
    print(f"The {b[0]} store sold {humble_len} high-ticket items in the last quarter.")
