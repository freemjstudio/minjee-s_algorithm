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

    # 위상 정렬 알고리즘
    result = []
    q = deque()
    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)

    certain = True # 위상 정렬 결과가 하나인가 ?
    cycle = False # 그래프 내 사이클이 존재하는가

    for i in range(n): # 노드 개수 만큼 반복
        if len(q) == 0:
            cycle = True
            break
        if len(q) >= 2: # 한번에 진입차수가 동일한 두개이상의 노드가 동시에 들어오면 결과가 여러개가 된다
            certain = False
            break
        now = q.popleft()
        result.append(now)
        # 진입차수 갱신
        for j in range(1, n+1):
            if graph[now][j]:
                indegree[j] -= 1
                if indegree[j] == 0:
                    q.append(j)

    # 결과 출력
    if cycle:
        print("IMPOSSIBLE")
    elif not certain:
        print("?")
    else:
        for i in result:
            print(i, end=' ')
        print()
