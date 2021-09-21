# 04.구현 - (3) 게임 개발

# 입력 받기
N, M = map(int, input().split())
x,y,dir = map(int, input().split()) # 좌표 (x,y) dir 는 방향

d = [[0]*M for _ in range(N)] # 방문한 위치를 저장하기 위해서 0으로 초기화 한다.

# 입력된 맵 정보
array = []
for i in range(N):
    array.append(list(map(int, input().split())))

count = 1 # 맨 처음 위치도 카운트 하므로!
# 이동
dx = [-1,0,1,0] #  북 동 남 서
dy = [0,1,0,-1]


def turn_left():
    global dir
    dir -= 1
    if dir == -1:
        dir = 3

turn_time = 0

while True:
    turn_left() # 왼쪽으로 회전하기
    nx = x + dx[dir]
    ny = y + dy[dir]

    if d[nx][ny] == 0 and array[nx][ny] == 0:
        d[nx][ny] = 1 # 방문했다는 표시를 해준다 !!
        x = nx
        y = ny
        count += 1 # 이동 한번 했당
        turn_time = 0
        continue

    # 회전한 이후에 정면에 가보지 않은 칸이 없거나 바다인 경우
    else:
        if turn_time == 4:
            nx = x - dx[dir]
            ny = y - dy[dir]

            if array[nx][ny] == 0: # 뒤로 이동했을 때 육지인 경우 !! 이동한다.
                x = nx
                y = ny
            else: # 바다인경우
                break # 못간당..
            turn_time = 0
            
print(count)


