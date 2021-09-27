# 04 미로탈출
from collections import deque

N,M = map(int, input().split())
graph = []
for i in range(N):
    graph.append(list(map(int, input())))

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
    queue = deque()
    queue.append((x,y))

    while queue:
        x,y = queue.popleft()

        for i in range(4): # 상하좌우 위치 확인하기
            nx = x + dx[i]
            ny = y + dy[i]

            if nx <= -1 or ny <= -1 or nx >= N or ny >= M:
                continue # 만약 nx ny가 범위를 벗어나면 !! 무시한다.
                # 벽인 경우에도 무시한다.
            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append(nx,ny)
    return graph[N-1][M-1]
            
print(bfs(0,0))