# 어른 상어
n, m, k = map(int, input().split())

graph = []  # 격자 정보
for i in range(n):
    graph.append(list(map(int, input().split())))

directions = list(map(int, input().split()))  # 상어의 방향
priority = [[] for _ in range(m)]  # 상어 이동 방향 우선순위
for i in range(m):
    for j in range(4):
        priority[i].append(list(map(int, input().split())))

smell = [[[0, 0]] * n for _ in range(n)]  # (상어 번호, 남은시간)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def update_smell():  # 냄새 정보를 업데이트
    for i in range(n):
        for j in range(n):
            if smell[i][j][1] > 0:
                smell[i][j][1] -= 1

            if graph[i][j] != 0:  # 상어가 존재하면
                smell[i][j] = [graph[i][j], k]


# 현재 남아있는 상어의 수 = num
def move():
    # 이동 결과를 담기 위한 임시 결과 테이블 초기화
    new_graph = [[0] * n for _ in range(n)]
    for x in range(n):
        for y in range(n):
            if graph[x][y] != 0:  # 상어가 존재하면
                direction = directions[graph[x][y] - 1]
                found = False
                for i in range(4):  # 인접 칸 확인하기
                    nx = x + dx[priority[graph[x][y] - 1][direction - 1][i] - 1]
                    ny = y + dy[priority[graph[x][y] - 1][direction - 1][i] - 1]

                    if 0 <= nx and nx < n and 0 <= ny and ny < n:
                        if smell[nx][ny][1] == 0:  # 냄새 x
                            directions[graph[x][y] - 1] = priority[graph[x][y] - 1][direction - 1][i]  # 방향 갱신

                            if new_graph[nx][ny] == 0:  # 상어가 없으면 이동 !
                                new_graph[nx][ny] = graph[x][y]
                            else:  # 상어가 있으면 작은 상어가 남는다
                                new_graph[nx][ny] = min(new_graph[nx][ny], graph[x][y])
                            found = True
                            break
                if found:
                    continue
            # 주변에 모두 냄새가 있는 곳만 있다면 자신의 냄새가 있는 곳으로 이동한다.
            for i in range(4):
                nx = x + dx[priority[graph[x][y] - 1][direction - 1][i] - 1]
                ny = y + dy[priority[graph[x][y] - 1][direction - 1][i] - 1]
                if 0 <= nx and nx < n and 0 <= ny and ny < n:
                    if smell[nx][ny][0] == graph[x][y]:
                        directions[graph[x][y] - 1] = priority[graph[x][y] - 1][direction - 1][i]
                        new_graph[nx][ny] = graph[x][y]
                        break
    return new_graph


time = 0
while True:
    update_smell()
    new_graph = move()
    graph = new_graph  # array 업데이트
    time += 1
    check = True
    for i in range(n):
        for j in range(n):
            if graph[i][j] > 1:
                check = False
    if check:
        print(time)
        break

    if time >= 1000:
        print(-1)
        break

