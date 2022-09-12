# 2294 동전 2
n, k = map(int, input().split())
coins = []
dp = [999999] * (k+1)
dp[0] = 0
for _ in range(n):
    coins.append(int(input()))

# 모든 경우의 수가 아니라 사용가능한 동전의 최소개수를 구하는 문제
for coin in coins:
    for i in range(1, k+1):
        if coin <= i:
            dp[i] = min(dp[i - coin]+1, dp[i])

if dp[k] == 999999:
    print(-1)
else:
    print(dp[k])