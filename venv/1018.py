# 1018 체스판 다시 칠하기

# 브루투 포스 문제 : 모든 경우의 수를 다 돌려서 최적의 해를 구하는 방식이다.

board = []
n, m = map(int, input().split())
for i in range(n):
    board.append(input()) # 체스판 입력 받기

repair = list()

for i in range(n-7):
    for j in range(m-7):
        first_w = 0
        first_b = 0
        for k in range(i,i+8):
            for l in range(j,j+8):
                if (k+l) %2 == 0:
                    if board[k][l] != 'W':
                        first_w += 1
                    if board[k][l] != 'B':
                        first_b += 1
                else:
                    if board[k][l] != 'B':
                        first_w += 1
                    if board[k][l] != 'W':
                        first_b += 1
        repair.append(first_w)
        repair.append(first_b)

print(min(repair))




