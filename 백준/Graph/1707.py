# 이분 그래프
from collections import deque
import sys

for _ in range(int(sys.stdin.readline())):
    v, e = map(int, sys.stdin.readline().split())
    graph = [[] for _ in range(v+1)]
    visited = [0]*(v+1)
    flag = True
    for i in range(e):
        a, b = map(int, sys.stdin.readline().split())
        graph[a].append(b)
        graph[b].append(a)
    group = 1 # group 은 1 과 -1 로 함
    q = deque()

    # bfs
    for i in range(1, v+1):
        if visited[i] == 0:
            q.append(i)
            visited[i] = group
            while q:
                now = q.popleft()
                for j in graph[now]:
                    if visited[j] == 0: # 아직 방문하지 않은 노드의 경우
                        q.append(j)
                        visited[j] = -1 * visited[now]
                    elif visited[j] == visited[now]:
                        flag = False
                        break

    if flag:
        print('YES')
    else:
        print('NO')
