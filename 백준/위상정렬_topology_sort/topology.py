from collections import deque

v, e = map(int, input().split())
graph = [[] for _ in range(v+1)]
indegree = [0] * (v+1) # 진입차수는 모두 0으로 초기화

for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

def topology_sort():
    result = []
    queue = deque()

    for i in range(1, v+1):
        if indegree[i] == 0: # 진입차수가 0이면 queue에 집어넣기
            queue.append(i)

    while queue: # queue 가 빌 때까지
        now = queue.popleft()
        result.append(now)
        for i in graph[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                queue.append(i)
    return result

result = topology_sort()
for i in result:
    print(i, end=' ')
