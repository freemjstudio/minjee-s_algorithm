n = int(input())
dp = []
for i in range(n):
    dp.append(list(map(int, input().split())))

for i in range(1, n): # 세로 길이
    for j in range(i+1): # 가로 길이는 세로마다 다르니까
        # 왼쪽위에서 내려오는 경우
        if j == 0:
            up_left = 0
        else:
            up_left = dp[i-1][j-1]

        # 바로 위에서 내려오는 경우
        if j == i:
            up = 0
        else:
            up = dp[i-1][j]

        # 최대합을 저장
        dp[i][j]= dp[i][j] + max(up_left, up)

print(max(dp[n-1]))