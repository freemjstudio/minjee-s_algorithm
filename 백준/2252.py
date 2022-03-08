# 2252

n, m = map(int, input().split())

graph = [[0]*(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a] = b
    