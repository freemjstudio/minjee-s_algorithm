# 13460 구슬 탈출 2
from collections import deque

n, m = map(int, input().split())
board = []

rx, ry = 0, 0 # red
bx, by = 0, 0 # blue


for i in range(n):
    array = list(input())
    board.append(array)
    for j in range(n):
        if array[j] == 'R':
            rx, ry = i, j
        if array[j] == 'B':
            bx, by = i, j

visited = [[[[False]*m for _ in range(n)] for _ in range(m)] for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 벽에 닿기 바로 이전 혹은 출구에 닿기전까지 움직이게 한다.
def move(i, j, dx, dy):
    count = 0
    while board[i + dx][j + dy] != '#' and board[i][j] != 'O':
        i += dx
        j += dy
        count += 1
    return i, j, count

def bfs():
    while q:
        rx, ry, bx, by, count = q.popleft()
        for i in range(4):
            nrx, nry, rc = move(rx, ry, dx[i], dy[i])
            nbx, nby, bc = move(bx, by, dx[i], dy[i])
            if board[nbx][nby] != 'O': # 파란 구슬이 구멍으로 빠지지 않을 때
                if board[nrx][nry] == 'O': # 빨간 구슬이 구멍으로 나가는 경우
                    print(count)
                    return
                if nrx == nbx and nry == nby:
                    if rc > bc:
                        nrx -= dx[i]
                        nry -= dx[i]
                    else:
                        nbx -= dx[i]
                        nby -= dy[i]
                if not visited[nrx][nry][nbx][nby]:
                    visited[nrx][nry][nbx][nby] = True
                    q.append([nrx, nry, nbx, nby, count + 1])
    print(-1)

q = deque()
q.append([rx, ry, bx, by, 1])
visited[rx][ry][bx][by] = True

bfs()