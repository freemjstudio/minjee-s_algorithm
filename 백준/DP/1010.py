# https://www.acmicpc.net/problem/1010
import math
t = int(input())

dp = [[1]*31 for _ in range(31)]

for i in range(31):
    dp[1][i] = i

for i in range(2, 31):
    for j in range(i+1, 31):
        dp[i][j] = dp[i-1][j-1] + dp[i][j-1]

for _ in range(t):
    n, m = map(int, input().split())

    print(dp[n][m])

