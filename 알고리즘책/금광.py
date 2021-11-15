# pg 375

t = int(input())
for _ in range(t):
    n,m = map(int, input())
    array = list(map(int, input()))

    # 2차원 DP 테이블을 초기화 하는 과정
    dp = []
    index = 0
    for i in range(n):
        dp.append(array[index:index+m])
        index += m

    # DP 진행
    for j in range(1, m):
        for i in range(n):
            # 왼쪽 위에서 오는 경우
            if i == 0:
                left_top = 0
            else:
                left_top = dp[i-1][j-1]
            # 왼쪽에서 오는 경우
            left = dp[i][j-1]
            # 왼쪽아래에서 오는 경우
            if i == n-1:
                left_bottom = 0
            else:
                left_botton = dp[i+1][j-1]
            dp[i][j] = dp[i][j] + max(left_top, left, left_botton)

    result = 0
    for i in range(n):
        result = max(result, dp[i][m-1]) # 맨 마지막 줄 값 비교하기
    print(result)
