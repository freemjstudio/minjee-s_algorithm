# 3151 합이 0
from itertools import combinations

n = int(input())
data = list(map(int, input().split()))
data.sort()
count = 0
for comb in combinations(data, 3):
    if sum(comb) == 0:
        count += 1

print(count)