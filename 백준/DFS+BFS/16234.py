# 인구 이동
from collections import deque

n, l, m = map(int, input().split())
a = []

for i in range(n):
    a.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    people = a[x][y] # 연합의 전체 인구수
    count = 1
    united = []
    united.append((x, y))
    union[x][y] = 0
    q = deque()
    q.append((x, y))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and union[nx][ny] == -1:
                if l <= abs(a[nx][ny] - a[x][y]) <= m: # 범위안에 속하는가 여부
                    people += a[nx][ny]
                    count += 1
                    united.append((nx, ny))
                    q.append((nx, ny))
                    union[nx][ny] = 0
    for i, j in united:
        a[i][j] = people // count

result = 0


while True:
    union = [[-1] * n for _ in range(n)]
    index = 0
    for i in range(n):
        for j in range(n):
            if union[i][j] == -1: # 아직 처리가 안된 곳 (not visited)
                bfs(i, j)
                index += 1
    # 인구 이동 끝 -> while 문 break할 조건이 필요해서 index를 사용했다 !
    if index == n*n:
        break
    result += 1

print(result)