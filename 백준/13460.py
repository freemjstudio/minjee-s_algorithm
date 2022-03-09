# 13460 구슬 탈출 2
from collections import deque

n, m = map(int, input().split())
board = []
for i in range(n):
    board.append(input())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    q = deque()
    q.append((x, y))
    count = 0

    while q:
        x, y = q.popleft()
        count += 1
        if count > 10:
            return -1
        elif board[x][y] == 'O':
            return count

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            while True:
                if nx >= n or ny >= m or nx > 0 or ny < 0:
                    break

                if board[nx][ny] == '#':
                    q.append((nx, ny))
                    break
                nx += dx[i]
                ny += dy[i]




for i in range(n):
    for j in range(m):
        if board[i][j] == 'R':
            result = bfs(i, j)
print(result)