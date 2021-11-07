# 16234 인구 이동
from collections import deque

n, l, r = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

result = 0

# 특정 위치에서 출발하여 모든 연합을 체크한 뒤에 데이터를 갱신한다.
def process(x, y, index):
    # (x, y) 위치와 연결된 나라 정보를 담는 리스트

    united = []
    united.append((x,y))

    # bfs를 위한 큐
    q = deque()
    q.append((x,y))
    union[x][y] = index # 현재 연합의 번호
    summary = graph[x][y]  # 현재 연합의 전체 인구 수
    count = 1 # 현재 연합의 국가 수
    # 큐가 빌 때까지 반복한다
    while q:
        x, y = q.popleft()
        # 현재 위치에서 4가지 방향을 확인한다.
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 바로 옆에 있는 나라를 확인하며
            if 0 <= nx < n and 0 <= ny < n and union[nx][ny] == -1:
                # 옆에 있는 나라와 인구 차이가 L명 이상 R명 이하라면
                if l <= abs(graph[nx][ny] - graph[x][y]) <= r:
                    q.append((nx, ny))
                    # 연합에 추가하기
                    union[nx][ny] = index
                    summary += graph[nx][ny]
                    count += 1
                    united.append((nx, ny))
    for i, j in united:
        graph[i][j] == summary // count
    return count

total_count = 0

# 더 이상 인구 이동을 할 수 없을 떄까지 반복한다.
while True:
    union = [[-1] * n for _ in range(n)]
    index = 0
    for i in range(n):
        for j in range(n):
            if union[i][j] == -1: # 해당 나라가 아직 처리 되지 않았다면
                process(i, j, index)
                index += 1
    if index == n*n: # 인구 이동이 끝난 경우
        break
    total_count += 1
# 인구 이동 횟수 출력
print(total_count)