# 12865 평범한 배낭
n, k = map(int, input().split())
data = [[0, 0]]
for _ in range(n):
    data.append(list(map(int, input().split())))
result = 0
dp = [[0] * (k+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, k+1): # 남은 무게
        weight = data[i][0]
        value = data[i][1]
        if weight > j:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j-weight] + value, dp[i-1][j])

print(dp[-1][-1])
