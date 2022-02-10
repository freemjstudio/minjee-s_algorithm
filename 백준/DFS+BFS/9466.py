# 9466 텀프로젝트
from collections import deque
INF = int(1e9)
n, m, x = map(int, input().split()) # N M X
graph = [[] for _ in range(n+1)]
dist = [-1]*(n+1) # 최단거리 기록
dist[x] = 0 # 파티 개최하는 곳

for i in range(m):
    s, e, t = map(int, input().split())
    graph[s].append((e, t))





for i in range(1, n+1):
    if i == x:
        continue
    else:
        bfs(i)



