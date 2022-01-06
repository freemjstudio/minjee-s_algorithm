from collections import deque
visited = [False]*9
def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]: # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
        if not visited[i]:
            dfs(graph, i, visited)

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(v)
                visited[i] = True
