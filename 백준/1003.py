import sys


T = int(sys.stdin.readline())

for i in range(T):
    N = int(sys.stdin.readline())
    zero = 1
    one = 0
    temp = 0
    for _ in range(N):
        temp = one
        one = one + zero
        zero = temp
    print(zero, one)

