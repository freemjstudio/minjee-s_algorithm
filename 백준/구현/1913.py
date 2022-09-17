# 1913

n = int(input())
find = int(input()) # 찾고자 하는 숫자
find_x, find_y = 0, 0
array = [[0]*n for _ in range(n)]

# 방향 : 아래, 오른쪽, 위, 왼쪽
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
dir = 0
now = 0
count = n*n
x, y = 0, 0
array[x][y] = count
count -= 1

while count > 0:
    nx = x + dx[dir]
    ny = y + dy[dir]
    if 0 <= nx < n and 0 <= ny < n and array[x][y] == 0:
        array[nx][ny] = count
        if count == find:
            find_x, find_y = nx, ny
        count -= 1
        x, y = nx, ny
    else:
        dir = (dir+1)%4



# 표 출력하기
for i in range(n):
    for j in range(n):
        print(array[i][j], end=" ")
        if array[i][j] == find:
            find_x, find_y = i, j
    print()
print(find_x+1, find_y+1)