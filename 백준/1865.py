# 1865 웜홀

for _ in range(int(input())):
    n, m, w = map(int, input().split())
    graph = [[] * (m+1) for _ in range(n+1)]

    for i in range(m):
        start, end, value = map(int, input().split())
        graph[start].append((end, value))

    for j in range(w):
        start, end, value = map(int, input().split())
        graph[start].append((end, (-1)*value)) # 가중치가 음수이다.
        