# 18352
from collections import deque

n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n+1)] # 인접 리스트로 나타내기

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

distance = [-1]*(n+1) # 모든 도시에 대한 최단 거리 초기화
distance[x] = 0

q = deque([x])
while q:
    now = q.popleft()
    for next_node in graph[now]:
        if distance[next_node] == -1:
            distance[next_node] = distance[now] + 1
            q.append(next_node)

check = False
# 최단 거리가 K 인 모든 도시의 번호를 오름차순으로 출력
for i in range(1, n+1):
    if distance[i] == k:
        print(i)
        check = True

if check == False:
    print(-1)
