# 17863
from collections import deque


n, m, t = map(int, input().split())
array = []
for i in range(n):
    array.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
visited = [[0]*m for _ in range(n)]

def bfs():
    queue = deque()
    queue.append((0, 0))
    visited[0][0] = 1
    knife = 1000000 # 칼이 있는 경우의 최솟값

    while queue:
        x, y = queue.popleft()
        if x == n-1 and y == m-1: # 종료 조건
            knife = min(knife, visited[-1][-1]-1)
            return knife
        if array[x][y] == 2: # 칼을 찾았을 때
            knife = visited[x][y]-1 + n-x-1 + m-y-1
        else:
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == 0:
                    if array[nx][ny] != 1:
                        queue.append((nx, ny))
                        visited[nx][ny] = visited[x][y] + 1


result = bfs()
if result > t:
    print("Fail")
else:
    print(result)


