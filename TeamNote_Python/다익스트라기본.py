import sys
import heapq

input = sys.stdin.readline

INF = int(1e9)

n, m = map(int, input().split())

start = int(input()) # 시작 노드 번호를 입력 받는다
graph = [[] for i in range(n+1)]
visited = [False]*(n+1)
distance = [INF] * (n+1)

for _ in range(m):
    a, b, c = map(int, input().split()) # a 번 노드에서b 번 노드로 가는 비용이 c라는 의
    graph[a].append((b,c))

# 최단 거리가 가장 짧은 노드를 반환한다
def get_smallest_node():
    min_value = INF
    for i in range(1, n+1):
        if distance[i] < min_value:
            min_value = distance[i]
            index = i
    return index

def dijkstra(start):
    distance[start] = 0 # 자기 자신
    visited[start] = True

    for j in graph[start]:
        distance[j[0]] =j[1] # distance[b] = c 거리

    for i in range(n-1):
        now = get_smallest_node()
        visited[now] = True

        for j in graph[now]:
            cost = distance[now] + j[1]
            if cost < distance[j[0]]:
                distance[j[0]] = cost

dijkstra(start)

def dijkstra2(start):
    q = []
    heapq.heappush(q, (0, start))
    dist, now = heapq.headpop(q)

    if distance[now] < dist:
        continue

    for i in graph[now]:
        cost = dist + i[1]
        if cost < distance[i[0]]:
            distance[i[0]] = cost
            heapq.heappush(q, (cost, i[0]))


# 최단 거리 출력
for i in range(n-1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])