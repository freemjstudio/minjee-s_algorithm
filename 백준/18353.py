# 병사 배치하기

n = int(input())

array = list(map(int, input().split()))
array.reverse()

dp = [1] * n
# 가장 긴 증가하는 부분 수열 알고리즘
for i in range(1, n):
    for j in range(0, i):
        if array[i] > array[j]:
            dp[i] = max(dp[i], dp[j]+1)

print(n - max(dp))