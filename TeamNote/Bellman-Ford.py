INF = int(1e9)

n, m = map(int, input().split())
edges = []
dist = [INF] * (n+1)

for i in range(m):
    start, end, weight = map(int, input().split())
    edges.append((start, end, weight))

def bellman_ford(start):
    dist[start] = 0
    for i in range(n):
        for j in range(m):
            s = edges[j][0] # 현재 노드
            e = edges[j][1] # 도착 지점
            w = edges[j][2] # weight

            if dist[s] != INF and dist[e] > dist[s] + w:
                dist[e] = dist[s] + w
                if i == n-1:
                    return True # n-1 번 이후에도 값이 갱신되면 사이클이 있다 !
    return False

print(bellman_ford(0))