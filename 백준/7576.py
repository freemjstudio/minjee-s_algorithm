# 7576
import sys
from collections import deque

M, N = map(int, sys.stdin.readline().split())
tomato_box = []
queue = deque()

dx = [1,-1,0,0]
dy = [0,0,-1,1]

for i in range(N):
    tomato_box.append(list(map(int, sys.stdin.readline().split())))

def bfs():
    while queue:
        a, b = queue.popleft()
        for i in range(4):
            x = a+dx[i]
            y = b+dy[i]
            if 0 <= x < N and 0 <= y < M and tomato_box[x][y] == 0: # 좌표가 상자안이고 토마토가 unvisited (0이)면 상태이면
                tomato_box[x][y] = tomato_box[a][b] + 1 #1+1 == 2 ??????? 여기가 이해가 잘 안된다 아 된다 여기서 count 해준듯 ..
                queue.append([x,y]) # 익은 토마토라고 표시하고 queue에 넣어준다 graph is visited -> enqueue




for i in range(N):
    for j in range(M):
        if tomato_box[i][j] == 1:
            queue.append([i,j])

state = False
result = -2
bfs()

# 모든 토마토가 익어있는 상태인지 확인
for i in range(N):
    for j in range(M):
        if tomato_box[i][j] == 0: # 하나라도 0 인게 있으면
            state = True
        result = max(result, tomato_box[i][j]) # 왜 min 아니라 max인가 ???? -> 일수 출력하기 .. 와 대박 ..

# 저장될 때부터 모든 토마토가 익어있는 상태인 경우 0 을 출력함.
if state == True:
    print(-1)
elif result == -1:
    print(0)
else:
    print(result -1) # 그치 bfs 에서 마지막에도 +1 했으니까



