# 1967 트리의 지름
import heapq

n = int(input())
graph = [[] for _ in range(n+1)]
INF = int(1e9)
for _ in range(n-1):
    a, b, cost = map(int, input().split())
    graph[a].append((b, cost))
    graph[b].append((a, cost))

def dijkstra(start):
    distance = [INF]*(n+1)
    distance[start] = 0
    q = []
    heapq.heappush(q, (0, start))
    while q:
        cost, now = heapq.heappop(q)
        for next, next_cost in graph[now]:
            dist = next_cost + cost
            if dist < distance[next]:
                distance[next] = dist
                heapq.heappush(q, (dist, next))
    return distance
result = dijkstra(1)
first = max(result[1:])
print(max(dijkstra(result.index(first))[1:]))