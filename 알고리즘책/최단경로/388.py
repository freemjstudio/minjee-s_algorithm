# 화성 탐사

import heapq
t = int(input())
INF = int(1e9)
for _ in range(t):
    n = int(input())
    graph = []
    for i in range(n):
        data = list(map(int, input().split()))
        graph.append(data)

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    # 최단거리 테이블
    distance = [[INF]*n for _ in range(n)]
    x, y = 0, 0 # start point
    q = [(graph[x][y], x, y)]
    distance[x][y] = graph[x][y]

    while q:
        dist, x, y = heapq.heappop(q)
        if distance[x][y] < dist:
            continue
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 < nx <= n and 0 <= ny <= n:
                cost = dist + graph[nx][ny]
                if cost < distance[nx][ny]:
                    distance[nx][ny] = cost
                    heapq.heappush(q, (cost, nx, ny))
    print(distance[n-1][n-1])
