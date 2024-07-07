import itertools


a, b, c = 'abc', 'def', 'ghi'
print(list(itertools.chain(a, b, c)))

dog = [5, 4, 6, 8, 5, 4, 5], [5, 4, 8, 7, 8], ['ice cream', 'cake', 'hot chocolate']

print(list(itertools.chain(*dog)))

print(list(itertools.chain(dog)))
