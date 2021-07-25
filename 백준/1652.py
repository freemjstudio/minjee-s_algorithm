#1652 백준
board = [] # 2차원 배열
n = int(input()) # n*n 길이 입력받기
for i in range(n):
    board.append(input()) # 배열 입력받기

col_result = 0 # 세로 결과
row_result = 0 # 가로 결과

# 가로의 경
for i in range(n):
    cnt = 0
    for j in range(n):
        if board[i][j] == '.':
            cnt += 1
        elif board[i][j] == 'X':
            if cnt >= 2:
                row_result += 1
            cnt = 0 # 다시 초기화를 해줘서 쓸수있게 함
        if j == n-1:
            if cnt >= 2:
                row_result += 1

#세로의 경우
for i in range(n):
    cnt = 0
    for j in range(n):
        if board[j][i] == '.':
            cnt+=1
        elif board[j][i] == 'X':
            if cnt >= 2:
                col_result += 1
            cnt = 0
        if j == n-1:
            if cnt >= 2:
                col_result += 1

print(row_result, col_result)