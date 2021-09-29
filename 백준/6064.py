# 6064 카잉달력

def solve(M,N,x,y):
    while x <= M*N:
        if (x - y) % N == 0:
            return x
        x += M
    return -1


N = int(input())
for _ in range(N):
    M,N,x,y = map(int, input().split())
    print(solve(M,N,x,y))