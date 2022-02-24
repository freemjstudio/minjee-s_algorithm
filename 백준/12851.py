# 12851
from collections import deque
n, k = map(int, input().split())
visited = [[-1, 0] for _ in range(100001)] # (걸린 시간, 방법의 수 )

def bfs():
    q = deque()
    q.append(n)
    visited[n][0] = 0 # start
    visited[n][1] = 1


print(visited[k][0])
print(visited[k][1])