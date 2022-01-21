# 18352 특정 거리의 도시 찾기
from collections import deque

n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n+1)]
distance = [-1] * (n+1) # 최단거리 계산을 위한 리스트


for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

def bfs(start):
    q = deque()
    q.append(start)
    distance[start] = 0
    while q:
        now = q.popleft()
        for i in graph[now]:
            if distance[i] == -1: # 왜 나는 visit된지 안된지 여부를 체크를 안했는가 ? 왜 방문 여부를 체크 해야 하는가 이 문제에서
                distance[i] = distance[now] + 1
                q.append(i)
check = False
bfs(x)
for i in range(1, n+1):
    if distance[i] == k:
        print(i)
        check = True

if check == False:
    print(-1)

