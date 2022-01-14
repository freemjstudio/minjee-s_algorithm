# 안전 영역
# 2468
from collections import deque

n = int(input())

array = []
for i in range(n):
    array.append(list(map(int, input().split())))

max_height = max(map(max, array))
min_height = min(map(min, array))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y, h):
    q = deque()
    q.append((x, y))
    visited[x][y] = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if (0 <= nx < n) and (0 <= ny < n) and visited[nx][ny] == 0 and array[nx][ny] >= h:
                visited[nx][ny] = 1
                q.append((nx, ny))

result = min_height
for h in range(min_height, max_height+1):
    visited = [[0] * n for _ in range(n)]
    count = 0
    for i in range(n):
        for j in range(n):
            if array[i][j] >= h and visited[i][j] == 0:
                bfs(i, j, h)
                count += 1
    if count > result:
        result = count
print(result)
