N = int(input())
x,y = 1,1
plans = input().split()
# L R U D
dx = [0,0,-1,1]
dy = [-1,1,0,0]
move_types = ['L','R','U','D']

# 이동 계획을 하나씩 확인
for plan in plans:
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
        # 공간을 벗어나는 경우는 무시한다
        if nx < 1 or ny < 1 or nx > N or ny > N:
            continue
        x,y = nx,ny # 이동하기

print(x,y)


