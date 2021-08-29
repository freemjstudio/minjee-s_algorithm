# 2579

N = int(input()) # 계단의 수
stairs = [0] * (N+1)
d = [0] * N
for i in range(N):
    stairs[i+1] = int(input())

count = 0
for i in range(N):
    if count == 2:
        d[i] = d[i] + stairs[i+2]
        count = 0

    else:
        d[i] = max(d[i] + stairs[i+1], d[i] + stairs[i+2])
        if d[i] + stairs[i+1] > d[i] + stairs[i+2]:
            count += 1


print(d[N])


N = int(input())
s = [0 for i in range(301)]
dp = [0 for i in range(301)]

for i in range(N):
    s[i] = int(input())

dp[0] = s[0]
dp[1] = s[0] + s[1]
dp[2] = max(s[1] + s[2], s[0]+s[2])

for i in range(3,N):
    dp[i] = max(dp[i-3] + s[i-1] + s[i], dp[i-2] + s[i])
print(dp[N-1])