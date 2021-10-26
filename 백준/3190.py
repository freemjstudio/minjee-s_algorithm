n = int(input())
k = int(input())

board = [[0] * (n+1) for _ in range(n+1)]
rotate = [] # 회전 정보

for _ in range(k):
    x, y = map(int, input().split())
    board[x][y] = 1

l = int(input())

for _ in range(l):
    x, y = input().split()
    rotate.append((int(x), y))

# 처음에 동쪽을 보고 있으니가 동 남 서 북
dx = [0,1,0,-1]
dy = [1,0,-1,0]

def turn(direction, c):
    if c == "L":
        direction = (direction - 1)%4
    else:
        direction = (direction + 1)%4
    return direction

def simulate():
    x, y = 1, 1 # 뱀 머리 위치
    board[x][y] = 2 # 뱀이 존재하는 위치는 2로 표시
    direction = 0 # 처음에는 동쪽을 보고 있음
    time = 0
    index = 0 # 다음에 회전할 정보
    q = [(x,y)] # 뱀이 차지하고 있는 위치 정보
    while True:
        nx = x + dx[direction]
        ny = y + dy[direction]

        if 1 <= nx and nx <= n and 1 <= ny and ny <= n and board[nx][ny] != 2:
            if board[nx][ny] == 0: # 사과가 없다면 이동후에 꼬리 제거
                board[nx][ny] = 2
                q.append((nx, ny))
                px, py = q.pop(0)
                board[px][py] = 0

            if board[nx][ny] == 1:
                board[nx][ny] = 2
                q.append((nx, ny))
        else:
            time += 1
            break
        x, y = nx, ny
        time += 1
        if index < len(rotate) and time == rotate[index][0]: # 회전할 시간인 경우 회전
            direction = turn(direction, rotate[index][1])
            index += 1
    return time

print(simulate())












