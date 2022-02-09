# 1865 웜홀
INF = int(1e9)
t = int(input())

def solve(start):

    distance[start] = 0

    for i in range(1, n+1):
        for j in range(1, n+1):
            for end, cost in graph[j]:
                if distance[end] > distance[j] + cost:
                    distance[end] = distance[j] + cost
                    if i == n:
                        return False
    return True

for _ in range(t):
    n, m, w = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    distance = [INF] * (n + 1)
    for i in range(m):
        start, end, value = map(int, input().split())
        graph[start].append((end, value))
        graph[end].append((start, value))

    for j in range(w):
        start, end, value = map(int, input().split())
        graph[start].append((end, -value)) # start -> end 방향으로만 존재 !

    result = solve(1)
    if not result:
        print('YES')
    else:
        print('NO')