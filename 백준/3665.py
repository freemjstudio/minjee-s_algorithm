# 3665
from collections import deque

t = int(input())
for _ in range(t):
    n = int(input())
    data = list(map(int, input().split()))
    indegree = [0] * (n+1) # 모든 노드에 대한 진입차수 0으로 초기화
    graph = [[False] * (n+1) for i in range(n+1)]

    # 간선 정보 정리하기
    for i in range(n):
        for j in range(i+1, n):
            graph[data[i]][data[j]] = True # 한 방향 간선 정보
            indegree[data[j]] += 1 # 진입차수 정보 저장

    # 올해 변경된 순위 입력
    m = int(input())

    # 순서가 바뀐 간선
    for i in range(m):
        a, b = map(int, input().split())
        # 간선의 방향 뒤집기
        if graph[a][b]: # a <- b
            graph[a][b] = False
            graph[b][a] = True # b <- a
            indegree[a] += 1
            indegree[b] -= 1
        else: # b -> a
            graph[a][b] = True
            graph[b][a] = False # b <- a
            indegree[a] -= 1
            indegree[b] += 1
