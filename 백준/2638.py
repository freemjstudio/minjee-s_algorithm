# 2638 cheese
from collections import deque

n, m = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
count = 0
while True:
    flag = 0

    q = deque()
    visited = [[0 for _ in range(m)] for _ in range(n)]

    q.append((0, 0))
    visited[0][0] = 1

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == 0:
                if array[nx][ny]:
                    array[nx][ny] += 1
                else:
                    visited[nx][ny] = 1
                    q.append((nx, ny))

    for i in range(n):
        for j in range(n):
            if array[i][j] >= 3:
                array[i][j] = 0
            elif array[i][j] > 0:
                flag = 1
                array[i][j] = 1

    count += 1

    if not flag:
        print(count)
        break