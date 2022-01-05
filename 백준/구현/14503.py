# 14503  로봇 청소기

dx = [-1,0,1,0] # 북동남서로 고치기 !
dy = [0,1,0,-1]

n, m = map(int, input().split())
x, y, t = map(int, input().split())
array = [] # 칸
count = 0

for i in range(n):
    array.append(list(map(int, input().split())))

def clean(x, y, t):
    global count
    if array[x][y] == 0:
        array[x][y] = 2 # is visited
        count += 1
    for i in range(4):
        nt = (t + 3)%4 # 이게 어느정도 핵심이다 ! 현재 바라보고 있는 방향에서 좌측 회전을 한 후 새로운 t
        nx = x + dx[nt]
        ny = y + dy[nt]
        if array[nx][ny] == 0:
            clean(nx, ny, nt)
            return
        t = nt # t는 보존하려고 다시 둔다
    nt = (t+2) % 4 # 뒤로 이동을 위해 사용 !
    nx = x + dx[nt]
    ny = y + dy[nt]
    if array[nx][ny] == 1:
        return
    clean(nx, ny, t) # 뒷칸이 벽이 아닌 경우에 바라보는 방향 그대로 뒤로 한칸 이동시키기


clean(x,y,t)

print(count)