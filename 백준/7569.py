# 7569 토마토
import sys
from collections import deque
# 입력 받기
M, N, H = map(int, sys.stdin.readline().split())
tomato = [[] for i in range(H)]
visit = [[[0 for i in range(M)] for i in range(N)] for i in range(H)]


dx = [-1,1,0,0,0,0] # 0 ~ N
dy = [0,0,-1,1,0,0] # 0 ~ M
dz = [0,0,0,0,-1,1] # 0 ~ H

def bfs():
    while queue:
        x, y, z = queue.popleft()
        visit[z][x][y] = 1 # 방문했음!!
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            if 0 <= nx < N and 0 <= ny < M and 0 <= nz < H and tomato[nz][nx][ny] == 0 and visit[nz][nx][ny] == 0:
                queue.append([nx,ny,nz])
                tomato[nz][nx][ny] = tomato[z][x][y] + 1
                visit[nz][nx][ny] = 1 # 방문했다는 표시를 해준다.

# 모든 토마토가 익어있는 상태이면 0 출력

queue = deque()

for i in range(H): # 높이
    for j in range(N):
        tomato[i].append(list(map(int, sys.stdin.readline().split())))

for z in range(H):
    for x in range(N):
        for y in range(M):
            if tomato[z][x][y] == 1:
                queue.append([x,y,z])

bfs()
count = 0 # 토마토 익는데 걸리는 최소 일수
flag = False # 실패이면 true 들기
for z in range(H):
    for x in range(N):
        for y in range(M):
            if tomato[z][x][y] == 0: #bfs 실행 후에도 안익은게 있다 ????? 라는 뜻인데
                flag = True # 안익은게 있으면 탐색 실패이다 ㅎㅎ
            count = max(count, tomato[z][x][y])

if flag == True: # 모든 토마토가 익어있는 상태이면 0을 출력한다.
    print(-1)
else:
    print(count-1)
