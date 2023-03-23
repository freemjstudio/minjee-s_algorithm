from collections import deque

n, m = map(int, input().split())
board = []

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]




def count_iceberg():
    cnt = 0
    visited = [[False] * m for _ in range(n)]

    def iceberg(sx, sy):
        queue = deque([])
        queue.append((sx, sy))
        while queue:
            x, y = queue.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < n and 0 <= ny < m and board[nx][ny] and not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append((nx, ny))



    for i in range(n):
        for j in range(n):
            if board[i][j] and not visited[i][j]:
                visited[i][j] = True
                iceberg(i, j)
                cnt += 1


    return cnt


for i in range(n):
    data = list(map(int, input().split()))
    board.append(data)


def bfs():

    queue = deque([])
    pos = []

    for i in range(n):
        for j in range(m):
            if board[i][j]: # not 0
                queue.append((i, j, 0))
    while queue:
        x, y, time = queue.popleft()

        water = 0 # 바닷물 닿는 부분 개수
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and not board[nx][ny]:
                water += 1
        if water > 0:
            pos.append((x, y, water))
    # queue 한번 다 돌고 처리해주기
    for x, y, water in pos:
        board[x][y] -= water
        if board[x][y] < 0:
            board[x][y] = 0
answer = 0

while True:
    if count_iceberg() >= 2:
        break
    bfs()
    answer += 1 # 1 year passed
print(answer)