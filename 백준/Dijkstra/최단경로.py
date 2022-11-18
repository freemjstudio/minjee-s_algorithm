# 1753 최단경로
import heapq

INF = int(1e9)
v, e = map(int, input().split())
k = int(input()) # 시작 정점
graph = [[] for _ in range(v+1)]
for _ in range(e):
    a, b, c = map(int, input().split()) # a -> b weight
    graph[a].append((b, c))

distance = [INF] * (v+1)

def dijkstra(start):
    queue = []
    heapq.heappush(queue, (0, start))
    distance[start] = 0
    while queue:
        dist, now = heapq.heappop(queue)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1] # i[0] 까지의 cost
            if cost < distance[i[0]]:
                distance[i[0]] = cost # 갱신
                heapq.heappush(queue, (cost, i[0]))

dijkstra(k)

for i in range(1, v+1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])