# 1012
import sys
sys.setrecursionlimit(10**6)
T = int(sys.stdin.readline())

def search(x,y):
    if x < 0 or x >= N or y < 0 or y >= M:
        return

    if ground[x][y] == 0:
        return

    ground[x][y] = 0

    search(x+1,y)
    search(x,y+1)
    search(x-1,y)
    search(x,y-1)



for _ in range(T):
    M, N, K = map(int, sys.stdin.readline().split()) # 가로, 세로, 배추 수
    ground = [[0] * M for _ in range(N)]

    count = 0

    for _ in range(K):
        x, y = map(int, sys.stdin.readline().split())
        ground[y][x] = 1 # 이게 이해가 안된다...

    for i in range(N):
        for j in range(M):
            if ground[i][j] == 1:
                search(i,j)
                count += 1
    print(count)

