from collections import deque

n, m = map(int, input().split())
graph = [list(map(int, input())) for _ in range(n)]
INF = int(1e9)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(): # 최단 경로 구하기
    dist = [[-1] * m for _ in range(n)]
    q = deque()
    q.append((0, 0))
    dist[0][0] = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and dist[nx][ny] == -1 and graph[nx][ny] == 0:
                dist[nx][ny] = dist[x][y] + 1
                q.append((nx, ny))

    return dist[n-1][m-1]

result = INF
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            graph[i][j] = 0
            temp = bfs()
            if temp != -1:
                result = min(result, temp)
            graph[i][j] = 1


if result == INF:
    print(-1)
else:
    print(result)