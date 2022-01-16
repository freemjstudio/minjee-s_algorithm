from collections import deque

for _ in range(int(input())):
    n = int(input())
    indegree = [0] * (n+1)
    graph = [[False] * (n+1) for _ in range(n+1)]
    data = list(map(int, input().split())) # 작년 순위 정보 입력
    for i in range(n):
        for j in range(i+1, n):
            graph[data[i]][data[j]] = True # 방향 그래프 i -> j
            indegree[data[j]] += 1 # j 진입차수 1 증가
    m = int(input())
    for i in range(m):
        a, b = map(int, input().split())
        # 간선의 방향 뒤집기
        if graph[a][b]:
            graph[a][b] = False
            graph[b][a] = True
            indegree[a] += 1
            indegree[b] -= 1
        else:
            graph[a][b] = True
            graph[b][a] = False
            indegree[a] -= 1
            indegree[b] += 1
    # 위상 정렬
    result = []
    q = deque()

    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)

    certain = True # 위상정렬 수행 결과가 하나인가
    cycle = False
    for i in range(n):
        if len(q) == 0: # 큐가 비어있다면 사이클이 발생했다는 의미
            cycle = True
            break
        if len(q) >= 2: # 큐의 원소가 2개 이상이면 정렬 결과가 여러개
            certain = False
            break

        now = q.popleft()
        result.append(now)
        for j in range(1, n+1):
            if graph[now][j]:
                indegree[j] -= 1
                if indegree[j] == 0:
                    q.append(j)
    if cycle:
        print("IMPOSSIBLE")
    elif not certain:
        print("?")
    else:
        for i in result:
            print(i, end=' ')
        print()