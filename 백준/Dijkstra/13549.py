from collections import deque
MAX = 100001
n, k = map(int, input().split())
INF = int(1e9)
distance = [INF] * MAX
visited = [False] * MAX
q = deque()
q.append(n)
visited[n] = True
distance[n] = 0

while q:
    now = q.popleft()
    if now *2 <= MAX and visited[now*2] == False:
        q.appendleft(now*2)
        distance[now*2] = distance[now]
        visited[now*2] = True
    if now+1 < MAX and visited[now+1] == False:
        q.append(now+1)
        distance[now+1] = distance[now] + 1
        visited[now+1] = True
    if now-1 >= 0 and visited[now-1] == False:
        q.append(now-1)
        distance[now-1] = distance[now] + 1
        visited[now-1] = True
print(distance[k])