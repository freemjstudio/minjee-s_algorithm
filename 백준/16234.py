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
    united[x][y] = index # 현재 연합의 번호 할당
    summary = graph[x][y]  # 현재 연합의 전체 인구 수
