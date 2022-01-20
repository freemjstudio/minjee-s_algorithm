# 3190 뱀

n = int(input())
data = [[0]*(n+1) for _ in range(n+1)]
k = int(input())
for _ in range(k):
    a, b = map(int, input().split())
    data[a][b] = 1
L = int(input())
info = []
for _ in range(L):
    t, c = input().split()
    info.append((int(t), c))

count = 0
# 동 남 서 북
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def turn(direction, c):
    if c == "L": # 왼쪽
        (direction -1) %4
    else:
        (direction +1) %4
    return direction

def simulate():
    x, y = 1, 1 # 뱀의 위치
    data[x][y] = 2
    direction = 0 # 동쪽
    time = 0
    index = 0
    q = [(x, y)] # 뱀이 차지하는 위치 정보 - 꼬리가 앞쪽
    while True:
        nx = x + dx[direction]
        ny = y + dy[direction]
        if 1 <= nx and nx <= n and 1 <= ny and ny <= n and data[nx][ny] != 2:
            if data[nx][ny] == 0:
                data[nx][ny] = 2
                q.append((nx, ny))
                px, py = q.pop(0)
                data[px][py] = 0
            if data[nx][ny] == 1:
                data[nx][ny] = 2
                q.append((nx, ny))
        else:
            time += 1
            break
        x, y = nx, ny
        time += 1
        if index < L and time == info[index][0]: # 회전할 시간이 되면 회전한다.
            direction = turn(direction, info[index][1])
            index += 1
    return time
print(simulate())

