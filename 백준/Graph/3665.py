from collections import deque

for _ in range(int(input())): # test case 만큼 반복하기
    n = int(input())
    data = list(map(int, input().split()))
    m = int(input())
    graph = [[False]*(n+1) for _ in range(n+1)]
    indegree = [0] * (n + 1)  # 진입 차수
    for i in range(n):
        for j in range(i+1, n):
            graph[data[i]][data[j]] = True # i -> j
            indegree[data[j]] += 1

    for i in range(m):
        a, b = map(int, input().split()) # 그래프 방향 바꿔주기
        if graph[a][b]:
            graph[a][b] = False
            graph[b][a] = True # b -> a
            indegree[a] += 1
            indegree[b] -= 1

        else:
            graph[a][b] = True
            graph[b][a] = False
            indegree[a] -= 1
            indegree[b] += 1

    q = deque()
    result = []
    certain = True  # 결과가 오직 하나인가
    cycle = False # 사이클 판별

    for i in range(1, n+1): # node 수 만큼 판별을 해야 한다. -> q 가 비면, 사이클이 발생했다는 걸 확인
        if indegree[i] == 0:
            q.append(i)

    for i in range(n):
        if len(q) == 0: # 큐가 비어있으면 사이클이 발생했다는 의미
            cycle = True
            break
        if len(q) >= 2:
            certain = False
            break
        now = q.popleft()
        result.append(now)
        for j in range(1, n+1): # 해당 원소와 연결된 노드들의 진입차수에서 -1
            if graph[now][j]: # now -> j 가 true 이면 반환
                indegree[j] -= 1
                if indegree[j] == 0:
                    q.append(j)

    if cycle:
        print("IMPOSSIBLE")
    elif not certain:
        print('?')
    else:
        for i in result:
            print(i, end=' ')






