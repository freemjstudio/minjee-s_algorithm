# 14502 연구소

n, m = map(int, input().split())
board = []
temp = [[0]*m for _ in range(n)] # 벽을 설치한 다음의 리스트

for i in range(n):
    board.append(list(map(int, input().split())))

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def virus(x,y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= 0 and nx < n and ny >= 0 and ny < m:
            if temp[nx][ny] == 0 :
                temp[nx][ny] = 2
                virus(nx,ny)

def get_safe():
    score = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                score += 1
    return score

result = 0

def dfs(count):
    global result
    if count == 3: # 외벽 설치 3개 했을 때 바이러스 퍼트려서 확인한다.
        for i in range(n):
            for j in range(m):
                temp[i][j] = board[i][j]

        for i in range(n):
            for j in range(m):
                if temp[i][j] == 2:
                    virus(i,j)

        result = max(result, get_safe())

    # 외벽 설치하기
    for i in range(n):
        for j in range(m):
            if board[i][j] == 0:
                count += 1
                board[i][j] = 1
                dfs(count)
                board[i][j] = 0
                count -= 1

dfs(0)
print(result)
