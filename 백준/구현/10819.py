# 10819 차이를 최대로
from itertools import permutations
n = int(input())
array = list(map(int, input().split()))

result = 0
cases = permutations(array, n)
for case in cases:
    temp = 0
    for i in range(n-1):
        temp += abs(case[i] - case[i+1])
    if result < temp:
        result = temp

print(result)