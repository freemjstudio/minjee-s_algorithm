# 2407

n, m = map(int, input().split())

def solve(n):
    temp = 1
    for i in range(n):
        temp *= (i+1)
    return temp



print(solve(n)//(solve(n-m)*solve(m)))


n, m = map(int, input().split())

def solve(n):
    if n == 1:
        return 1
    return solve(n-1)*n

print(solve(n)//(solve(n-m)*solve(m)))