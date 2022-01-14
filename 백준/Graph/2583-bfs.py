# 2583 영역 구하기
from collections import deque

m, n, k = map(int, input().split())
array = [[0]*(n) for _ in range(m)]

for _ in range(k):
    a, b, c, d = map(int, input().split())
    for i in range(b, d):
        for j in range(a, c):
            array[i][j] = 1 # 직사각형

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
result = []

def bfs(x, y):
    queue = deque()
    array[x][y] = 1
    queue.append((x,y))
    count = 1
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if (0 <= nx < m) and (0 <= ny < n) and array[nx][ny] == 0:
                array[nx][ny] = 1
                queue.append((nx, ny))
                count += 1
    return count


for i in range(m):
    for j in range(n):
        if array[i][j] == 0:
            result.append(bfs(i, j))

result.sort()

print(len(result))
for i in result:
    print(i, end=' ')
