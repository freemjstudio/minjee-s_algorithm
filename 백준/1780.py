# 1780 종이의 개수
import sys

N = int(sys.stdin.readline())
matrix = []
result = [0]*3

for i in range(N):
    matrix.append(list(map(int, sys.stdin.readline().split())))

def check(x,y,N):
    temp = matrix[x][y]
    for i in range(N):
        for j in range(N):
            if temp != matrix[x+i][y+j]:
                return False
    return True

def divide(x,y,N):
    if check(x,y,N):
        result[matrix[x][y] +1] += 1
    else:
        for i in range(3):
            for j in range(3):
                divide(x + i*N//3, y+j*N//3, N//3)


divide(0,0,N)
for i in range(3):
    print(result[i])
