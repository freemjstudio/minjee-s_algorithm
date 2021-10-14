# 13023

n, m = map(int, input().split())
graph = [[] for i in range(n)]
visited = [False] * n # 노드 방문을 기록한다
stack = []
finished = False

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# dfs 로 풀어야 한다 ㅎ.. 그리고 출발점은 0이어야 한다.
def dfs(start, depth):
    global finished
    visited[start] = True
    if depth == 4:
        finished = True
        return

    for node in graph[start]:
        if not visited[node]:
            dfs(node, depth+1)
            visited[node] = False# 13023

n, m = map(int, input().split())
graph = [[] for i in range(n)]
visited = [False] * n # 노드 방문을 기록한다
stack = []
finished = False

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# dfs 로 풀어야 한다 ㅎ.. 그리고 출발점은 0이어야 한다.
def dfs(start, depth):
    global finished
    visited[start] = True
    if depth == 4:
        finished = True
        return

    for node in graph[start]:
        if not visited[node]:
            dfs(node, depth+1)
            visited[node] = False

for i in range(n):
    dfs(i, 0)
    visited[i] = False # 오ㅙ ????
    if finished == True:
        break

if finished:
    print(1)
else:
    print(0)

for i in range(n):
    dfs(i, 0)
    visited[i] = False # 오ㅙ ????
    if finished == True:
        break

if finished:
    print(1)
else:
    print(0)
