# 16928 뱀과 사다리 게임
from collections import deque

board = [0] * 101
visited = [False] * 101
snake = dict()
ladder = dict()

def bfs():
    queue = deque([1])
    visited[1] = True
    while queue:
        v = queue.popleft()
        for move in range(1,7):
            check_move = v+move
            if 0 < check_move <=100 and not visited[check_move]:
                if check_move in ladder.keys():
                    check_move = ladder[check_move]
                if check_move in snake.keys():
                    check_move = snake[check_move]

                if not visited[check_move]:
                    queue.append(check_move)
                    visited[check_move] = True
                    board[check_move] = board[v] + 1




N, M = map(int,input().split())
for i in range(N):
    x, y = map(int, input().split())
    ladder[x] = y

for j in range(M):
    u, v = map(int, input().split())
    snake[u] = v

bfs()
print(board[100])

