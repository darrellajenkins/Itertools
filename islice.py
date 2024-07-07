from itertools import islice, count


abc = 'A B C D E F G H I J K L'
c = abc.split()

print(c[2:8:2])

print(list(islice(c, 2, 8, 2)))

# An infinite iterator
numbers = count()

# This would run forever if we tried to materialize it into a list
# print(list(numbers)[1000:1005])  # This would not work

# islice works fine with the infinite iterator
print(list(islice(numbers, 1000, 1005)))


def large_file_reader():
    for i in range(1000000):  # Simulating reading a large file
        yield f"Line {i}"

# Regular slicing would require loading all lines into memory
# print(list(large_file_reader())[10000:10005])  # Memory intensive


# islice processes only the required elements
print(list(islice(large_file_reader(), 10000, 10005)))

