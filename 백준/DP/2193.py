# 2193 이친수
dp = [0] * 91
dp[1] = 1
dp[2] = 1

n = int(input())

for i in range(3, 91):
    dp[i] = dp[i-1] + dp[i-2]

print(dp[n])