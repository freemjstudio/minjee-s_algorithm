# 미세먼지안녕 17144


r, c, t = map(int, input().split())
array = []
up = -1 # x 좌표만 기록
down = -1

for i in range(r):
    array.append(list(map(int, input().split())))

# 공기 청정기 x 좌표 찾기 ( y 좌표는 동일함 )
for i in range(r):
    if array[i][0] == -1:
        up = i
        down = i + 1
        break
# 마세먼지 이동 시키기

def dust():
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    temp_array = [[0]*c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if array[i][j] > 0:
                temp = 0
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if 0 <= nx < r and 0 <= ny < c and array[nx][ny] != -1:
                        temp_array[nx][ny] += array[i][j]//5
                        temp += array[i][j]//5
                array[i][j] -= temp
    for i in range(r):
        for j in range(c):
            array[i][j] += temp_array[i][j]

def air_up():
    dx = [0, -1, 0, 1]
    dy = [1, 0, -1, 0]
    x, y = up, 1
    direct = 0
    before = 0
    while True:
        if x == up and y == 0:    # 공기 청정기 만남
            break
        nx = x + dx[direct]
        ny = y + dy[direct]
        if nx < 0 or nx >= r or ny < 0 or ny >= c:
            direct += 1
            continue
        array[x][y], before = before, array[x][y]
        x, y = nx, ny



def air_down():
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    x, y = down, 1
    direct = 0
    before = 0
    while True:
        if x == down and y == 0:
            break
        nx = x + dx[direct]
        ny = y + dy[direct]
        if nx < 0 or nx >= r or ny < 0 or ny >= c:
            direct += 1
            continue
        array[x][y], before = before, array[x][y]
        x, y = nx, ny


for _ in range(t):
    dust()
    air_up()
    air_down()


result = 0
for i in range(r):
    for j in range(c):
        if array[i][j] > 0:
            result += array[i][j]

print(result)


