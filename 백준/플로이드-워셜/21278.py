# 호석이 두마리 치킨 ~~

n, m = map(int, input().split())
INF = int(1e9)
graph = [[INF]*(n+1) for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1 # a와 b사이의 거리
    graph[b][a] = 1

# 플로이드 워셜 : 각 건물사이의 최단 거리

for k in range(1, n+1):
    graph[k][k] = 0  # 자기자신 -> 자기자신 : 0
    for i in range(1, n+1):
        for j in range(1, n+1):
            graph[i][j] = min(graph[i][k] + graph[k][j], graph[i][j])

total = INF 
# 치킨집 2개 골라서 브루트 포스로 확인하기
for i in range(1, n+1):
    for j in range(i, n+1):
        cost = 0
        for k in range(1, n+1): # k번쨰 정점에서 i or j 둘중 가까운 치킨집 방문
            cost += min(graph[k][i], graph[k][j])
        if total > cost*2:
            total = cost*2
            answer = [i, j, cost*2]
print(*answer)