# 9461
import sys

P = [0 for i in range(101)]
P[1] = 1
P[2] = 1
P[3] = 1
for i in range(0,98):
    P[i+3] = P[i] + P[i+1]

T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    print(P[N])

