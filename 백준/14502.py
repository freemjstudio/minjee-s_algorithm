# 14502 연구소
from collections import deque
from itertools import combinations

n, m = map(int, input().split())
board = []
temp = [[0]*m for _ in range(n)] # 벽을 설치한 다음의 리스트

for i in range(n):
    board.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# dfs를 사용해 바이러스가 사방에 퍼지도록 하기
result = 0
def virus(x,y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx >= 0 and nx < n and ny >= 0 and ny < m:
            if temp[nx][ny] == 0:
                temp[nx][ny] = 2
                virus(nx, ny)

# 안전 영역을 계산하는 메소드

def get_score():
    score = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                score += 1
    return score

def dfs(count):
    global result

    if count == 3:
        for i in range(n):
            for j in range(m):
                temp[i][j] = board[i][j]

        # 각 위치에서 virus 전파 실행시켜본다.
        for i in range(n):
            for j in range(m):
                if temp[i][j] == 2:
                    virus(i,j)

        # 안전 영역의 최댓값 계산
        result = max(result, get_score())
        return

    # 빈 공간에 울타리 설치
    for i in range(n):
        for j in range(m):
            if board[i][j] == 0:
                board[i][j] = 1
                count += 1
                dfs(count)
                board[i][j] = 0
                count -= 1

dfs(0)
print(result)