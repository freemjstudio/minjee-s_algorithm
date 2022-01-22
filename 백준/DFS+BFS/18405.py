# 18405 경쟁적 전염
from collections import deque

n, k = map(int, input().split())
graph = [] # 시험관의 정보
virus = [] # virus 정보를 저장
for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(n):
        if graph[i][j] != 0:
            virus.append((graph[i][j], 0, i, j)) # virus, time, position_x, position_y

virus.sort()
q = deque(virus)

s, x, y = map(int, input().split())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    while q:
        v, t, x, y = q.popleft()
        if t == s:
            break
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if graph[nx][ny] == 0:
                    graph[nx][ny] = v
                    q.append((v, t+1, nx, ny))

bfs()
print(graph[x-1][y-1])