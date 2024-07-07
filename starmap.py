from itertools import starmap


# STARMAP IS NOT LIKE REGULAR MAP

data = [108, 20236, 3002, 4420]
print(list(starmap(max, [data])))
print()

# Compare to MAP:

z = lambda x: x ** 2
result1 = map(z, [1, 2, 3, 4])
print(list(result1))  # prints a list of squares from a given list

zeta = lambda x, y: x + y
result2 = map(zeta, [1, 2, 3, 4], [5, 6, 7, 8])
print(list(result2))  # print a list of numbers that are the sum of 2 given lists

et = lambda e, t: (e ** 2, t ** 2)
result3 = map(et, [1, 2, 3, 4], [5, 6, 7, 8])
print(list(result3))

dc = lambda d, c: (d ** 2 + c ** 2)
result4 = map(dc, [1, 2, 3, 4], [5, 6, 7, 8])
print(list(result4))
