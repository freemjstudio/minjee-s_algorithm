import heapq

n, e = map(int, input().split())
graph = [[] for _ in range(n+1)]
INF = int(1e9)

for i in range(e):
    a, b, cost = map(int, input().split())
    graph[a].append((b, cost))
    graph[b].append((a, cost))

x, y = map(int, input().split())



def dijkstra(start):
    q = []
    distance = [INF] * (n + 1)
    distance[start] = 0
    heapq.heappush(q, (0, start))
    while q:
        dist, now = heapq.heappop(q)
        if dist > distance[now]:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    return distance


one = dijkstra(1)
dx = dijkstra(x)
dy = dijkstra(y)

result = min(one[x] + dx[y] + dy[n], one[y] + dy[x] + dx[n])
if result < INF:
    print(result)
else:
    print(-1)