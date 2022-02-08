# 1865 웜홀
INF = int(1e9)
for _ in range(int(input())):
    n, m, w = map(int, input().split())
    edges = []
    distance = [INF]*(n+1)
    for i in range(m):
        start, end, value = map(int, input().split())
        edges.append((start, end, value))

    for j in range(w):
        start, end, value = map(int, input().split())
        edges.append((start, end, (-1)*value))

    