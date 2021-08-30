# 9095: 1,2,3 더하기

T = int(input())

def solve(N):
    if N == 1:
        return 1
    elif N == 2:
        return 2
    elif N == 3:
        return 4
    else:
        return solve(N-1) + solve(N-2) + solve(N-3)

for _ in range(T):
    print(solve(int(input())))


