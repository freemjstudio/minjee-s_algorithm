# 12015 가장 긴 증가하는 부분 수열 2

n = int(input())
array = map(int, input().split())

result = 0

dp = [0]*n
dp[0] = 1

for i in range(1, n):
    if array[i] > array[i-1]:
        dp[i] = max(dp[i-1]+1, dp[i])




print(result)