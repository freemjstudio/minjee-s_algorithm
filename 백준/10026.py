#10026 적록색약
from collections import deque

n = int(input())
array = [list(map(str, input())) for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
q = deque()
c = [[0]* n for _ in range(n)] # 0으로 n*n 2차원 배열 초기화

def bfs(x, y):
    q.append([x,y])
    c[x][y] = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0 <= nx < n and 0 <= ny < n:
                if array[x][y] == array[nx][ny] and c[nx][ny] == 0:
                    q.append([nx, ny])
                    c[nx][ny] = 1

cnt = 0
for i in range(n):
    for j in range(n):
        if c[i][j] == 0:
            bfs(i, j)
            cnt += 1
print(cnt, end=' ')

# R==G이니까 R을 G로 바꿔주어 생각한다.

for i in range(n):
    for j in range(n):
        if array[i][j] == 'R':
            array[i][j] = 'G'
c = [[0]* n for _ in range(n)] # 0으로 n*n 2차원 배열 초기화
cnt = 0
for i in range(n):
    for j in range(n):
        if c[i][j] == 0:
            bfs(i, j)
            cnt += 1
print(cnt)