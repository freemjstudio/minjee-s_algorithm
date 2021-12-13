#16236
from collections import deque
n = int(input())
array = []

for i in range(n):
    array.append(list(map(int, input().split())))

now_x = 0
now_y = 0
for i in range(n):
    for j in range(n):
        if array[i][j] == '9': # 상어 위치
            now_x = i
            now_y = j
            array[now_x][now_y] = 0

now_size = 2

dx = [-1, 0, 1, 0] # 좌 하 우 상 ..?
dy = [0, 1, 0, -1]

INF = 1e9
def bfs():
    dist = [[-1]*n for _ in range(n)]
    q = deque([(now_x, now_y)])
    dist[now_x][now_y] = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx and nx < n and 0 <= ny and ny < n:
                if dist[nx][ny] == -1 and array[nx][ny] <= now_size:
                    dist[nx][ny] = dist[x][y] + 1
                    q.append((nx, ny))
    return dist # 모든 위치까지의 최단거리 테이블 반환

# 최단 거리 테이블이 주어졌을 때 먹을 물고기를 찾는 함수
def find(dist):
    x, y = 0, 0
    min_dist = INF
    for i in range(n):
        for j in range(n):
            if dist[i][j] != -1 and 1 <= array[i][j] and array[i][j] < now_size:
                if dist[i][j] < min_dist:
                    x, y = i, j
                    min_dist = dist[i][j]
    if min_dist == INF:
        return None
    else:
        return x, y, min_dist
result = 0
ate = 0 # 현재 크기에서 먹은 양

while True:
    value = find(bfs())

    if value == None:
        print(result)
        break
    else:
        now_x, now_y = value[0], value[1]
        result += value[2]
        array[now_x][now_y] = 0
        ate += 1
        if ate >= now_size:
            now_size += 1
            ate = 0
