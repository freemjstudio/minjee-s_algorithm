# 경쟁적 전염
import sys
sys.setrecursionlimit(100000)
n, k = map(int, sys.stdin.readline().split())
data = []
for _ in range(n):
    data.append(list(map(int, sys.stdin.readline().split())))

s, x, y = map(int, sys.stdin.readline().split())

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def virus(ax,ay,v): # virus 종류는 v
    for i in range(4):
        nx = ax + dx[i]
        ny = ay + dy[i]
        if nx >= 0 and ny >= 0 and nx < n and ny < n:
            if data[nx][ny] == 0:
                data[nx][ny] = v


while True:
    count = 1
    for v in range(k+1):
        for i in range(n):
            for j in range(n):
                if data[i][j] == v:
                    virus(i,j,v)
    count += 1
    if count == s:
        break



print(data[x-1][y-1])