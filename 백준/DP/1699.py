import math

n = int(input())
INF = int(1e9)
dp = [INF]*(n+1)
dp[0] = 0
dp[1] = 1

for i in range(2, n+1):
    for j in range(1, int(math.sqrt(i))+1):
        temp = i
        total = 0
        if j**2 <= i:
            count = i // (j*j)
            temp -= (j*j) * count
            total = count + dp[temp]
            if dp[i] > total:
                dp[i] = total

print(dp[n])

