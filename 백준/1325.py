# 1325 효율적인 해킹
from collections import deque

n, m = map(int, input().split())
graph = [[] for i in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[b].append(a)
# bfs/dfs 로 탐색해서 가장 많은 컴퓨터를 거치는 번호를 알아낸다
max_count = 0

# bfs
def bfs(start):
    queue = deque()
    visited = [False] * (n+1)
    visited[start] = True
    queue.append(start)
    count = 1  # 자기 자신
    while queue:
        now = queue.popleft()
        for node in graph[now]:
            if not visited[node]:
                queue.append(node)
                count += 1
                visited[node] = True
    return count

result = []
for i in range(1, n+1):
    temp_count = bfs(i)
    if temp_count > max_count:
        max_count = temp_count
    result.append([i, temp_count])

# 오름차순 출력
for i, count in result:
    if count == max_count:
        print(i, end=' ')