import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
start = int(input())

graph = [[] for _ in range(n)]
# 최단 거리 테이블을 만든다
distance = [INF] * (n+1)
for i in range(m):
    a, b, cost = map(int, input().split())
    graph[a].append((b, cost))

def solve(start):
    q = []
    heapq.heappush(q, (0, start)) # cost, node
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist: # 현재 노드가 이미 처리된 적 있다면 (이미 최단 경로인 경우)
            continue

        for i in graph[now]:
            cost = dist + i[1] # i  (b, cost)
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

solve(start)

for i in range(1, n+1):
    if distance[i] == "INF": # 도달할 수 없는 경우
        print("INF")
    else:
        print(distance[i])