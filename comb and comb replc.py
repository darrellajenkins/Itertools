from itertools import combinations as comb
from itertools import combinations_with_replacement as combrpl

print(list(comb('ABC', 2)))

print(list(comb('CBA', 2)))

print(list(combrpl(range(4), 3)))
