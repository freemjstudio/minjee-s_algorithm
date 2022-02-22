# 17070 DP로 풀어보기 !!

n = int(input())
array = []
for _ in range(n):
    array.append(list(map(int, input().split())))

result = [[[0]*n for _ in range(n)] for _ in range(3)]
result[0][0][1] = 1 # 맨 처음 파이프의 위치

# x == 0 (가로 방)향 인 row 1로 초기화
for i in range(2, n):
    if array[0][i] == 0:
        result[0][0][i] = result[0][0][i-1]

for i in range(1, n):
    for j in range(2, n):
        # 대각선으로 오는 경우 - 양 옆의 세 칸이 모두 빈칸인지 확인
        if array[i][j] == 0 and array[i-1][j] == 0 and array[i][j-1] == 0:
            # 대각선으로 올때 : 가로, 세로 대각선 모두 가능!
            result[2][i][j] = result[0][i-1][j-1] + result[1][i-1][j-1] + result[2][i-1][j-1]

        if array[i][j] == 0:
            # 가로로 올 때 : 가로에서 가로, 대각선에서 가로
            result[0][i][j] = result[0][i][j-1] + result[2][i][j-1]
            # 세로로 올 때 : 세로에서 세로, 대각선에서 세로
            result[1][i][j] = result[1][i-1][j] + result[2][i-1][j]

# 총합 : 가로 세로 대각선 방향
print(result[0][n-1][n-1] + result[1][n-1][n-1] + result[2][n-1][n-1])