INF = int(1e9)
n, m = map(int, input().split())
graph = [[INF]*(n+1) for i in range(n+1)]

# 자기 자신은 최단거리 0으로 초기화
for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            graph[a][b] = 0

# 입력 받기
for i in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1
x, k  = map(int, input().split())

for i in range(1, n+1):
    for j in range(1, n+1):
        for k in range(1, n+1):
            graph[j][k] = min(graph[j][k],graph[j][i]+graph[i][k])

# 수행된 결과를 출력한다
distance = graph[1][k] + graph[k][x]

if distance == INF:
    print(-1)
else:
    print(distance)
