# python permutation
# 1. 순열
from itertools import permutations

a = [1,2,3]
permute = permutations(a, 2)

print(list(permute))

# 2. 조합

from itertools import combinations

b = [1,2,3]
combi = combinations(b,2)
print(list(combi))


