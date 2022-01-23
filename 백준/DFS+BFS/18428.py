# 감시 피하기
from itertools import combinations


n = int(input())
data = []
teacher = []
space = [] # 빈 공간
for i in range(n):
    data.append(list(input().split()))
    for j in range(n):
        if data[i][j] == 'T':
            teacher.append((i, j))
        if data[i][j] == 'X':
            space.append((i, j))


 # 3개 뽑기

def check(x, y, dir): # 선생님
    if dir == 0: # left
        while y >= 0:
            if data[x][y] == "S":
                return True
            if data[x][y] == "O":
                return False
            y -= 1 # 왼쪽으로 이동

    if dir == 1: # right
        while y < n:
            if data[x][y] == "S":
                return True
            if data[x][y] == "O":
                return False
            y += 1
    if dir == 2: # up
        while x >= 0:
            if data[x][y] == "S":
                return True
            if data[x][y] == 'O':
                return False
            x -= 1
    if dir == 3: # down
        while x < n:
            if data[x][y] == 'S':
                return True
            if data[x][y] == 'O':
                return False
            x += 1

def process():
    for x, y in teacher:
        for i in range(4):
            if check(x, y, i): #
                return True
    return False


# 설치 하기
result = False
for case in combinations(space, 3):
    for x, y in case:
        data[x][y] = 'O'
    if not process():
        result = True
        break

    for x, y in case:
        data[x][y] = 'X'

if result:
    print('YES')
else:
    print('NO')