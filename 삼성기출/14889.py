# 14889 스타트와 링크
from itertools import combinations

n = int(input())
numbers = [i for i in range(n)]
array = []

for i in range(n):
    array.append(list(map(int, input().split())))

cases = combinations(numbers, n//2)
startlink = []
for case in cases:
    check = combinations(case, 2)
    total = 0
    for i in check:
        total += array[i[0]][i[1]] + array[i[1]][i[0]]
    startlink.append(total)

result = int(1e9)
startlink.sort()
for i in range(len(startlink)-1):
    diff = abs(startlink[i] - startlink[i+1])
    if diff < result:
        result = diff
print(result)