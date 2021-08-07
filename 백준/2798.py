# 2798

N, M = map(int, input().split())
numbers = list(map(int, input().split()))
result = 0

for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            if numbers[i] + numbers[j] + numbers[k] > M:
                continue
            else:
                result = max(result, numbers[i]+numbers[j]+numbers[k])

print(result)

# 편리한 풀이 : combinatinos

from itertools import combinations
N, M = map(int, input().split())
numbers = list(map(int, input().split()))
result = 0

for num in combinations(numbers, 3):
    temp = sum(num)
    if result < temp <= M:
        result = temp

print(result)