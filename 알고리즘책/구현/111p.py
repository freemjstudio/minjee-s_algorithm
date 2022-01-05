n = int(input())
array = list(map(input().split()))
x = 1
y = 1
dx = [0,0,-1,1]
dy = [-1,1,0,0]

types = ['L','R','U','D']
for i in array:
    # ㅇㅣ동 후 좌표 구하기
    for j in range(4): # 0 1 2 3
        if i == types[j]:
            nx = x + dx[i]
            ny = y + dy[i]
        if nx < 1 or nx < n or ny < 1 or ny > n:
            continue
        x, y = nx, ny # 이동 수행

print(x, y)