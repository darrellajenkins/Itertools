from itertools import groupby as gby


for k, l in gby("AAABBBCCC"):
    print(list(l))
print()

devs = [('Scott', 34, 'Houston', 'B'), ('Sullivan', 23, 'Houston', 'A'), ('Marge', 41, 'Austin', 'C'),
        ('Howey', 39, 'Chicago', 'B'), ('Suzie', 23, 'San Francisco', 'B'), ('Dave', 41, 'Chicago', 'C'), 
        ('Sammie', 42, 'Rochester', 'A'), ('Katelynn', 34, 'Rochester', 'B'), 
        ('Tamika', 39, 'San Francisco', 'A'), ('Caity', 42, 'San Francisco', 'C')
        ]

age = lambda a: a[1]
city = lambda a: a[2]

devs.sort(key=age)  # This must be done first, outside of the groupby function

engineers = [list(d) for key, d in gby(devs, key=age)]
for eng in engineers:
    print(eng)
print()

# Use groupby and store results in a dictionary
age_groups = {key: list(d) for key, d in gby(devs, key=age)}

# Now you can access each group by age
print("Developers aged 23:")
print(age_groups[23])

print("\nDevelopers aged 34:")
print(age_groups[34])

# You can also iterate over all groups
for age, group in age_groups.items():
    print(f"\nAge {age}:")
    for dev in group:
        print(dev)
