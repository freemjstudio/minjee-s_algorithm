# 2*n 타일링 2

N = int(input())
P = [0 for _ in range(1001)]
P[1] = 1
if N == 1:
    print(P[1])
else:
    for i in range(2,N+1):
        if i% 2 == 0:
            P[i] = P[i-1]*2 + 1
        else:
            P[i] = P[i-1]*2 - 1
    print(P[N]%10007)

