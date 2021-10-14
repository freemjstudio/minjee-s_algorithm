import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())

start = int(input())

graph = [[] for i in range(n+1)] # node 연결 정보를 담는 그래프 리스트
distance = [INF] * (n+1)

# 모든 간선 정보를 입력 받기
for _ in range(m):
    a,b,c = map(int, input().split())
    # a번 노드에서 b번 노드로 가는 비용이 c
    graph[a].append((b,c))

def dijkstra(start):
    q = [] # 우선순위 큐

    heapq.heappush(q ,(0, start))
    # 시작 노드로 가기 위한 최단 경로는 0으로 설정하여 큐에 삽입
    distance[start] = 0
    while q: # queue가 비어 있지 않다면
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue # 현재 노드가 이미 처리된 적이 있는 노드라면 무시

        for i in graph[now]: # 현재 노드와 연결된 다르인접한 노드들을 확인
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost # 현재 노드를 거쳐서 다르노드로 이동하는 거리가 더 짧을 경우
                heapq.heappush(q, (cost, i[0]))

dijkstra(start)























































