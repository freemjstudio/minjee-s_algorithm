import sys
def dfs(v):
    visited[v] = 1
    print(v, end=' ')
    for i in range(1,N+1):
        if visited[i] == 0 and graph[v][i] == 1:
            dfs(i)

def bfs(v):
    queue = [v] # 시작 정점
    visited[v] = 0
    while (queue):
        v = queue[0]
        print(v, end=' ')
        del queue[0]
        for i in range(1,N+1):
            if visited[i] == 1 and graph[v][i] == 1:
                queue.append(i)
                visited[i] = 0


N, M, V = map(int, sys.stdin.readline().split())
visited = [0 for i in range(N+1)]
graph = [[0]*(N+1) for _ in range(N+1)]
for i in range(M):
    start, end = map(int, sys.stdin.readline().split())
    graph[start][end] = 1
    graph[end][start] = 1

dfs(V)
print()
bfs(V)