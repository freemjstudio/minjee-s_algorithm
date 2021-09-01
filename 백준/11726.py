# 11726

N = int(input())
P = [0 for _ in range(1001)]
P[1] = 1
P[2] = 2

if N == 1:
    print(P[1])
elif N == 2:
    print(P[2])
else:
    for i in range(3, N+1):
        P[i] = P[i-1] + P[i-2]
    print(P[N]%10007)


