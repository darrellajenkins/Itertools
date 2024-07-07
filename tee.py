from itertools import tee


keen = ['commander', 'ray', 'music', 'green', 'yellow', 'precursor']
keen_a, keen_b = tee([keen])

print(keen_a, keen_b)
print()


for k in keen_a:
    print(k)

for e in keen_b:
    print(e)
