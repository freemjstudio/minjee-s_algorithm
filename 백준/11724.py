# 11724 연결요소의 개수
import sys
sys.setrecursionlimit(10000)

input = sys.stdin.readline
N, M = map(int, input().split())
adj_list = [[] for i in range(N+1)] # 인접 리스트 정점의 개수만큼 stack
visit = [False] * (N+1)
count = 0

for _ in range(M):
    x, y = map(int, input().split())
    adj_list[x].append(y)
    adj_list[y].append(x)

def dfs(v):
    visit[v] = True # start node checked as visited

    for edge in adj_list[v]:
        if not visit[edge]:
            dfs(edge)

for i in range(1, N+1):
    if not visit[i]:
        dfs(i)
        count += 1

print(count)

### bfs로 풀이 ??

def bfs(v):
    







