import sys
from collections import deque

grid = [list(map(int, sys.stdin.readline().split())) for _ in range(19)]
dxs = [
    [0, 0],  # 좌우
    [-1, 1],  # 상하
    [-1, 1],  # 대각선_좌우
    [-1, 1]  # 대각선_우좌
]
dys = [
    [-1, 1],  # 좌우
    [0, 0],  # 상하
    [-1, 1],  # 대각선_좌우
    [1, -1]  # 대각선_우좌
]
pos_x, pos_y = 19, 19

visited_b = [[0] * 19 for _ in range(19)]
for i in range(19):
    for j in range(19):
        visited_b[i][j] = [False, False, False, False]

visited_w = [[0] * 19 for _ in range(19)]
for i in range(19):
    for j in range(19):
        visited_w[i][j] = [False, False, False, False]

q = deque()


def in_range(x, y):
    return 0 <= x < 19 and 0 <= y < 19


def can_go(x, y, type, dir):
    if not in_range(x, y): return False
    if grid[x][y] != type: return False
    if type == 1 and visited_b[x][y][dir]: return False
    if type == 2 and visited_w[x][y][dir]: return False
    return True


def push(x, y, type, dir):
    q.append((x, y, type, dir))
    if type == 1:
        visited_b[x][y][dir] = True
    else:
        visited_w[x][y][dir] = True


def bfs(x, y, type, dir):
    global pos_x, pos_y
    global q
    pos_x, pos_y = x, y
    push(x, y, type, dir)
    cnt = 1

    while q:
        if cnt >= 6: break
        x, y, type, dir = q.popleft()

        for i in range(2):
            new_x, new_y = x + dxs[dir][i], y + dys[dir][i]
            if can_go(new_x, new_y, type, dir):
                push(new_x, new_y, type, dir)
                cnt += 1
                if pos_y > new_y:
                    pos_x = new_x
                    pos_y = new_y
                elif pos_y == new_y:
                    pos_x = min(pos_x, new_x)

    q = deque()
    if cnt == 5: return True
    return False


flag = False
for i in range(19):
    for j in range(19):
        if grid[i][j] != 0:
            type = grid[i][j]
            for k in range(4):
                result = bfs(i, j, type, k)
                if result:
                    flag = True
                    break
        if flag: break
    if flag: break

if flag:
    print(grid[pos_x][pos_y])
    print(pos_x + 1, pos_y + 1)
else:
    print(0)
