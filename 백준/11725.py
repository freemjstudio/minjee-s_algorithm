# 11725 트리의 부모 찾기
import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
parent = [0] * (n+1) # 부모 노드를 저장한다.
graph = [[] for _ in range(n+1)]

for i in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def BFS():
    queue = deque()
    queue.append(1) # root
    while queue:
        node = queue.popleft()
        for i in graph[node]:
            if parent[i] == 0:
                parent[i] = node
                queue.append(i)

BFS()

for i in range(2,n+1):
    print(parent[i])