# 1389
from collections import deque


N, M = map(int, input().split())
graph = [[] * (N+1) for _ in range(N+1)]
for _ in range(M): # 친구 관계의 수만큼 반복하여 입력 받는다 !
    A, B = map(int, input().split())
    graph[A].append(B)
    graph[B].append(A)

def bfs(graph, start):
    num = [0] * (N+1) # 이게 bacon 수 저
    queue = deque()
    visited[start] = 1
    queue.append(start)
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if visited[i] == 0: # if the vertex is unvisited
                num[i] = num[v] + 1
                queue.append(i)
                visited[i] = 1
    return sum(num)

result = []

for i in range(1,N+1):
    visited = [0 for _ in range(N+1)]
    result.append(bfs(graph, i))

print(result.index(min(result))+1)



















