# 12851
from collections import deque
n, k = map(int, input().split())

visited = [[-1, 0] for _ in range(100001)] # (cost , 방법의 개수)

def bfs():
    q = deque()
    q.append(n) # start node 는 n
    visited[n][0] = 0
    visited[n][1] = 1

    while q:
        now = q.popleft()
        for i in [now-1, now+1, now*2]:
            if 0 <= i <= 100000: # 주어진 범위
                if visited[i][0] == -1: # 첫 방문
                    visited[i][0] = visited[now][0] + 1
                    visited[i][1] = visited[now][1] # 방법의 개수
                    q.append(i)

                elif visited[i][0] == visited[now][0] + 1: # 이미 방문했다면, 최단거리인 경우에만 갱신함
                    visited[i][1] += visited[now][1]

bfs()

print(visited[k][0])
print(visited[k][1])
