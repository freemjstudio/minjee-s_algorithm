# 1987 알파벳
from collections import deque


r, c = map(int, input().split())
array = []
for _ in range(r):
    array.append(list(input()))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

max_count = 0

def bfs():
    global max_count
    q = deque()
    q.append((0,0))
    alphabet = []
    visited = [[0]*c for _ in range(r)]
    visited[0][0] = 1
    alphabet.append(array[0][0])

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < r and 0 <= ny < c:
                if visited[nx][nx] == 0:
                    visited[nx][ny] = 1
                    if array[nx][ny] not in alphabet:
                        alphabet.append(array[nx][ny])
                        if max_count < len(alphabet):
                            max_count = len(alphabet)
                        q.append((nx, ny))


bfs()
print(max_count)