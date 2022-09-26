# https://www.acmicpc.net/problem/1697
from collections import deque

n, k = map(int, input().split())
MAX = 100000
visited = [False] * (MAX+1)

def bfs():
    queue = deque()
    time = 0
    queue.append((n, time))
    while queue:
        now, t = queue.popleft()
        if now == k:
            print(t)
            break

        for nx in [now+1, now-1, now*2]:
            if 0 <= nx <= MAX and not visited[nx]:
                visited[nx] = True
                queue.append((nx, t+1))

bfs()
