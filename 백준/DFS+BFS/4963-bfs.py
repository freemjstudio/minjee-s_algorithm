from collections import deque

dx = [-1, 1, 0, 0, -1, -1, 1, 1]
dy = [0, 0, -1, 1, -1, 1, -1, 1]  # 8개 방향

def bfs(x, y):
    a[x][y] = 0
    q = deque()
    q.append([x, y])
    while q:
        x, y = q.popleft()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < h and 0 <= ny < w and a[nx][ny] == 1:
                a[nx][ny] = 0
                q.append([nx, ny])



while True:
    w, h = map(int, input().split())
    if w == 0 or h == 0:
        break
    a = []
    for i in range(h):
        a.append(list(map(int, input().split())))
    result = 0
    for i in range(h):
        for j in range(w):
            if a[i][j] == 1:
                bfs(i, j)
                result += 1
    print(result)

