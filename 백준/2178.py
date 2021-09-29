# 2178

from collections import deque

N, M = map(int, input().split())

maze = []

for _ in range(N):
    maze.append(list(map(int, input())))

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):

    queue = deque()
    queue.append((x,y)) # 시작점!!

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= N or ny >= M:
                continue

            if maze[nx][ny] == 1:
                queue.append((nx,ny))
                maze[nx][ny] = maze[x][y] + 1 # 지금 칸까지 오기까지 몇개가 지났는지 count 한다.


    return maze[N-1][M-1]


print(bfs(0,0))

