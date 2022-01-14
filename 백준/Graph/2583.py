# 2583 영역 구하기
import sys
sys.setrecursionlimit(10000)

m, n, k = map(int, input().split())
array = [[0]*(n) for _ in range(m)]

for _ in range(k):
    a, b, c, d = map(int, input().split())
    for i in range(b, d):
        for j in range(a, c):
            array[i][j] = 1 # 직사각형

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
result = []
temp = 0
def dfs(x, y):
    global temp
    array[x][y] = 1
    temp += 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < m and 0 <= ny < n and array[nx][ny] == 0:
            dfs(nx, ny)
    return temp

for i in range(m):
    for j in range(n):
        if array[i][j] != 1:
            temp = dfs(i, j)
            if temp != 0:
                result.append(temp)
                temp = 0

result.sort()
print(len(result))
for i in result:
    print(i, end=' ')
