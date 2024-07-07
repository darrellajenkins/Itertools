from itertools import cycle

colors = cycle(['red', 'green', 'blue'])
for i in range(10):
    print(next(colors))  # Will print red, green, blue, red, green, blue, ...


# Creating cycling iterators for custom classes:
class CircularBuffer:
    def __init__(self, data):
        self.data = cycle(data)

    def next(self):
        return next(self.data)


nums = [1, 3, 7, 4, 9]
cycled = cycle(nums)
count = 0
for num in cycled:
    print(num, end=' ')
    count += 1
    if count >= 15:
        break
