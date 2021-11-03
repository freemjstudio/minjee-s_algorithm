# 경쟁적 전염
from collections import deque

n, k = map(int, input().split())

graph = []
data = []
for i in range(n):
    graph.append(list(map(int, input().split())))

for i in range(n):
    for j in range(n):
        if graph[i][j] != 0:
            data.append((graph[i][j],0,i,j)) # 바이러스 종류 - s - x - y

s, target_x, target_y = map(int, input().split())

dx = [1,-1,0,0]
dy = [0,0,1,-1]

data.sort()
q = deque(data)

while q:
    virus, time, x, y = q.popleft()
    if time == s:
        break

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx >= 0 and nx < n and ny >= 0 and ny < n:
            if graph[nx][ny] == 0:
                graph[nx][ny] = virus
                q.append((virus, time+1, nx, ny))

print(graph[target_x-1][target_y-1])