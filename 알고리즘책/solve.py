# 못생긴수

n = int(input())
dp = [0]*n

i2 = i3 = i5 = 0 # index
next_2, next_3, next_5 = 2, 3, 5
dp[0] = 1 # 첫번 째 못생긴 수
for i in range(1, n):
    dp[i] = min(next_2, next_3, next_5)
    if next_2 == dp[i]:
        i2 += 1
        next_2 = 2 * dp[i2]

    if next_3 == dp[i]:
        i3 += 1
        next_3 = 3*dp[i3]

    if next_5 == dp[i]:
        i5 += 1
        next_5 = 5*dp[i5]



print(dp[n-1])

