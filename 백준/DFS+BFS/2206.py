from collections import deque

n, m = map(int, input().split())
graph = [list(map(int, input())) for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(): # 최단 경로 구하기
    dist = [[[-1]*2 for _ in range(m)] for _ in range(n)]
    q = deque()
    q.append((0, 0, 0)) # x, y, crash
    dist[0][0][0] = 1 # 최단 거리
    while q:
        x, y, crash = q.popleft()
        if x == n-1 and y == m-1:
            return dist[x][y][crash]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 0 and dist[nx][ny][crash] == -1:
                    dist[nx][ny][crash] = dist[x][y][crash] + 1
                    q.append((nx, ny, crash))
                if graph[nx][ny] == 1 and crash == 0:
                    dist[nx][ny][crash +1] = dist[x][y][crash] + 1
                    q.append((nx, ny, crash+1))
    return -1

print(bfs())