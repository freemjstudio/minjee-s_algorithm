# 1238 파티
import heapq
INF = int(1e9)
n, m, x = map(int, input().split()) # N M X
graph = [[] for _ in range(n+1)]


for i in range(m):
    s, e, t = map(int, input().split())
    graph[s].append((e, t))

def dijkstra(start):
    dist = [INF] * (n+1)
    dist[start] = 0
    q = []
    heapq.heappush(q, (0, start))
    while q:
        d, now = heapq.heappop(q)
        if dist[now] < d:
            continue
        for next, cost in graph[now]:
            if dist[next] > dist[now] + cost:
                dist[next] = dist[now] + cost
                heapq.heappush(q, (dist[next], next))
    return dist



result = 0
for i in range(1, n+1):
    first = dijkstra(i) # to go to x
    second = dijkstra(x) # return from x
    result = max(result, first[x] + second[i])

print(result)
