import heapq

INF = int(1e9)

t = int(input()) # test case

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

for _ in range(t):
    n = int(input())
    graph = []
    distance = [[INF]*n for _ in range(n)]# 최단 거리 테이블을 모두 무한으로 초기화

    for i in range(n):
        graph.append(list(map(int, input().split())))

    x, y = 0, 0 # 시작 위치
    q = [(graph[x][y], x, y)] # 시작 노드로 가기 위한 비용은 (0, 0) 위치에 있는 value이다.큐에 삽입한다
    distance[x][y] = graph[x][y]

    # 다익스트라 알고리즘 수행
    while q:
        dist, x, y = heapq.heappop(q)
        # 현재 노드가 이미 처리된 적이 있다면 무시한다
        if distance[x][y] < dist:
            continue

        for i in range(4): # 현재 노드와 연결되어 있는 다르인접한 노드드을 상하좌우로 확인한다
            nx = x + dx[i]
            ny = y + dy[i]
            # 앱이 범위를 벗어나는 경우 무시
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue

            cost = dist + graph[nx][ny]
            if cost < distance[nx][ny]:
                distance[nx][ny] = cost
                heapq.heappush((cost, nx, ny))

    print(distance[n-1][n-1])
