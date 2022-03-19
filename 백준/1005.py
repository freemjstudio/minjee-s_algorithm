# 1005 ACM Craft
# 위상정렬
from collections import deque

t = int(input())
for _ in range(t):
    result = 0
    n, k = map(int, input().split())
    indegree = [0]*(n+1) # 모든 노드에 대해 진입차수를 0으로 초기화
    graph = [[] for i in range(n+1)] # node 수만큼 간선의 정보를 담는다.
    cost = list(map(int, input().split()))
    for _ in range(k):
        a, b = map(int, input().split()) # a -> b
        # a에서 b로 이동가능
        graph[a].append(b)
        # 진입 차수 1 증가
        indegree[b] += 1
    w = int(input()) # 반드시 건설해야 하는 번호 w
    q = deque()
    for i in range(1, n+1):
        if indegree[i] == 0: # 진입 차수가 0이면 q에 넣는다.
            q.append(i)
    while q: # 큐가 빌 때까지 반복
        now = q.popleft()
        result += cost[now-1]
        if now == w:
            break
        for i in graph[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)

    print(result)