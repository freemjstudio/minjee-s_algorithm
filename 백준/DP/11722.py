# 11722 가장 긴 감소하는 부분 수열

n = int(input())
array = list(map(int, input().split()))

dp = [1]*n


for i in range(n):
    for j in range(i, n):
        if array[i] > array[j]:
            dp[j] = max(dp[i]+1, dp[j])

print(dp)
print(max(dp))