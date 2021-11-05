# 감시 피하기
from collections import deque
n = int(input())
data = []
teacher = deque()
temp = []

for i in range(n):
    data.append(input().split())

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

for i in range(n):
    for j in range(n):
        if data[i][j] == 'T':
            teacher.append((i, j)) # 선생님의 좌표를 저장한다.

def check():
    while teacher:
        x, y = teacher.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i] # 상하좌우 좌표
            if nx >= 0 and nx < n and ny >= 0 and ny < n and data[nx][ny] != 'O':
                if data[nx][ny] == 'S':
                    return False
                teacher.append((nx, ny))
    return True


def dfs(count):
    if count == 3: # 장애물 3개를 모두 설치했으면
        if check():
            return "YES"
        else:
            count = 0

    # 장애물 3개 설치하기
    for i in range(n):
        for j in range(n):
            if data[i][j] == 'X':
                data[i][j] = 'O' # 장애물 넣기
                dfs(count+1)
                data[i][j] = 'X' # 다시 바꿔주기 ㅋㅋ
                count -= 1
    return "NO"

print(dfs(0))