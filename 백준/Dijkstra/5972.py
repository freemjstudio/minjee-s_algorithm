# https://www.acmicpc.net/problem/5972
import heapq

n, m = map(int, input().split())
graph = [[]*(n+1) for _ in range(n+1)]
INF = int(1e9)
distance = [INF]*(n+1)

for i in range(m):
    a, b, cost = map(int, input().split())
    graph[a].append((b, cost))
    graph[b].append((a, cost))

def dijkstra(start):
    queue = []
    distance[start] = 0
    heapq.heappush(queue, (0, start))
    while queue:
        dist, now = heapq.heappop(queue)
        if dist < distance[now]:
            continue
        for node in graph[now]:
            cost = dist + node[1]
            if cost < distance[node[0]]:
                distance[node[0]] = cost
                heapq.heappush(queue, (cost, node[0]))

dijkstra(1)
print(distance[n])