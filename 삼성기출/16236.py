# 아기 상어
from collections import deque

n = int(input())
size = 2 # 현재 상어의 크기
result = 0
array = []
INF = int(1e9)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(n):
    data = list(map(int, input().split()))
    array.append(data)

sx, sy = 0, 0 # shark position

for i in range(n):
    for j in range(n):
        if array[i][j] == 9: # 상어 위치
            sx = i
            sy = j
            array[i][j] = 0

def distance(): # 최단 거리 계산
    dist = [[-1]*n for _ in range(n)] # 최단 거리 테이블
    q = deque()
    q.append((sx, sy))
    dist[sx][sy] = 0 # 시작 지점은 최단거리 0 이라고 한다
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and dist[nx][ny] == -1 and array[nx][ny] <= size: # 지나갈 수 있는가 확인
                dist[nx][ny] = dist[x][y] + 1
                q.append((nx, ny))

    return dist


def find(dist): # 최단 거리가 주어졌을 때 먹을 물고기를 찾는 함수
    x, y = 0, 0
    min_dist = INF

    for i in range(n):
        for j in range(n):
            if dist[i][j] != -1 and 1 <= array[i][j] < size: # 먹을 수 있는 물고기인지 확인
                if min_dist > dist[i][j]:
                    min_dist = dist[i][j]
                    x, y = i, j
    if min_dist == INF:
        return None # 먹을 수 있는 물고기가 없다
    return x, y, min_dist

eat = 0 # 지금 먹은 물고기 개수
while True:
    data = find(distance())
    if data == None:
        print(result)
        break
    else:
        result += data[2] # min_dist 만큼 물고기에 도달하는데 시간이 걸릴 것이므로
        sx, sy = data[0], data[1] # 새로운 위치로 이동
        array[sx][sy] = 0 # 먹었으면 0 으로 바꿔준다.
        eat += 1
        if eat >= size:
            size += 1
            eat = 0




