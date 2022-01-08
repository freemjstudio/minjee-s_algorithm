# 10451
import sys
sys.setrecursionlimit(10**5)

t = int(input())

def dfs(v):
    visited[v] = 1
    next = array[v]
    if visited[next] == 0:
        dfs(next)

for i in range(t):
    n = int(input())
    result = 0
    array = [0]+list(map(int, input().split()))
    visited = [0]*(n+1)
    for i in range(1, n+1):
        if visited[i] == 0: 
            dfs(i)
            result += 1
    print(result)