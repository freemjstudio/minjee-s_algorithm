# 11660 구간 합구하기
import sys

n, m = map(int, sys.stdin.readline().split())
graph = [[0]*(n+1)]
for _ in range(n):
    graph.append([0] + list(map(int, sys.stdin.readline().split())))


# column
for i in range(1, n+1):
    for j in range(1, n):
        graph[i][j+1] += graph[i][j]

# row
for j in range(1, n+1):
    for i in range(1, n):
        graph[i+1][j] += graph[i][j]

for _ in range(m):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    result = graph[x2][y2] - graph[x1-1][y2] - graph[x2][y1-1] + graph[x1-1][y1-1]
    print(result)
