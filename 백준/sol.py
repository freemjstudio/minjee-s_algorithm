# 플로이드
INF = int(1e9)
n = int(input()) # 도시 개수
m = int(input()) # 버스 개수
graph = [[INF]*(n+1) for _ in range(n+1)]
for i in range(m):
    a, b, cost = map(int, input().split())
    if cost < graph[a][b]: #  -> 시작 도시와 도착 도시를 연결하는 노선은 하나가 아닐 수 있다 !
        graph[a][b] = cost

for i in range(1, n+1):
    for j in range(1, n+1):
        if i == j:
            graph[i][j] = 0

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])

for i in range(1, n+1):
    for j in range(1, n+1):
        if graph[i][j] == INF:
            print(0, end=' ')
        else:
            print(graph[i][j], end=' ')
    print()