a = input()
b = input()

def edit_dist(str1, str2):
    n = len(str1)
    m = len(str2)

    # dp를 위한 2차원 dp테이블 초기화
    dp = [[0]*(m+1) for _ in range(n+1)]

    for i in range(1, n+1):
        dp[i][0] = i
    for i in range(1, m+1):
        dp[0][i] = i

    # 최소 편집 거리 계산

    for i in range(1, n+1):
        for j in range(1, m+1):
            if str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i][j-1], dp[i-1][j-1], dp[i-1][j])
    return dp[n][m]


print(edit_dist(a, b))


