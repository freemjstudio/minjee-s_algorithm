# 18353 병사 배치하기

n = int(input())
a = list(map(int, input().split())) # 전투력
a.reverse()
dp = [1] * n

for i in range(1, n):
    for j in range(0, i):
        if a[i] > a[j]:
            dp[i] = max(dp[i], dp[j] + 1)


print(n - max(dp))