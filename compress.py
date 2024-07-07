from itertools import compress


foods = ['mashed potatoes', 'mac n cheese', 'pizza', 'seafood', 'ribeye', 'filet mignon', 'fish cakes', 'pie',
         'cobbler', 'flan']
my_foods = list(compress(foods, [0, 0, 1, 1, 1, 0, 0, 1, 1, 0]))

print(my_foods)
