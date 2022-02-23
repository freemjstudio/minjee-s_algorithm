# 10971 외판원순회 2

n = int(input())
graph = [[0]*(n+1)]
INF = int(1e9)

for _ in range(n):
    graph.append([0]+list(map(int, input().split())))

def dijkstra(start):
    visited = [False]*(n+1)
    distance = [INF]*(n+1)

