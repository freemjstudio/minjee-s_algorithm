#1167 트리의 지름
import heapq

n = int(input())
graph = [[] for _ in range(n+1)]
for i in range(n):
    data = list(map(int, input().split()))
    length = len(data)
    for i in range(1, length-1, 2):
        graph[data[0]].append((data[i],data[i+1])) # next_node, cost
INF = int(1e9)

def dijkstra(start):
    distance = [INF] * (n+1)
    distance[start] = 0
    q = []
    heapq.heappush(q, (0, start))
    while q:
        dist, now = heapq.heappop(q)
        if dist > distance[now]:
            continue
        for next, cost in graph[now]:
            if distance[next] > distance[now] + cost:
                distance[next] = distance[now] + cost
                heapq.heappush(q, (distance[next], next))
    return distance

r1 = dijkstra(1) # result 1
idx = r1.index(max(r1[1:]))
r2 = dijkstra(idx)
print(max(r2[1:]))

