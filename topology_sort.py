# 위상정렬
from collections import deque

v, e = map(int, input().split())
indegree = [0]* (v+1) # 진입 차수
graph = [[] for i in range(v+1)]

for i in range(e):
    a, b = map(int, input().split())
    indegree[b] += 1
    graph[a].append(b)

def topology_sort(n):
    result = [] # 알고리즘 수행 결과
    queue = deque()
    for i in range(1, v+1):
        if indegree[i] == 0:
            queue.append(i)

    while queue:
        now = queue.popleft()
        result.append(now)
        for i in graph[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                queue.append(i)


