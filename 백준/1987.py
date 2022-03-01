# 1987 알파벳
import sys

r, c = map(int, sys.stdin.readline().split())
array = [list(map(lambda x:ord(x)-65, input().rstrip())) for _ in range(r)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

count = 1
alphabet = [0] * 26

def dfs(x, y, cnt):
    global count
    count = max(cnt, count)

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < r and 0 <= ny < c and alphabet[array[nx][ny]] != 1:
                alphabet[array[nx][ny]] = 1
                dfs(nx, ny, cnt+1)
                alphabet[array[nx][ny]] = 0

alphabet[array[0][0]] = 1

dfs(0, 0, count)
print(count)