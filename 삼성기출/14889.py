# 14889 스타트와 링크
from itertools import combinations

n = int(input())
numbers = [i for i in range(n)]
array = []

for i in range(n):
    array.append(list(map(int, input().split())))

cases = combinations(numbers, n//2)
result = int(1e9)

for case in cases:
    check_start = combinations(case, 2)
    outofcase = list(set(numbers) - set(case))
    check_link = combinations(outofcase, 2)
    start, link = 0, 0
    for i in check_start:
        start += array[i[0]][i[1]] + array[i[1]][i[0]]
    for i in check_link:
        link += array[i[0]][i[1]] + array[i[1]][i[0]]
    result = min(result, abs(start-link))


print(result)