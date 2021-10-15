# 전보
import heapq
INF = int(1e9)
n, m, c = map(int, input().split())
graph = [[] for i in range(n+1)]
distance = [INF] * (n+1)

for i in range(m):
    x, y, z = map(int, input().split())
    graph[x].append((y,z))


def dijkstra(start):
    q = []
    heapq.heappush(q, (0,start)) # 시작 노드로 가기 위한 최단 경로는 0으로 설정하여 큐에 삽입한다
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue
        # 현재 노드와 인접한 다른 노드들을 확
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(c)

count = 0 # 도달할 수 있는 노드의 개수
result_time = 0 # 걸리는 시간
for d in distance:
    if d != INF:
        count += 1
        result_time = max(result_time, d)

print(count -1, result_time) # 시작 노드는 제외해야 하므로 count -1를 출력한다
