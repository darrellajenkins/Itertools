import itertools


# Pairwise will not behave in actual pairs as you would expect.
exams = ['Albert', 70, 'Eden', 56, 'Dara', 89, 'Brianna', 90, 'Amy', 77, 'Brian', 60, 'Carrie', 84, 'Flora', 62,
         'Glenn',
         65, 'Hailey', 74, 'Jenette', 80, 'Allison', 90, 'Katie', 81, 'Laura', 80, 'Susanna', 98, 'Shannon', 88]

for pair in itertools.pairwise(exams):
    print(pair)
print()

"""itertools.pairwise() is a function that takes an iterable and returns an iterator of overlapping pairs.
It creates pairs of adjacent elements in the input iterable. The function doesn't know or care about the
semantic meaning of the data; it just creates pairs based on the order of elements. The itertools.pairwise()
function is more commonly used for things like:
1. Calculating differences between adjacent elements in a sequence.
2. Processing overlapping windows of data.
3. Analyzing transitions between states in a sequence.
It's a general-purpose tool that can be very useful in certain scenarios,
but it may not be the best fit for every data structure or use case."""

# Here are some simple, practical examples of using itertools.pairwise():

temperatures = [20, 22, 25, 23, 24, 26]
temp_changes = [b - a for a, b in itertools.pairwise(temperatures)]
print("Temperature changes:", temp_changes)
# Output: Temperature changes: [2, 3, -2, 1, 2]

stock_prices = [100, 101, 102, 98, 97, 99, 103]
direction_changes = [
    "Up" if b > a else "Down" if b < a else "No change"
    for a, b in itertools.pairwise(stock_prices)
]
print("Price direction changes:", direction_changes)
# Output: Price direction changes: ['Up', 'Up', 'Down', 'Down', 'Up', 'Up']

word = "hello"
letter_pairs = list(itertools.pairwise(word))
print("Letter pairs:", letter_pairs)
# Output: Letter pairs: [('h', 'e'), ('e', 'l'), ('l', 'l'), ('l', 'o')]

monthly_sales = [
    ("Jan", 1000), ("Feb", 1200), ("Mar", 1100),
    ("Apr", 1300), ("May", 1250)
]
for (month1, sales1), (month2, sales2) in itertools.pairwise(monthly_sales):
    diff = sales2 - sales1
    print(f"{month1} to {month2}: {'Increase' if diff > 0 else 'Decrease'} of ${abs(diff)}")
# Output:
# Jan to Feb: Increase of $200
# Feb to Mar: Decrease of $100
# Mar to Apr: Increase of $200
# Apr to May: Decrease of $50

moves = ["up", "up", "left", "down", "right", "up"]
move_changes = [
    "Same" if a == b else "Changed"
    for a, b in itertools.pairwise(moves)
]
print("Move changes:", move_changes)
# Output: Move changes: ['Same', 'Changed', 'Changed', 'Changed', 'Changed']

