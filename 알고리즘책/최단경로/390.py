# 390p 숨바꼭질
import heapq
INF = int(1e9)
n, m = map(int,input().split())
graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1)
start = 1 # 시작 노드

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append((b, 1)) # 목적지 , 비용
    graph[b].append((a, 1))

def solve(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if dist > distance[now]:
            continue
        for i in graph[now]: # 현재 노드에서 연결된 다른 노드들을 탐색한다.
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

solve(start)
max_node = 0
max_distance = 0
result = []

for i in range(1, n+1):
    if max_distance < distance[i]:
        max_distance = distance[i]
        max_node = i
        result = [max_node]
    elif max_distance == distance[i]:
        result.append(i)

print(max_node, max_distance, len(result))