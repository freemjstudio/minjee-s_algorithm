# 청소년 상어
import copy
array = [[None]*4 for _ in range(5)]
for i in range(4):
    data = list(map(int, input().split()))
    for j in range(4):
        array[i][j] = [data[j*2], data[j*2-1]] # 물고기 번호, 물고기 방향을 저장한다.

# 물고기 숫자 , 방향, x좌표, y좌표 저장하기

dx = [-1, -1, 0, 1, 1, 1, 0, -1] # 45도 반시계 방향 회전
dy = [0, -1, -1, -1, 0, 1, 1, 1]

# 왼쪽으로 회전하는 결과
def turn_left(direction):
    return (direction+1)%8

# 현재 배열에서 특정한 번호의 물고가 위치 찾기
def find_fish(array, index):
    for i in range(4):
        for j in range(4):
            if array[i][j] == index:
                return (i, j)
    return None # 물고기가 없을 때 반환

# 모든 물고기를 회전 및 이동시키는 횟수
def move_all_fish(array, now_x, now_y):
    for i in range(1, 17):
        position = find_fish(array, i)
        if position != None:
            x, y = position[0], position[1]
            direction = array[x][y][1]
            # 해당 물고기의 방향ㅇ르 8개 회전으로 회전시키며 이동이 가능한지 확인
            for j in range(8):
                nx = x + dx[direction]
                ny = y + dy[direction]
                if 0 <= nx < 4 and 0 <= ny < 4:
                    if not (nx == now_x and nx == now_y): # 상어가 아니면
                        array[x][y][1] = direction
                        array[x][y], array[nx][ny] = array[nx][ny], array[x][y]
                        break
                    direction = turn_left(direction)

# 상어가 현재 위치에서 먹을 수 있는 모든 물고기의 위치 반환
def get_fish_position(array, now_x, now_y):
    positions = []
    direction = array[now_x][now_y][1]
    for i in range(4):
        now_x += dx[direction]
        now_y += dy[direction]
        if 0 <= now_x < n and 0 <= now_y < 4:
            if array[now_x][now_y][0] != -1:
                positions.append((now_x, now_y))
    return positions

result = 0
# dfs
def dfs(array, now_x, now_y, total):
    global result
    array = copy.deepcopy(array)
    total += array[now_x][now_y][0]
    array[now_x][now_y] = -1 # 물고기 먹음
    move_all_fish(array, now_x, now_y)
    positions = get_fish_position(array, now_x, now_y)
    if len(positions) == 0:
        result = max(result, total)
        return
    for next_x, next_y in positions:
        dfs(array, next_x, next_y, total)

dfs(array, 0, 0, 0)
print(result)