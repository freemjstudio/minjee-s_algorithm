# 1697
from collections import deque

N, K = map(int,input().split())

MAX = 10 ** 5
dist = [0] * (MAX+1)

def bfs():
    q = deque()
    q.append(N)
    while q:
        x = q.popleft()
        if x == K:
            print(dist[x])
            break
        for nx in (x-1, x+1, x*2):
            if 0 <= nx <= MAX and not dist[nx]: # not visited node
                dist[nx] = dist[x] + 1 # 1초 소요된다
                q.append(nx) # 방문표시한 노드를 큐에 삽입한다

bfs()

