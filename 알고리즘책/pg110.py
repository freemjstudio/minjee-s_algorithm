n = int(input())
data = list(input().split())

# L R U D
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

x = 1
y = 1 # 현재 위치
for plan in data:
    for i in len(move_types):
        if move_types[i] == plan:
            nx = x + dx[i]
            ny = y + dy[i]
    # 공간을 넘어가면 무시해야 한다
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    x, y = nx, ny

print(x, y)