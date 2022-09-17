# 1913
import sys

n = int(input())
find = int(input()) # 찾고자 하는 숫자
find_x, find_y = 0, 0
array = [[0 for _ in range(n)] for _ in range(n)]

# 방향 : 아래, 오른쪽, 위, 왼쪽
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
direction = 0
now = 0
count = n**2
x, y = 0, 0
array[x][y] = count
count -= 1

while count > 0:
    nx = x + dx[direction]
    ny = y + dy[direction]

    if 0 <= nx < n and 0 <= ny < n and not array[nx][ny]:
        array[nx][ny] = count
        if count == find:
            find_x, find_y = nx, ny
        x, y = nx, ny
        count -= 1
    else:
        direction = (direction+1) % 4


# 표 출력하기
for row in array:
    print(*row)
print(find_x+1, find_y+1)