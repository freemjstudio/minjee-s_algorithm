from collections import deque

n, m = map(int, input().split())
board = []

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def count_iceberg():
    cnt = 0

    return cnt


for i in range(n):
    data = list(map(int, input().split()))
    board.append(data)

answer = 0
def bfs():
    global answer

    queue = deque([])

    for i in range(n):
        for j in range(m):
            if board[i][j]: # not 0
                queue.append((i, j, 0))

    while queue:
        x, y, remove = queue.popleft()
        board[x][y] -= remove
        if board[x][y] < 0:
            board[x][y] = 0
            continue

        water = 0 # 바닷물 닿는 부분 개수
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and not board[nx][ny]:
                water += 1
        queue.append((x, y, water))
bfs()
print(answer)