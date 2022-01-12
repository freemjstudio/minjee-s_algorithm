n, m = map(int, input().split()) # 회사 개수 , 경로 개수
INF = int(1e9)
graph = [[INF]*(n+1) for _ in range(n+1)]

for i in range(n):
    for j in range(n):
        if i == j:
            graph[i][j] = 0

for i in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

x, k = map(int, input().split())

for k in range(n):
    for a in range(n):
        for b in range(n):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

distance = graph[1][k] + graph[k][x]

if distance >= INF:
    print("-1")
else:
    print(distance)
    