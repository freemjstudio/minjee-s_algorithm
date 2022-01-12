n, m = map(int, input().split())
array = []
for i in range(n):
    array.append(list(map(int, input().split())))

dx = [0,0,1,-1]
dy = [1, -1, 0,0]
types = [[[0, 1], [0, 2], [-1, 1]],
         [[0, 1], [0, 2], [1, 1]],
         [[1, 0], [2, 0], [1, 1]],
         [[1, 0], [1, -1], [2, 0]]]


visit = [[0]*m for i in range(n)]
result = 0

def dfs(x, y, cnt, num):
    global result
    if cnt == 4:
        result = max(result, num)
        return
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and visit[nx][ny] == 0:
            visit[nx][ny] = 1
            dfs(nx, ny, cnt+1, num + array[nx][ny])
            visit[nx][ny] = 0

def type(x,y):
    global result
    for type in types:
        try:
            num = array[x][y] + array[x + type[0][0]][y+type[0][1]] + array[x + type[1][0]][y+ type[1][1]] + array[x+type[2][0]][y+type[2][1]]
        except:
            num = 0
        result = max(num, result)

for i in range(n):
    for j in range(m):
        visit[i][j] = 1
        dfs(i, j, 1, array[i][j])
        visit[i][j] = 0
        type(i, j)
print(result)