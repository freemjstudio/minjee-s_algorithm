# 263 이코테
import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

n, m, start = map(int, input().split())
graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c)) # a->b : cost

def dijkstra(start):
    queue = []
    heapq.heappush(queue, (0, start))