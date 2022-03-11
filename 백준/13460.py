# 13460 구슬 탈출 2
from collections import deque

n, m = map(int, input().split())
board = []
rx, ry = 0, 0 # red position
bx, by = 0, 0 # blue position

for i in range(n):
    array = list(input())
    board.append(array)
    for j in range(m):
        if array[j] == "R":
            rx, ry = i, j
        elif array[j] == "B":
            bx, by = i, j


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

visited = [[[[False]*m for i in range(n)] for _ in range(m)] for _ in range(n)]

def move(i, j, dx, dy): # 'O' or '#' 나올 때까지 이동
    c = 0
    while board[i + dx][j + dy] != 'O' and board[i + dx][j + dy] != '#':
        i += dx
        j += dy
        c += 1
    return i, j, c

def bfs():
    while q:
        rx, ry, bx, by, count = q.popleft()
        if count > 10:
            break
        for i in range(4):
            nrx, nry, red_count = move(rx, ry, dx[i], dy[i])
            nbx, nby, blue_count = move(bx, by, dx[i], dy[i])
            if board[nbx][nby] != 'O':
                if board[nrx][nry] == 'O':
                    print(count)
                    return
                if nrx == nbx and nry == nby:
                    if red_count > blue_count:
                        nrx -= dx[i]
                        nry -= dy[i]
                    else:
                        nbx -= dx[i]
                        nby -= dy[i]
                if not visited[nrx][nry][nbx][nby]:
                    visited[nrx][nry][nbx][nby] = True
                    q.append([nrx, nry, nbx, nby, count+1])
    print(-1)


q = deque()
q.append([rx, ry, bx, by, 1]) # count
visited[rx][ry][bx][by] = True
bfs()


