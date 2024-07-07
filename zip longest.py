from itertools import zip_longest


a = ['house', 'car', 'bike', '3000 acres', 'european condo']
b = [300_000, 25_000, 700]

c = zip_longest(a, b, fillvalue=f'{2_000_000:,}')
print(list(c))
print()

tasks = [1, 2, 3, 4, 5, 6, 7, 8]
workers = ['Alice', 'Bob', 'Charlie']

for task, worker in zip_longest(tasks, workers, fillvalue=workers[-1]):
    print(f"{worker} does task {task}")
