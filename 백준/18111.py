
import sys

N, M, B = map(int, sys.stdin.readline().split())
ground = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
time = 9223372036854775807
height = 0

for h in range(257):
    bottom = 0
    top = 0

    for i in range(N):
        for j in range(M):
            if ground[i][j] < h:
                bottom += h - ground[i][j]
            else:
                top += ground[i][j] - h

    if bottom > top + B:
        continue
    t = bottom + top * 2
    if t <= time: # 최소시간
        time = t
        height = h
print(time, height)






