from itertools import accumulate, dropwhile, takewhile


# dropwhile: as soon as the opposite of the first condition has been met, EVERYTHING (REGARDLESS) else is included
a = ("Spring",
     [21.22, 30.66, 55.84, 447.99, 53.30, 96.36, 47.52, 330.45, 682.22, 11.25, 32.33, 62.12, 704.11, 55.30, 900.66,
      22.10, 12.30])
b = ("Humble",
     [229.64, 330.99, 55.84, 11.11, 47.25, 33.30, 68.27, 93.17, 21.10, 80.71, 3.36, 99.88, 102.31, 41.14, 54.77, 306.03,
      109.35])


def salesover_1000(store):
    """Creates list that begins with the next sale after the accumulated total of sales meets or exceeds $1000.
    Function input must be a tuple of the store name and a list of all sales. Return value is the store name,
    the list of the sales, and the sum of those sales.  In variable <aa> Since the list begins with the value
    that sent the accum total over 1000, we slice with the next value as the requirements of the contest
    stipulate all sales beginning with the next sale after $1000 has been met."""
    condition = lambda x: list(accumulate(store[1][:store[1].index(x) + 1]))[-1] < 1000
    aa = list(dropwhile(condition, store[1]))[1:]
    return store[0], aa, sum(aa)


s = salesover_1000(a)
print(f"{s[0]} qualifies for the matching donations over $1000. Their total after exceeding $1000 in"
      f" sales is ${s[2]:,.2f}!")
print()

h = salesover_1000(b)
print(f"{h[0]} qualifies for the matching donations over $1000. Their total after exceeding $1000 in"
      f" sales is ${h[2]:,.2f}!")
print()

# In the following example it is even more clear that dropwhile removes items meeting the condition but RETAINS all 
# subsequent items, even though some may meet the original condition.  Thus dropwhile is more of a trigger to 
# begin creating a new list.
words = ['dog', 'cat', 'pig', 'bat', 'mouse', 'horse', 'tiger', 'goat', 'ram', 'owl']
alpha = list(dropwhile(lambda x: len(x) < 4, words))
print(alpha)
print()

# takewhile: as soon as the opposite of the first condition has been met, EVERYTHING (REGARDLESS) else is excluded
sq = ("Seattle",
      [21.22, 30.66, 55.84, 447.99, 53.30, 96.36, 47.52, 330.45, 682.22, 11.25, 32.33, 62.12, 1704.11, 55.30, 900.66,
       22.10, 12.30])
pb = ("Portland",
      [229.64, 330.99, 55.84, 11.11, 47.25, 33.30, 68.27, 93.17, 21.10, 80.71, 3.36, 99.88, 1102.31, 41.14, 54.77,
       306.03, 109.35])


def small_tickets(store):
    """Creates a list of all small ticket item sales under $1000 sold prior to any large ticket item, which
    creates a stopping trigger of any sales over $1000. Function input must be a tuple of the store name and
    a list of all sales. Return value is the store name, the list of the sales, and the sum of those sales."""
    condition = lambda x: x < 1000
    aa = list(takewhile(condition, store[1]))
    return store[0], aa, sum(aa)


sq_under = small_tickets(sq)
print(f"{sq_under[0]} sold a total of ${sq_under[2]:,.2f} in small ticket items!")
print()

pb_under = small_tickets(pb)
print(f"{pb_under[0]} sold a total of ${pb_under[2]:,.2f} in small ticket items!")
print()

# A more simple example is provided below:
words = ['dog', 'cat', 'pig', 'bat', 'mouse', 'horse', 'tiger', 'goat', 'ram', 'owl']
beta = list(takewhile(lambda x: len(x) < 4, words))
print(beta)

"""Explanation for dropwhile above:
1. `condition = lambda x: list(accumulate(store[1][:store[1].index(x)+1]))[-1] < 1000`

This line defines a lambda function that serves as the condition for the `dropwhile` function. Let's break it down further:

   a. `lambda x:` creates an anonymous function that takes one parameter `x`.
   
   b. `store[1]` is the list of sales figures from the input tuple.
   
   c. `store[1].index(x)` finds the index of the current sales figure `x` in the list.
   
   d. `store[1][:store[1].index(x)+1]` slices the list from the beginning up to and including the current sales figure.
   
   e. `accumulate(...)` creates an iterator of cumulative sums of this slice.
   
   f. `list(...)` converts the iterator to a list.
   
   g. `[...][-1]` takes the last element of this list, which is the total cumulative sum up to the current sales figure.
   
   h. `< 1000` checks if this cumulative sum is less than 1000.

So, this condition returns `True` for each sales figure until the cumulative sum exceeds or equals 1000, and `False` afterwards.

2. `aa = list(dropwhile(condition, store[1]))[1:]`

This line uses the condition we just defined to process the list of sales figures:

   a. `dropwhile(condition, store[1])` creates an iterator that drops elements from `store[1]` as long as the `condition` is `True`.
   
   b. `list(...)` converts this iterator to a list.
   
   c. `[1:]` slices this list starting from the second element (index 1) to the end.

The reason for `[1:]` is that `dropwhile` will stop at the first element where the condition is `False`
(i.e., the first sale that makes the cumulative sum exceed or equal 1000). By taking `[1:]`, we exclude this
"threshold" sale and only keep the ones after it. In essence, these two lines together find the point at which
cumulative sales exceed $1000, and then create a new list (`aa`) of all sales figures after that point. This
approach ensures that the returned sales figures all occur after the $1000 threshold has been crossed, which
seems to be the qualification criteria for the matching donations program mentioned in the print statements."""
