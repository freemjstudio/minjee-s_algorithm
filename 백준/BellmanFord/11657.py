# 11657 타임 머신

n, m = map(int, input().split())
INF = int(1e9)
dist = [INF] * (n+1)
edges = []
for i in range(m):
    a, b, cost = map(int, input().split())
    edges.append((a, b, cost))

dist[1] = 0

def solve():
    for i in range(n):
        for j in range(m): # edges 확인하기 !!!!
            start, end, cost = edges[j][0], edges[j][1], edges[j][2]

            if dist[start] != INF and dist[end] > dist[start] + cost:
                dist[end] = dist[start] + cost
                if i == n-1:
                    return False
    return True

if solve() == False:
    print(-1)
else:
    for i in range(2, n+1):
        if dist[i] == INF:
            print(-1)
        else:
            print(dist[i])