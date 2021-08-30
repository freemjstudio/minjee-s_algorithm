N = int(input())
M = int(input())
graph = [[]*(N+1) for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

cnt = 0
visited = [0]*(N+1)
def dfs(start):
    global cnt
    visited[start] = 1
    for i in graph[start]:
        if visited[i] == 0: # 들리지 않은 정점인 경우에
            dfs(i)
            cnt += 1
dfs(1)
print(cnt)

N = int(input())
T = int(input())
s = [[0]*n for i in range(N)]
visit = [0 for i in range(N)]

for i in range(T):
    a, b = map(int, input().split())
    s[a-1][b-1] = 1
    s[b-1][a-1] = 1

def dfs(v):
    visit[v] = 1
    for i in range(N):
        if s[v][i] == 1 and visit[i] == 0:
            dfs(i)

dfs(0)
cnt = 0
for i in range(1,N):
    if visit[i] == 1:
        cnt += 1
print(cnt)