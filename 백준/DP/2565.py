# 2565

n = int(input())
lines = []
for _ in range(n):
    a, b = map(int, input().split())
    lines.append([a, b])
lines.sort()
dp = [1] * n # 가장 긴 증가하는 수열
for i in range(n):
    for j in range(i):
        if lines[i][1] > lines[j][1]:
            dp[i] = max(dp[i], dp[j]+1)

print(n - max(dp))
