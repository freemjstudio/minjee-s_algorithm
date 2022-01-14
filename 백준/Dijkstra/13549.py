from collections import deque
n, k = map(int, input().split())
INF = int(1e9)
MAX = 100001
visited = [False] * MAX
distance = [INF] * MAX

q = deque()
q.append(n)
distance[n] = 0
visited[n] = True
while q:
    now = q.popleft()
    if now*2 < MAX and visited[now*2] == False:
        q.append(now*2)
        visited[now*2] = True
        distance[now*2] = distance[now]
    if now + 1 < MAX and visited[now+1] == False:
        q.append(now+1)
        visited[now+1] = True
        distance[now+1] = distance[now] + 1
    if now - 1 >= 0 and visited[now-1] == False:
        q.append(now-1)
        visited[now-1] = True
        distance[now-1] = distance[now] + 1
print(distance[k])