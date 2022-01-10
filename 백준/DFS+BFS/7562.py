from collections import deque
t = int(input())
steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

for i in range(t):
    n = int(input())
    x, y = map(int, input().split()) # 현재 위치
    a, b = map(int, input().split())
    graph = [[0]*n for _ in range(n)]
    q = deque()
    q.append([x, y])

    while q:
        x, y = q.popleft()
        if x == a and y == b:
            break

        for step in steps:
            nx = x + step[0]
            ny = y + step[1]
            if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                q.append([nx, ny])
    print(graph[a][b])



