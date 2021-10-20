

def solve(n):
    if n == 1:
        return 1
    return solve(n-1)*n

print(solve(5))