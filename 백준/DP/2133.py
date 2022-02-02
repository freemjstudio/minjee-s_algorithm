n = int(input())
dp = [0]* 31
# max 값을 저장하면 된다.

dp[2] = 3


for i in range(4, 31, 2): # 4칸씩 잡아먹는 모양이 있음
    dp[i] = dp[i-2] * 3
    for j in range(4, i, 2):
        dp[i] += 2 * dp[i-j]
    dp[i] += 2

print(dp[n])