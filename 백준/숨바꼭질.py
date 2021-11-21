import heapq
INF = int(1e9)
n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1) # 최단 거리 테이블을 모두 무한으로 초기화
start = 1

for _ in range(n):
    a, b = map(int, input().split())
    graph[a].append((b, 1))
    graph[b].append((a, 1))

def dijkstra(start):
    q = []
    # 시작 노드로 가기 위한 최단 경로는 0으로 설정하여 큐에 삽ㅇ딥
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(cost, i[0])

dijkstra(start)
max_node = 0 # 최단 거리가 가장 먼 노드 번호
max_distance = 0 # 최단 거리가 가장 먼 노드와의 최단 거리
result = [] # 최단 거리가 가장 먼 노드와 동일한 거리를 가지는 노드들

for i in range(1, n+1):
    if max_distance < distance[i]:
        max_node = i
        max_distance = distance[i]
        result = [max_node]
    elif max_distance == distance[i]:
        result.append(i)

print(max_node, max_distance, len(result))



