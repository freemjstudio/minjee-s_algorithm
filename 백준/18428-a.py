from itertools import combinations

n = int(input())
board = [] # 복도의 정보 n*n
teachers = [] # 선생님 위치 정보
spaces = [] # 모든 빈 공간의 정보 이후에 조합 라이브러리 사용해서 3개씩 뽑을거니까 따로 저장해둠

for i in range(n):
    board.append(list(input().split()))
    for j in range(n):
        if board[i][j] == 'T':
            teachers.append((i, j))
        if board[i][j] == 'X':
            spaces.append((i, j))

def watch(x, y, dir):
    if dir == 0: # 왼쪽으로 감시하
        while y >= 0:
            if board[x][y] == 'S':
                return True
            if board[x][y] == 'O':
                return False
            y -= 1

    if dir == 1: # 오른쪽
        while y < n:
            if board[x][y] == 'S':
                return True
            if board[x][y] == 'O':
                return False
            y += 1
    if dir == 2: # 상
        while x >= 0:
            if board[x][y] == 'S':
                return True
            if board[x][y] == 'O':
                return False
            x -= 1

    if dir == 3: #
        while x < n:
            if board[x][y] == 'S':
                return True
            if board[x][y] == 'O':
                return False
            x += 1
    return False

# 장애물 설치 이후에 한명이라도 학생이 있는지 watch()
def process():
    for x, y in teachers:
        for i in range(4):
            if watch(x, y, i):
                return True
    return False

find = False # 정답 flag

for data in combinations(spaces, 3):
    # 장애물 설치하기
    for x, y in data:
        board[x][y] == 'O'
    if not process():
        find = True
        break
    for x, y, in data:
        board[x][y] = 'X'

if find:
    print('YES')
else:
    print('NO')